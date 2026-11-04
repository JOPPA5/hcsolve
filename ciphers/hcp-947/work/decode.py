#!/usr/bin/env python3
"""HCP 947: decode the three-line sign block on the address side.

Run from the repo root:  python3 -I ciphers/hcp-947/work/decode.py
Verifies source hashes, then maps the manual sign transcription through the key.
"""
import hashlib, os, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HASHES = {
    "source/address-large.jpg": "c6cfe6d5e2a0930ac254c2b861168c98fc33e59079c31f37ff87e98d9bfc954d",
    "source/picture-large.jpg": "fd3093690ba62e29d0617845a61e79df0067a79fc90f05c10b45c70472b76d83",
    "work/hires/cpc_1909-06-03_DE_Doberan_DE_Reddelich_ernagarbe-03_adr.jpg": "c0aaf9c9696c2c5518023a3bf827119fef57949758ad44d5d6e9f76c4e090e10",
    "work/hires/cpc_1909-06-03_DE_Doberan_DE_Reddelich_ernagarbe-03_pic.jpg": "357be9cb547d3b2b5b51c305366b5f80491cde5304fe6de72abfcf7234fb0ba6",
}
for rel, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(BASE, rel), "rb").read()).hexdigest()
    if got != h:
        sys.exit(f"HASH MISMATCH {rel}: {got}")
print("source hashes OK")

# Sign names describe what is drawn on the card (orientation as the card is held
# with the cursive upright). ',-' and '!-' are punctuation written normally.
TRANSCRIPTION = [
    ["INV_A", "BRACKET_C", "H_BARRED", ",-"],                       # line 1
    ["LAMBDA_STEM", "INV_A_MARK", "ZIGZAG", "EIGHT", "INV_T", ",-"],   # line 2
    ["REV_D", "PI", ",-", "IBEAM", "INV_i", "THREE", "ZIGZAG", "!-"],  # line 3
]
KEY = {
    "INV_A": "A",        # ∀, upside-down A (pixel shape)
    "INV_A_MARK": "A",   # ∀ with a mark above it; possibly umlaut -> Ä (uncertain)
    "BRACKET_C": "C",    # bracket/hooked C (word sense for ACH)
    "H_BARRED": "H",     # H-like sign with extra strokes (word sense for ACH)
    "LAMBDA_STEM": "W",  # Λ with faint central stem = inverted W (shape + word sense)
    "ZIGZAG": "R",       # zigzag Σ-like sign, twice (word sense: WÄRST, HIER)
    "EIGHT": "S",        # 8-shaped closed S (word sense)
    "INV_T": "T",        # ⊥, upside-down T
    "REV_D": "D",        # ᗡ, D turned 180°
    "PI": "U",           # Π, upside-down U
    "IBEAM": "H",        # 工, H turned 90° (word sense)
    "INV_i": "I",        # stroke above, dot below = i turned 180°
    "THREE": "E",        # 3 = cursive Ɛ turned 180°
}
# ",-" is a word separator written after every word (not a comma in the
# plaintext); "!-" closes the message with an exclamation mark.
PUNCT = {",-": " ", "!-": "!"}
words, cur = [], ""
for line in TRANSCRIPTION:
    for sg in line:
        if sg in PUNCT:
            words.append(cur + ("!" if sg == "!-" else ""))
            cur = ""
        else:
            cur += KEY[sg]
print("lines    :", " | ".join(" ".join(KEY.get(x, x) for x in line) for line in TRANSCRIPTION))
print("words    :", " / ".join(words))
print("plaintext:", " ".join(words))
print("reading  : Ach, wärst du hier!  (umlaut on A from the mark above sign 2 of line 2 / word sense)")
