"""Fast tokenizer for Bamman & Burns (2020) Latin BERT.

Provides word_ids() support via a Rust-backed tokenizers.Tokenizer.
The pre-tokenization (character-class splitting + escaping) runs in
Python; the subword model (WordPiece, greedy longest-match) and
post-processing (BertProcessing) run in Rust.

This is needed by frameworks like Flair and Stanza that rely on
word_ids() to align subword embeddings back to word-level tokens.

Usage:
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(
        "latincy/latin-bert", trust_remote_code=True, use_fast=True
    )
    enc = tokenizer("Gallia est omnis", return_tensors="pt")
    enc.word_ids()  # [None, 0, 1, 2, None]  (each word maps to its subtokens)
"""

import os
import re
import unicodedata
from typing import Dict, List, Optional, Tuple

from tokenizers import Tokenizer, normalizers, pre_tokenizers, processors
from tokenizers.models import WordPiece
from tokenizers.pre_tokenizers import PreTokenizer
from transformers import PreTrainedTokenizerFast


# ── Character-class tokenizer ──────────────────────────────────────────
# Reproduces tensor2tensor.data_generators.tokenizer.encode()

_ALPHANUMERIC_CHAR_SET = set()
for _i in range(0x110000):
    _c = chr(_i)
    _cat = unicodedata.category(_c)
    if _cat.startswith("L") or _cat.startswith("N"):
        _ALPHANUMERIC_CHAR_SET.add(_c)

_ESCAPE_CHARS = set("\\_u;0123456789")


def _tokenizer_encode(text: str) -> List[Tuple[str, int, int]]:
    """Split text at alphanumeric / non-alphanumeric boundaries.

    Returns list of (token_text, start_offset, end_offset).
    """
    if not text:
        return []
    tokens = []
    start = 0
    is_alnum = text[0] in _ALPHANUMERIC_CHAR_SET
    for i in range(1, len(text)):
        c_is_alnum = text[i] in _ALPHANUMERIC_CHAR_SET
        if c_is_alnum != is_alnum:
            tokens.append((text[start:i], start, i))
            start = i
            is_alnum = c_is_alnum
    tokens.append((text[start:], start, len(text)))
    return tokens


def _escape_token(token: str, alphabet: set) -> str:
    """Escape a token and append word boundary marker.

    Reproduces tensor2tensor _escape_token():
      - \\ → \\\\
      - _  → \\u
      - out-of-alphabet chars → \\<ordinal>;
      - append trailing _ (word boundary marker)
    """
    token = token.replace("\\", "\\\\").replace("_", "\\u")
    ret = []
    for c in token:
        if c in alphabet and c != "\n":
            ret.append(c)
        else:
            ret.append("\\%d;" % ord(c))
    return "".join(ret) + "_"


# ── Custom pre-tokenizer ───────────────────────────────────────────────

class _LatinBertPreTokenizer:
    """Custom pre-tokenizer: character-class split + escape + append '_'.

    Applied AFTER a WhitespaceSplit pre-tokenizer (see
    _build_backend_tokenizer), so it receives one whitespace-delimited
    word at a time and splits it at alphanumeric/non-alphanumeric
    boundaries (e.g. "tres," → "tres_", ",_"). It never sees inter-word
    spaces, so no `\\32;_` space-escapes are produced.
    """

    def __init__(self, alphabet: set):
        self.alphabet = alphabet

    def pre_tokenize_str(self, text: str) -> List[Tuple[str, Tuple[int, int]]]:
        tokens = _tokenizer_encode(text)
        result = []
        for tok_text, start, end in tokens:
            escaped = _escape_token(tok_text, self.alphabet)
            result.append((escaped, (start, end)))
        return result

    def pre_tokenize(self, pretok):
        pretok.split(self._split)

    def _split(self, i, normalized):
        text = str(normalized)
        tokens = _tokenizer_encode(text)
        splits = []
        for tok_text, start, end in tokens:
            escaped = _escape_token(tok_text, self.alphabet)
            slice_ = normalized[start:end]
            slice_.replace(slice_.normalized, escaped)
            splits.append(slice_)
        return splits


# ── BERT special tokens ───────────────────────────────────────────────

SPECIAL_TOKENS = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
NUM_SPECIAL = 5

VOCAB_FILES_NAMES = {"vocab_file": "latin.subword.encoder"}


def _build_backend_tokenizer(vocab_file: str, do_lower_case: bool = True) -> Tokenizer:
    """Build a tokenizers.Tokenizer from the SubwordTextEncoder vocab."""
    # Load subword vocab
    subtoken_strings = []
    with open(vocab_file, encoding="utf-8") as f:
        for line in f:
            s = line.rstrip()
            if (s.startswith("'") and s.endswith("'")) or (
                s.startswith('"') and s.endswith('"')
            ):
                s = s[1:-1]
            subtoken_strings.append(s)

    # Build vocab dict: special tokens at 0-4, subtokens at 5+
    vocab: Dict[str, int] = {}
    for i, tok in enumerate(SPECIAL_TOKENS):
        vocab[tok] = i
    for i, st in enumerate(subtoken_strings):
        if st:  # skip empty strings
            vocab[st] = i + NUM_SPECIAL

    # Build alphabet for escaping
    alphabet = {c for token in subtoken_strings for c in token}
    alphabet |= _ESCAPE_CHARS

    # WordPiece with no continuation prefix = greedy longest-match
    # (same algorithm as SubwordTextEncoder)
    model = WordPiece(
        vocab=vocab,
        unk_token="[UNK]",
        continuing_subword_prefix="",
        max_input_chars_per_word=10000,
    )
    tokenizer = Tokenizer(model)

    # Normalizer: lowercase (the vocab was trained on lowercased text;
    # matches the slow tokenizer's do_lower_case=True). Without this,
    # uppercase chars fall outside the alphabet and get escaped to their
    # codepoints (e.g. 'G' → `\71;`), inflating tokens and producing
    # embeddings the model never saw.
    if do_lower_case:
        tokenizer.normalizer = normalizers.Lowercase()

    # Pre-tokenizer: whitespace-split FIRST (drops inter-word spaces,
    # keeps punctuation attached), then char-class split + escape + '_'
    # per word. Splitting on whitespace first is essential — otherwise
    # spaces are escaped to `\32;_` and injected between words, corrupting
    # the model input and breaking word_ids() alignment. WhitespaceSplit
    # preserves offsets, so word_ids() maps subtokens to the right words.
    tokenizer.pre_tokenizer = pre_tokenizers.Sequence([
        pre_tokenizers.WhitespaceSplit(),
        PreTokenizer.custom(_LatinBertPreTokenizer(alphabet)),
    ])

    # BertProcessing: adds [CLS] at start, [SEP] at end
    tokenizer.post_processor = processors.BertProcessing(
        sep=("[SEP]", vocab["[SEP]"]),
        cls=("[CLS]", vocab["[CLS]"]),
    )

    return tokenizer


