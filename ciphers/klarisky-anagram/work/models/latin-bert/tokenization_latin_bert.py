"""HuggingFace PreTrainedTokenizer for Bamman & Burns (2020) Latin BERT.

Faithfully reproduces the original tensor2tensor SubwordTextEncoder
tokenization pipeline without requiring TensorFlow. Verified against
the original POS tagging case study (Perseus 95.2%, ITTB 99.2%,
PROIEL 98.2% — matching or exceeding paper targets).

The tokenization pipeline:
  1. Character-class splitting (alphanumeric vs non-alphanumeric boundaries)
  2. Escape special characters (backslash, underscore, out-of-alphabet)
  3. Append trailing underscore (word boundary marker)
  4. Greedy longest-match against subword vocabulary

IDs 0-4 are reserved for BERT special tokens ([PAD], [UNK], [CLS],
[SEP], [MASK]). SubwordTextEncoder subtokens start at ID 5.

Usage:
    from transformers import AutoModel, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(
        "latincy/latin-bert", trust_remote_code=True
    )
    model = AutoModel.from_pretrained("latincy/latin-bert")

    inputs = tokenizer("Gallia est omnis divisa in partes tres",
                        return_tensors="pt")
    outputs = model(**inputs)
"""

import os
import re
import unicodedata
from typing import Dict, List, Optional, Tuple

from transformers import PreTrainedTokenizer


# ── Character-class tokenizer ──────────────────────────────────────────
# Reproduces tensor2tensor.data_generators.tokenizer.encode()

_ALPHANUMERIC_CHAR_SET = set()
for _i in range(0x110000):
    _c = chr(_i)
    _cat = unicodedata.category(_c)
    if _cat.startswith("L") or _cat.startswith("N"):
        _ALPHANUMERIC_CHAR_SET.add(_c)

_ESCAPE_CHARS = set("\\_u;0123456789")


def _tokenizer_encode(text: str) -> List[str]:
    """Split text at alphanumeric / non-alphanumeric boundaries."""
    if not text:
        return []
    tokens = []
    current = [text[0]]
    is_alnum = text[0] in _ALPHANUMERIC_CHAR_SET
    for c in text[1:]:
        c_is_alnum = c in _ALPHANUMERIC_CHAR_SET
        if c_is_alnum == is_alnum:
            current.append(c)
        else:
            tokens.append("".join(current))
            current = [c]
            is_alnum = c_is_alnum
    tokens.append("".join(current))
    return tokens


