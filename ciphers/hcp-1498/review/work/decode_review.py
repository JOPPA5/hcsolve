#!/usr/bin/env python3
"""Reviewer's independent Pigpen decoder (does not use the solver's code).
Glyph notation: grid cell 1..9 numbered row-major in the # grid
(1 = lines right+bottom, 2 = left+right+bottom, 3 = left+bottom,
 4 = top+right+bottom, 5 = box, 6 = top+left+bottom,
 7 = top+right, 8 = top+left+right, 9 = top+left);
X wedges by opening: v (S), > (U), < (W), ^ (Y).
Suffix '.' = dotted (second letter of the pair).  '?' = unreadable glyph."""
import sys, string
cells = list("123456789") + list("v><^")
key = {}
for i, c in enumerate(cells):
    key[c] = string.ascii_uppercase[2*i]
    key[c + "."] = string.ascii_uppercase[2*i + 1]
def dec(tok):
    return key.get(tok, "?")
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.rstrip("\n")
    if not line or line.startswith("#"):
        print(line); continue
    words = line.split("|")[0].split("/")
    print(" ".join("".join(dec(t) for t in w.split()) for w in words), "  ", line.split("|")[1].strip() if "|" in line else "")
