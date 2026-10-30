#!/usr/bin/env python3
"""Reviewer's independent reading of hcp-1486 (Claude Opus 5.5, review round 1).
Own visual left-to-right transcription from review/work crops; dots omitted.
Sign classes (own labels): P = pi-form T (bar + two legs), Z = bar + 3/z-shaped
descending stem, Q = looped sign with tail (you/quite), A = crossed loop (word 'a'),
G = descender loop (are), W = xi-form w, N = 3-form n, L = horizontal loop,
S = open u/v-shaped loop, F = tall looped stroke, D = capital D, U = M-like u.
Run: python3 -I review/work/indep_decode.py  (from the cipher dir or anywhere)"""
VIS = [
    "U o Q / t n o D",
    "A / s i h P / k n i h P",
    "t h g i r F / A / f o / t i Z",
    "l l / e r G / U o Q / e p o Z",
    "a h S / l l e W / e t i u Q",
    "y a d s e u P / n w o d / e Z",
    "e v o L / h t i W / t h g i N",
]
# context-free values for unambiguous classes
FIX = {"U": "u", "A": "a", "G": "a", "W": "w", "N": "n", "L": "l", "S": "S", "F": "f", "D": "D", "P": "t"}  # P in Tuesday printed lower-case t
# context-dependent classes, values chosen per word (the point under test)
CTX = {"Q": {"UoQ": "y", "etiuQ": "q"}, "Z": {"tiZ": "b", "epoZ": "h", "eZ": "b"}}
lines = []
for v in VIS:
    words = []
    for w in v.split(" / ")[::-1]:            # right-to-left word order
        g = w.split()
        key = "".join(g)
        out = ""
        for s in g[::-1]:                     # right-to-left letter order
            if s in CTX:
                out += CTX[s][key] if key in CTX[s] else "?"
            else:
                out += FIX.get(s, s)
        words.append(out)
    lines.append(" ".join(words))
for i, l in enumerate(lines, 1):
    print(f"L{i}: {l}")
