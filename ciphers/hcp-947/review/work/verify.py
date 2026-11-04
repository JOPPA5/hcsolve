#!/usr/bin/env python3
"""Reviewer's independent decode of hcp-947 (sign block, address side, left margin).
Hypothesis: each letter is drawn rotated 180 deg (or turned) in normal left-to-right order.
Sign names are the reviewer's own, read from review/work/l1.png, l2.png, l3.png."""
ROT180 = {  # what an upright letter looks like turned 180 deg -> letter
    "∀": "A", "⊥": "T", "Π": "U", "ᗡ": "D", "Ɛ(3)": "E", "!(i turned)": "I",
    "8(S)": "S", "C": "C", "H": "H",
}
WORDSENSE = {"Λ+stem": "W", "Σ": "R", "工": "H"}  # not pure rotations; rest on word sense
K = {**ROT180, **WORDSENSE}
rows = [["∀", "C", "H"],
        ["Λ+stem", "∀", "Σ", "8(S)", "⊥"],
        ["ᗡ", "Π"], ["工", "!(i turned)", "Ɛ(3)", "Σ"]]
words = ["".join(K[s] for s in w) for w in rows]
print(" ".join(words))
print("signs by rotation only:", "".join(K[s] if s in ROT180 else "?" for w in rows for s in w))
