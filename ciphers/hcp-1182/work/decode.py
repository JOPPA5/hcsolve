"""hcp-1182: decode the Morse transcription; check source hashes. Run from repo root:
python3 -I ciphers/hcp-1182/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
HASHES = {
 "source/address-large.jpg": "26c1cb471b6fb3601fa9d5ad6249b0a03b96fd7cbb31c2d8e429c8e02738c65d",
 "source/picture-large.jpg": "a021682e4dea72293c8774e0505a7100384441891ea6314a7bfd95841fbca672",
 "work/hires/cpc_1909-10-16_DE_Berlin_DE_Lichtenrade__adr.jpg": "1ac51b12f47cbec0e4364c2f3917777311b6b7b1d6ac914276cea3afd8da3232",
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    print(("OK   " if got == h else "BAD  ") + p); 
    if got != h: sys.exit(1)
# Standard International Morse plus German CH and Ü.
STD = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",
 ".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O","--.-":"Q",".-.":"R","...":"S",
 "-":"T","..-":"U","...-":"V","-..-":"X","--..":"Z","----":"CH","..--":"Ü",".-.-":"Ä","---.":"Ö"}
# The writer's own variants (consistent on the card; standard P and Y never occur):
WRITER = {".--.":"W", "-.--":"Z"}
KEY = {**STD, **WRITER}
out = []; vert = []
for line in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    if not line[:1] in ("L", "V"): continue
    toks = line.split(":", 1)[1].split()
    s = ""
    for t in toks:
        if t in ("[u", "u]"): continue
        if t == "|": s += " "; continue
        if t == "=": s += "="; continue
        if t == "-dash-": s += "–"; continue
        n = 1
        if t.endswith("*2"): t, n = t[:-2], 2
        s += KEY[t] * n
    (out if line.startswith("L") else vert).append(s.strip())
print("\nLine by line:")
for i, s in enumerate(out, 1): print(f"{i:2d} {s}")
text = " ".join(out).replace("= ", "").replace("=", "")
print("\nRunning text:\n" + " ".join(text.split()))
print("\nVertical line along the divider (second text):")
for s in vert: print(s)
