"""Reviewer's independent Ogham decoder for hcp-915 (own transcription, read from review/work crops).
Groups: (side, count, mark) with side U=above stem only, D=below stem only, C=perpendicular across,
S=slanted across, BAR=horizontal bar above; mark '.'=dot above, "'"=acute above."""
OGHAM = {("D", 1): "b", ("D", 2): "l", ("D", 3): "f", ("D", 4): "s", ("D", 5): "n",
         ("U", 1): "h", ("U", 2): "d", ("U", 3): "t", ("U", 4): "c", ("U", 5): "q",
         ("S", 1): "m", ("S", 2): "g", ("S", 3): "ng", ("S", 4): "z", ("S", 5): "r",
         ("C", 1): "a", ("C", 2): "o", ("C", 3): "u", ("C", 4): "e", ("C", 5): "i"}
words = [
    [("U", 2, ""), ("C", 1, ""), ("D", 1, "."), ("C", 1, ""), ("C", 5, ""), ("S", 5, "")],
    [("U", 2, ""), ("C", 2, ""), ("S", 1, "")],
    [("BAR", 1, ""), ("C", 2, "'"), ("S", 2, "")],
]
out = []
for w in words:
    s = ""
    for side, n, mark in w:
        ch = "p?" if side == "BAR" else OGHAM[(side, n)]
        if mark == ".": ch += "h"
        if mark == "'": ch = {"a": "á", "o": "ó", "u": "ú", "e": "é", "i": "í"}[ch]
        s += ch
    out.append(s)
print("groups:", sum(len(w) for w in words), "decoded:", " ".join(out) + ".")
