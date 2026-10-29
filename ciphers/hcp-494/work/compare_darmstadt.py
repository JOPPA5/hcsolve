"""Reproduce a small, manually transcribed incompatibility check.

This is not an OCR transcription or a full edition of either auxiliary key.
The values below were read from delivered full-size archive images, with
the target's manuscript gloss readings already known.
"""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
cells = [
    {"code": "20", "darmstadt239": "c", "hcp255": "a"},
    {"code": "28", "darmstadt239": "w", "hcp255": "e"},
    {"code": "83", "darmstadt239": "g", "hcp255": "r"},
    {"code": "117", "darmstadt239": "d", "hcp255": "t"},
]
words = [
    {"word": "France", "darmstadt239": "167", "hcp494_gloss_supported": "576"},
    {"word": "Holland", "darmstadt239": "187", "hcp494_gloss_supported": "774"},
    {"word": "Emperor", "darmstadt239": "194", "hcp494_gloss_supported": "602"},
]
assert all(r["darmstadt239"] != r["hcp255"] for r in cells)
assert all(r["darmstadt239"] != r["hcp494_gloss_supported"] for r in words)
paths = [
    "source/arcinsys/darmstadt239-full/hstad_d_4_nr_239--1_008.jpg",
    "source/arcinsys/darmstadt239-full/hstad_d_4_nr_239--1_010.jpg",
    "source/arcinsys/darmstadt239-full/hstad_d_4_nr_239--1_011.jpg",
    "source/arcinsys/darmstadt206-full/hstad_d_4_nr_206--6_061.jpg",
    "source/arcinsys/darmstadt206-full/hstad_d_4_nr_206--6_062.jpg",
    "source/full/key255.jpg",
    "source/full/0004.jpg",
]
result = {
    "accepted_hcp494_plaintext": None,
    "letter_cells": cells,
    "word_entries": words,
    "darmstadt239_other_evidence": "Images 009-010 include numeric cipher with interlinear readings. Images 010-011 give the associated word list and special ruler signs; the Danish king has a graphic sign, not target 834. These are auxiliary evidence, not another copy of HCP 494.",
    "darmstadt206": "Image 061 dates the alphabet wrapper to 1658. Image 062 has a one-column letter/graphic-sign substitution and an Otiosa list, not the HCP 494 homophonic numeric table or expanded word list.",
    "limits": "Manual samples establish that these particular keys are not identical. They do not exclude undocumented derivation, later variants, or other key material elsewhere in the files. Thumbnails were used only to select full-size pages.",
    "source_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
}
(ROOT/'work/darmstadt-comparison.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
