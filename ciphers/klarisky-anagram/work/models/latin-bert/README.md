---
language: la
license: apache-2.0
library_name: transformers
tags:
  - latin
  - bert
  - nlp
  - classics
pipeline_tag: fill-mask
---

# Latin BERT (Bamman & Burns 2020)

HuggingFace-compatible packaging of the Latin BERT model from:

> Bamman, D., & Burns, P.J. (2020). [Latin BERT: A Contextual Language Model for Classical Philology](https://arxiv.org/abs/2009.10053). *arXiv preprint arXiv:2009.10053*.

The original model and training code are available at [github.com/dbamman/latin-bert](https://github.com/dbamman/latin-bert). This repo repackages the same weights for use with HuggingFace `transformers`.

**Note:** This is an experimental repackaging. If you encounter any issues, please open a thread in the [Discussion tab](https://huggingface.co/latincy/latin-bert/discussions).

## Model Details

- **Version**: 1.1.2 (tokenizer fix — see [Changelog](#changelog))
- **Architecture**: BERT-base (12 layers, 768 hidden, 12 attention heads)
- **Parameters**: ~111M
- **Vocab size**: 32,900 (SubwordTextEncoder)
- **Max sequence length**: 512
- **Training data**: Latin texts (see paper for details)

## Install

```bash
pip install transformers torch
```

## Usage

### Basic: Get contextual embeddings

```python
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "latincy/latin-bert", trust_remote_code=True
)
model = AutoModel.from_pretrained("latincy/latin-bert")

inputs = tokenizer("Gallia est omnis divisa in partes tres", return_tensors="pt")
outputs = model(**inputs)

# outputs.last_hidden_state: (batch, seq_len, 768)
```

### Masked language model (fill-mask)

```python
from transformers import AutoTokenizer, BertForMaskedLM
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "latincy/latin-bert", trust_remote_code=True
)
model = BertForMaskedLM.from_pretrained("latincy/latin-bert")

text = "Gallia est omnis [MASK] in partes tres"
inputs = tokenizer(text, return_tensors="pt")
mask_idx = (inputs["input_ids"] == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]

with torch.no_grad():
    logits = model(**inputs).logits

top5 = logits[0, mask_idx, :].topk(5).indices.squeeze()
for token_id in top5:
    print(tokenizer.decode([token_id.item()]))
```

## Custom Tokenizer

The original Latin BERT uses a tensor2tensor `SubwordTextEncoder`, not standard
WordPiece. This repo includes a faithful reimplementation as a HuggingFace
`PreTrainedTokenizer` — this is why `trust_remote_code=True` is required.

Verified against the original case studies from the paper:

**POS tagging** (Table 1)

| Treebank | Accuracy |
|----------|----------|
| Perseus  | 95.2%    |
| PROIEL   | 98.2%    |
| ITTB     | 99.2%    |

**Masked word prediction** (Table 3)

| Metric | Score |
|--------|-------|
| P@1    | 33.1% |
| P@10   | 62.2% |
| P@50   | 74.0% |

## spaCy Integration

Works with [spacy-transformers](https://github.com/explosion/spacy-transformers):

```ini
[components.transformer.model]
@architectures = "spacy-transformers.TransformerModel.v3"
name = "latincy/latin-bert"

[components.transformer.model.tokenizer_config]
trust_remote_code = true
use_fast = false
```

## Changelog

### v1.1.2 — Bug fix: whitespace-split before subword encoding

The HF tokenizer's full-string path did character-class splitting on the
entire string. Unlike the original tensor2tensor `tokenizer.encode` (and
the GitHub `gen_berts.py` `LatinTokenizer`, which splits on whitespace
first), it did not drop inter-word spaces, so it escaped every space to
`\32;_` and injected spurious subtokens between every word. This corrupted
masked-word predictions and broke subword→word alignment when calling
`tokenizer("full sentence")` (the documented usage). Both the slow and fast
tokenizers now whitespace-split first, so the native string API reproduces
the original per-word tokenization with no `is_split_into_words` needed.
The fast tokenizer also gained the `do_lower_case` normalizer it was
previously missing (it had ignored the flag, escaping capitals to
codepoints exactly as the slow tokenizer did before v1.1.1). Decode now
renders word boundaries as spaces (BERT-style; `"tres."` → `"tres ."`).

Verified: the native full-string path reproduces the paper's infilling
metrics exactly (P@1 33.1% / P@10 62.2% / P@50 74.0%, n=1161), identical
to the per-word path, and recovers the reported masked words (e.g. Caesar
*aliam*, Livy *primo*). The full case-study suite reproduces through the
native path — POS tagging (95.2 / 98.2 / 99.2%), WSD (0.764), and the §4.4
contextual nearest neighbors (Tables 6–7: top cosine 0.835 for *in* and
0.919 for *audentes*, with the paper's lexical variants *audentis* /
*audaces* / *audentem* retrieved).

Responds to [discussion #3](https://huggingface.co/latincy/latin-bert/discussions/3) —
thanks to aimgo for the report.

### v1.1.1 — Bug fix: add `do_lower_case=True` to tokenizer

The original Latin BERT vocabulary was trained on lowercased text. All original
case studies (POS tagging, WSD, infilling) explicitly called `.lower()` before
tokenizing. The HF `PreTrainedTokenizer` wrapper was missing this step, causing
uppercase characters to be escaped to their ASCII codepoints (e.g. `C` →
`\67;`), inflating token counts ~4x and producing embeddings the model was never
trained on. The tokenizer now lowercases input by default (`do_lower_case=True`),
matching the original pipeline behavior.

### v1.1.0 — HuggingFace repackaging

Repackaged the original tensor2tensor `SubwordTextEncoder` tokenizer and
PyTorch weights as a HuggingFace `PreTrainedTokenizer` + `safetensors` model.

### v1.0.0 — Original model

Bamman & Burns (2020) Latin BERT weights and tensor2tensor tokenizer.

## Citation

```bibtex
@article{bamman2020latin,
  title={Latin BERT: A Contextual Language Model for Classical Philology},
  author={Bamman, David and Burns, Patrick J},
  journal={arXiv preprint arXiv:2009.10053},
  year={2020}
}
```