def _escape_token(token: str, alphabet: set) -> str:
    """Escape a token before subword encoding.

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


# ── BERT special tokens ───────────────────────────────────────────────

SPECIAL_TOKENS = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
NUM_SPECIAL = 5  # IDs 0-4 reserved for BERT special tokens

# ── HuggingFace tokenizer ─────────────────────────────────────────────

# Vocab file name expected by HF save/load
VOCAB_FILES_NAMES = {"vocab_file": "latin.subword.encoder"}


class LatinBertTokenizer(PreTrainedTokenizer):
    """HuggingFace tokenizer for Bamman & Burns (2020) Latin BERT.

    Wraps the original tensor2tensor SubwordTextEncoder as a
    PreTrainedTokenizer so it works with AutoTokenizer and standard
    HF pipelines.

    IDs 0-4 are reserved for BERT special tokens:
      0=[PAD], 1=[UNK], 2=[CLS], 3=[SEP], 4=[MASK]
    SubwordTextEncoder subtokens are shifted to start at ID 5.
    """

    vocab_files_names = VOCAB_FILES_NAMES
    model_input_names = ["input_ids", "attention_mask"]

    def __init__(
        self,
        vocab_file: str,
        do_lower_case: bool = True,
        pad_token: str = "[PAD]",
        unk_token: str = "[UNK]",
        cls_token: str = "[CLS]",
        sep_token: str = "[SEP]",
        mask_token: str = "[MASK]",
        eos_token: str = "<EOS>_",
        **kwargs,
    ):
        # Load subword vocabulary before super().__init__ so that
        # special token resolution can use the vocab.
        self._subtoken_strings: List[str] = []
        self._subtoken_to_id: Dict[str, int] = {}
        self._max_subtoken_len: int = 0
        self._alphabet: set = set()
        self._cache_size: int = 2**20
        self._cache: List[Tuple] = [(None, None)] * self._cache_size

        self._load_vocab(vocab_file)
        self.vocab_file = vocab_file
        self.do_lower_case = do_lower_case

        super().__init__(
            pad_token=pad_token,
            unk_token=unk_token,
            cls_token=cls_token,
            sep_token=sep_token,
            mask_token=mask_token,
            eos_token=eos_token,
            **kwargs,
        )

    # ── Vocab loading ──────────────────────────────────────────────

    def _load_vocab(self, filename: str) -> None:
        subtoken_strings = []
        with open(filename, encoding="utf-8") as f:
            for line in f:
                s = line.rstrip()
                if (
                    (s.startswith("'") and s.endswith("'"))
                    or (s.startswith('"') and s.endswith('"'))
                ):
                    s = s[1:-1]
                subtoken_strings.append(s)
        # IDs 0-4 are reserved for BERT special tokens [PAD],[UNK],[CLS],[SEP],[MASK]
        # SubwordTextEncoder subtokens are shifted to IDs 5+
        self._subtoken_strings = subtoken_strings
        self._max_subtoken_len = (
            max(len(s) for s in subtoken_strings) if subtoken_strings else 0
        )
        self._subtoken_to_id = {
            s: i + NUM_SPECIAL for i, s in enumerate(subtoken_strings) if s
        }
        # Also map special tokens to their IDs
        for i, tok in enumerate(SPECIAL_TOKENS):
            self._subtoken_to_id[tok] = i
        self._alphabet = {c for token in subtoken_strings for c in token}
        self._alphabet |= _ESCAPE_CHARS

    # ── PreTrainedTokenizer interface ──────────────────────────────

    @property
    def vocab_size(self) -> int:
        return len(self._subtoken_strings) + NUM_SPECIAL

    def get_vocab(self) -> Dict[str, int]:
        vocab = {tok: i for i, tok in enumerate(SPECIAL_TOKENS)}
        vocab.update(self._subtoken_to_id)
        return vocab

    def _tokenize(self, text: str, **kwargs) -> List[str]:
        """Tokenize text into subtoken strings.

        Splits on whitespace first (like the original gen_berts.py
        LatinTokenizer), then applies character-class splitting within
        each word. This is essential: tensor2tensor's tokenizer.encode()
        drops inter-word spaces, so feeding a full string through
        _tokenizer_encode() directly would escape every space to
        ``\\32;_`` and inject spurious subtokens between words, corrupting
        the input the model was trained on and breaking word alignment.
        Because whitespace-split words contain no spaces, no space escape
        can be produced here.
        """
        if self.do_lower_case:
            text = text.lower()
        subtokens = []
        for word in text.split():
            for token in _tokenizer_encode(word):
                subtokens.extend(self._token_to_subtokens(token))
        return subtokens

    def _token_to_subtokens(self, token: str) -> List[str]:
        """Convert a single word-level token to subtoken strings."""
        cache_location = hash(token) % self._cache_size
        cache_key, cache_value = self._cache[cache_location]
        if cache_key == token:
            return cache_value
        escaped = _escape_token(token, self._alphabet)
        subtokens = self._greedy_match(escaped)
        self._cache[cache_location] = (token, subtokens)
        return subtokens

    def _greedy_match(self, escaped_token: str) -> List[str]:
        """Greedy longest-match against subword vocabulary."""
        ret = []
        start = 0
        token_len = len(escaped_token)
        while start < token_len:
            found = False
            for end in range(
                min(token_len, start + self._max_subtoken_len), start, -1
            ):
                subtoken = escaped_token[start:end]
                if subtoken in self._subtoken_to_id:
                    ret.append(subtoken)
                    start = end
                    found = True
                    break
            if not found:
                ret.append(self.unk_token)
                start += 1
        return ret

    def _convert_token_to_id(self, token: str) -> int:
        return self._subtoken_to_id.get(token, 1)  # 1 = [UNK]

    def _convert_id_to_token(self, index: int) -> str:
        if 0 <= index < NUM_SPECIAL:
            return SPECIAL_TOKENS[index]
        subtoken_index = index - NUM_SPECIAL
        if 0 <= subtoken_index < len(self._subtoken_strings):
            return self._subtoken_strings[subtoken_index]
        return self.unk_token

    def convert_tokens_to_string(self, tokens: List[str]) -> str:
        """Reverse the tokenization: unescape and join.

        Word boundaries are the trailing ``_`` markers, so each is
        rendered as a space (BERT-style; punctuation spacing is lossy,
        e.g. "tres." → "tres ."). Literal underscores are encoded as
        ``\\u`` and are restored afterward.
        """
        # Filter out special tokens before joining
        filtered = [t for t in tokens if t not in SPECIAL_TOKENS]
        text = "".join(filtered)
        # Word-boundary underscores → spaces; then unescape:
        # \\<digits>; → chr, \\u → _, \\\\ → \\
        text = re.sub(r"(?<!\\)_", " ", text)
        text = re.sub(r"\\(\d+);", lambda m: chr(int(m.group(1))), text)
        text = text.replace("\\u", "_").replace("\\\\", "\\")
        return text.strip()

    def build_inputs_with_special_tokens(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None
    ) -> List[int]:
        cls_id = [self.convert_tokens_to_ids("[CLS]")]
        sep_id = [self.convert_tokens_to_ids("[SEP]")]
        if token_ids_1 is None:
            return cls_id + token_ids_0 + sep_id
        return cls_id + token_ids_0 + sep_id + token_ids_1 + sep_id

    def get_special_tokens_mask(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None,
        already_has_special_tokens: bool = False
    ) -> List[int]:
        if already_has_special_tokens:
            return super().get_special_tokens_mask(
                token_ids_0, token_ids_1, already_has_special_tokens=True
            )
        if token_ids_1 is None:
            return [1] + [0] * len(token_ids_0) + [1]
        return [1] + [0] * len(token_ids_0) + [1] + [0] * len(token_ids_1) + [1]

    def create_token_type_ids_from_sequences(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None
    ) -> List[int]:
        sep = [self.convert_tokens_to_ids("[SEP]")]
        cls_ = [self.convert_tokens_to_ids("[CLS]")]
        if token_ids_1 is None:
            return [0] * (len(cls_) + len(token_ids_0) + len(sep))
        return [0] * (len(cls_) + len(token_ids_0) + len(sep)) + [1] * (len(token_ids_1) + len(sep))

    def save_vocabulary(
        self, save_directory: str, filename_prefix: Optional[str] = None
    ) -> Tuple[str]:
        if not os.path.isdir(save_directory):
            os.makedirs(save_directory, exist_ok=True)
        prefix = filename_prefix + "-" if filename_prefix else ""
        vocab_path = os.path.join(
            save_directory, prefix + VOCAB_FILES_NAMES["vocab_file"]
        )
        with open(vocab_path, "w", encoding="utf-8") as f:
            for subtoken in self._subtoken_strings:
                f.write(f"'{subtoken}'\n")
        return (vocab_path,)
