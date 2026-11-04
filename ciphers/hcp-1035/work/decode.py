"""hcp-1035 decoder: numeric substitution A=1 ... Z=25 with I/J merged (9).
Usage (from repo root): python3 -I ciphers/hcp-1035/work/decode.py
Checks source hashes, then decodes work/transcription_partial.txt."""
import hashlib, pathlib, re
B = pathlib.Path(__file__).resolve().parent.parent
H = {"source/address-large.jpg":"3867bff31e2e9fa8cf7525c6c8d04e87ce50826316025cd87f009839069092d4",
     "source/picture-large.jpg":"02da54c83da4a85e6133f6d1195ce6c7c1fa314150b0af7bd6c38cdab6d3914b"}
for f,h in H.items():
    d = hashlib.sha256((B/f).read_bytes()).hexdigest()
    print(("OK  " if d==h else "BAD ")+f)
A = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
def letter(t):
    t = t.strip("{}")
    return A[int(t)-1] if t.isdigit() and 1 <= int(t) <= 25 else "?"
def word(g):
    if g.startswith("["): return g
    return "".join(letter(t) for t in re.split(r"\.", g) if t)
for line in (B/"work/transcription_partial.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    print(" ".join(word(g) if g not in "!..." else g for g in line.split()))