# ── HuggingFace fast tokenizer ─────────────────────────────────────────

class LatinBertTokenizerFast(PreTrainedTokenizerFast):
    """Fast tokenizer for Bamman & Burns (2020) Latin BERT.

    Wraps the SubwordTextEncoder as a Rust-backed tokenizers.Tokenizer,
    providing word_ids() and other fast-tokenizer features needed by
    frameworks like Flair and Stanza.

    IDs 0-4 are reserved for BERT special tokens:
      0=[PAD], 1=[UNK], 2=[CLS], 3=[SEP], 4=[MASK]
    SubwordTextEncoder subtokens are shifted to start at ID 5.
    """

    vocab_files_names = VOCAB_FILES_NAMES
    model_input_names = ["input_ids", "attention_mask"]
    slow_tokenizer_class = None  # set below after import

    def __init__(
        self,
        vocab_file: Optional[str] = None,
        tokenizer_object: Optional[Tokenizer] = None,
        do_lower_case: bool = True,
        pad_token: str = "[PAD]",
        unk_token: str = "[UNK]",
        cls_token: str = "[CLS]",
        sep_token: str = "[SEP]",
        mask_token: str = "[MASK]",
        eos_token: str = "<EOS>_",
        **kwargs,
    ):
        if tokenizer_object is None and vocab_file is not None:
            tokenizer_object = _build_backend_tokenizer(
                vocab_file, do_lower_case=do_lower_case
            )
        self.do_lower_case = do_lower_case

        # PreTrainedTokenizerFast.__init__ does deepcopy(tokenizer_object),
        # which fails for custom Python pre-tokenizers. Bypass by setting
        # the backend tokenizer directly.
        self._tokenizer = tokenizer_object
        self.vocab_file = vocab_file

        # Call grandparent init (PreTrainedTokenizer) which handles
        # special tokens, model_max_length, etc. without deepcopy.
        from transformers import PreTrainedTokenizerBase
        PreTrainedTokenizerBase.__init__(
            self,
            pad_token=pad_token,
            unk_token=unk_token,
            cls_token=cls_token,
            sep_token=sep_token,
            mask_token=mask_token,
            eos_token=eos_token,
            **kwargs,
        )

        # Ensure added_tokens_encoder is populated for special tokens
        self._add_tokens(
            [pad_token, unk_token, cls_token, sep_token, mask_token],
            special_tokens=True,
        )

    @staticmethod
    def _unescape(text: str) -> str:
        """Reverse the t2t escape encoding used by the pre-tokenizer.

        Word-boundary underscores become spaces (BERT-style decode;
        punctuation spacing is lossy). Literal underscores are encoded
        as ``\\u`` and restored afterward.
        """
        text = re.sub(r"(?<!\\)_", " ", text)
        text = re.sub(r"\\(\d+);", lambda m: chr(int(m.group(1))), text)
        text = text.replace("\\u", "_").replace("\\\\", "\\")
        return text.strip()

    def convert_tokens_to_string(self, tokens: List[str]) -> str:
        """Reverse tokenization: unescape t2t encoding and join."""
        filtered = [t for t in tokens if t not in SPECIAL_TOKENS]
        return self._unescape("".join(filtered))

    def _decode(
        self,
        token_ids: List[int],
        skip_special_tokens: bool = False,
        **kwargs,
    ) -> str:
        # Convert IDs to token strings via the backend
        tokens = [self._tokenizer.id_to_token(i) for i in token_ids if i is not None]
        if skip_special_tokens:
            tokens = [t for t in tokens if t not in SPECIAL_TOKENS]
        else:
            tokens = [t for t in tokens if t is not None]
        return self._unescape("".join(tokens))

    def save_vocabulary(
        self, save_directory: str, filename_prefix: Optional[str] = None
    ) -> Tuple[str]:
        if not os.path.isdir(save_directory):
            os.makedirs(save_directory, exist_ok=True)
        prefix = filename_prefix + "-" if filename_prefix else ""
        out_path = os.path.join(
            save_directory, prefix + VOCAB_FILES_NAMES["vocab_file"]
        )
        if self.vocab_file and os.path.abspath(self.vocab_file) != os.path.abspath(out_path):
            import shutil
            shutil.copy(self.vocab_file, out_path)
        return (out_path,)


# Wire up slow_tokenizer_class for auto-conversion
try:
    from tokenization_latin_bert import LatinBertTokenizer
    LatinBertTokenizerFast.slow_tokenizer_class = LatinBertTokenizer
except ImportError:
    pass
