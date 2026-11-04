"""hcp-1194 decoder: python3 -I ciphers/hcp-1194/work/decode.py (run from repo root)."""
import hashlib, json, os, sys
d = os.path.dirname(os.path.abspath(__file__))
base = os.path.dirname(d)
H = {"source/picture-large.jpg": "9a79aefbe5b421cab6b01db9e1c53416c447e5f4751e619b1e2ce86228b19f46",
     "source/address-large.jpg": "0769e827e37dcd53c144160b022b47b0775035bcaa3e5605570199df10e052cd",
     "work/hires/cpc_1900-06-17_AT_Tepi_AT_Wien_schoenfelder-02_pic.jpg": "e93d74ad12c70678bc166e0ab67988b16406bbe9eecd2ea9c2a2980c4101df61"}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(base, p), "rb").read()).hexdigest()
    print(("OK  " if got == h else "BAD ") + p)
    if got != h: sys.exit(1)
key = json.load(open(os.path.join(d, "key.json")))
for line in open(os.path.join(d, "transcription.txt")):
    line = line.strip()
    if not line or line.startswith("#"): continue
    out = []
    for t in line.split():
        out.append({"|": " ", ".": ". "}.get(t) or key[t])
    print("".join(out).replace("  ", " ").strip())
