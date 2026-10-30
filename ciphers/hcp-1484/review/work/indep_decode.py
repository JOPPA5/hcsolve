"""Reviewer's independent decoder: derives letters from the structural rule
(side x anchor x bar-count -> consecutive alphabet), not from work/key.json."""
import sys, re
ALPH = "BCDFGHJKLMNPQRSTVWXZ"  # consonants in order
ORDER = ["Lt", "Lb", "Rt", "Rb", "Bt", "Bb"]
VOW = {"CIRC": "A", "TRI": "E", "TRIS": "I", "BOX": "O", "BOXU": "U", "BOXY": "Y"}
def letter(t):
    if t in VOW: return VOW[t]
    m = re.fullmatch(r"([LRB][tb])([123])", t)
    if not m: raise SystemExit("bad sign " + t)
    return ALPH[ORDER.index(m.group(1)) * 3 + int(m.group(2)) - 1]
txt = open(sys.argv[1]).read()
out, n = [], 0
for tok in txt.split():
    if tok.startswith("#"): continue
    pass
lines = [l for l in txt.splitlines() if l.strip() and not l.startswith("#")]
s = ""
for l in lines:
    for tok in l.split():
        if tok == "/": s += " "; continue
        if tok in ",.?\"-": s += tok; continue
        faint = tok.startswith("[faint]"); tok = tok.replace("[faint]", "")
        d = tok.endswith("^2"); tok = tok.replace("^2", "")
        c = letter(tok); n += 1
        s += ("[%s]" % c.lower()) if faint else c * (2 if d else 1)
print(s); print(n, "signs")
