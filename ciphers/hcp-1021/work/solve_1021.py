#!/usr/bin/env python3
"""HCP 1021 - decode the Pigpen line on the picture side (Claude Opus 5.5, 2026-10-29/30).

Run from the repo root:  python3 -I ciphers/hcp-1021/work/solve_1021.py

The cipher line runs along the TOP edge of the picture side but was written with
the card turned 180 degrees (the letters stand on the frame line, the comma-like
word dividers descend below it).  Shapes below are therefore described with the
card rotated 180 degrees, and listed in that reading order (left to right after
rotation = right to left on the scan as stored).  Glyph ids are the ids of
work/transcript.json (earlier GPT geometry boxes, original orientation).

Shape names (walls present, after 180-degree rotation; '.' = dot inside):
  BR = right+bottom (_|)   U = left+right+bottom   BL = left+bottom (|_)
  TRB = top+right+bottom   BOX = all four          TLB = top+left+bottom
  TR = top+right           TLR = top+left+right    TL = top+left
  V = sector open upwards  LT = '<' sector
"""
import hashlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / "source"
EXPECTED = {
    "picture.jpg": "d0ab8297410a28a74b38d35ba20daeb1cdae000263b455d4f731356c1b80cb2c",
    "address.jpg": "7a54e02489a958e54293b6cbdfdcdcc29ef6166d02c5a7fa0f7c4b2ac095fd64",
    "metadata.md": "0d799c33f63caeb7b67023dfef803acdeb0cc006207cfd7fd868c46b3053287c",
}
for name, sha in EXPECTED.items():
    got = hashlib.sha256((SRC / name).read_bytes()).hexdigest()
    if got != sha:
        sys.exit(f"hash mismatch for source/{name}: {got}")
    print("SHA256 ok", name)

# Standard Pigpen (tic-tac-toe A-I, dotted J-R, X: S top, T left, U right, V bottom)
GRID = ["BR", "U", "BL", "TRB", "BOX", "TLB", "TR", "TLR", "TL"]
KEY = {}
for i, s in enumerate(GRID):
    KEY[s] = chr(65 + i)          # A..I
    KEY[s + "."] = chr(74 + i)    # J..R
KEY.update({"V": "S", "GT": "T", "LT": "U", "WEDGE": "V"})

# Reading order (card turned 180 deg). (glyph id, shape). '|' = divider. 'X' = cancelled.
LINE = [
    (29, "TL."), (28, "BR"), (27, "TRB"), (26, "X"), (25, "TLB"),
    (24, "BR"),            # drawn as a T: horizontal joins a little above the foot of the vertical
    (23, "TL."), (22, "BOX"), (21, "BOX."), "|",
    (20, "V"), (19, "TLB."), (18, "BL."), (17, "BL."), "|",
    (16, "BL."), (15, "BOX"), (14, "U"), (13, "BOX"), (12, "BOX."), "|",
    (11, "BR"),            # same T-like A as id 24
    (10, "BL."), (9, "BL."), "|",
    (8, "TLR"), (7, "BOX"), (6, "TL"), (5, "BL."), "|",
    (4, "TR"), (3, "TL."), (2, "LT"), (1, "V"), "|",
]

words, cur, detail = [], "", []
for item in LINE:
    if item == "|":
        words.append(cur); cur = ""; continue
    gid, shape = item
    p = "[x]" if shape == "X" else KEY[shape]
    detail.append(f"{gid}:{shape}={p}")
    cur += p
print("glyphs:", " ".join(detail))
print("cipher plaintext:", " ".join(words))
assert " ".join(words) == "RAD[x]FAREN SOLL LEBEN ALL HEIL GRUS", words
print("normalised:      Radfahren soll leben! All Heil! Gruß")
