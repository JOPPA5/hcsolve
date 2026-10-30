"""Decode hcp-1458 (tall/short stroke Morse). Run from repo root:
   python3 -I ciphers/hcp-1458/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
HASHES = {"source/address-large.jpg": "a27a6dc56c11dac77e05c70ac977df6ae53127b34274da1a4231b89756b0c5a3",
          "source/picture-large.jpg": "84e8298356a2918795f33dc5a43c18a9e669a9909e5d6be1fa7a64eb6c40acbb"}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    if got != h: sys.exit(f"hash mismatch {p}")
print("source hashes OK")
M = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J",
     "-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T",
     "..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z","--..--":","}
for line in open(os.path.join(D, "transcription.txt")):
    line = line.strip()
    if not line or line.startswith("#"): continue
    tag, body = line.split(":", 1)
    out = []
    for tok in body.split():
        if tok == "/": out.append(" ")
        elif tok == "[BLOT]": continue   # ink blot; no stroke visible, nothing decoded
        else: out.append(M[tok])
    print(f"{tag:3}", "".join(out).strip())
