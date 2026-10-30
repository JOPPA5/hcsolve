"""Reviewer's independent decoder for hcp-1485. Key is generated from the stated construction
rule (not read from work/key.json): consonants BCDFGHJKLMNPQRSTVW in order, index = side*6 + pos*3 + (count-1),
side L=0 R=1 X=2, pos t=0 b=1. Vowel shapes fixed. Usage: python3 -I indep_decode.py <transcription>"""
import re, sys, collections
CONS = "BCDFGHJKLMNPQRSTVW"
SHAPES = {"CIR": "A", "TRI": "E", "TRII": "I", "SQ": "O", "SQB": "U", "SQF": "Y"}
def sign(tok):
    if tok in SHAPES: return SHAPES[tok]
    m = re.fullmatch(r"([LRX])([123])([tb])", tok)
    if not m: raise ValueError(tok)
    return CONS["LRX".index(m[1]) * 6 + "tb".index(m[3]) * 3 + int(m[2]) - 1]
used = collections.Counter(); out = []
for line in open(sys.argv[1], encoding="utf-8"):
    if line.startswith("#") or not line.strip(): continue
    s = ""
    for tok in line.split():
        if tok == "/": s += " "; continue
        if tok.startswith("[["): s += tok[2:-2]; continue
        base, n = (tok[:-2], 2) if tok.endswith("^2") else (tok, 1)
        used[base] += n; s += sign(base) * n
    out.append(s)
print("\n".join(out))
print("glyph types:", len(used), "letters:", sum(used.values()))
print(sorted(used.items()))
