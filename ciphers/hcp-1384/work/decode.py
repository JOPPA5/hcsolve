#!/usr/bin/env python3
"""HCP 1384: check source hashes, apply Caesar -1 to the manual transcription."""
import hashlib, json, string
from pathlib import Path
d = Path(__file__).resolve().parents[1]
H = {
 "source/picture-large.jpg": "8d754b081a1234a942cbc14521ce83a23e296d927e1f3450adaba1d6d975f789",
 "source/address-large.jpg": "1c5e008de0c6bf71f4fa3030fbf5ea86f50ede7801f84335ceb250aa1d54ef56",
 "work/hires/pc_hcp_65_pic.JPG": "6279b91d3e1f9f225c8e0d1d8687d729303afc897372b4266dc1d463e5eaabbd",
 "work/hires/pc_hcp_65_adr.JPG": "ddf70b782e8f5264cc8a3b57d293205b1daca1799ed93603e6421ae153f59d02",
}
for f, h in H.items():
    assert hashlib.sha256((d / f).read_bytes()).hexdigest() == h, f
print("source hashes OK")
U = string.ascii_uppercase
key = str.maketrans(U + U.lower(), U[-1] + U[:-1] + U[-1].lower() + U[:-1].lower())
t = json.loads((d / "work/transcription.json").read_text())
print("[plain heading]", t["heading_plain"])
n = 0
for row in t["rows"]:
    out = []
    for kind, s in row:
        if kind == "c":
            n += sum(c.isalpha() for c in s)
            out.append(s.translate(key).upper())
        else:
            out.append(f"[{s}]")
    print(" ".join(p[1] for p in row), "->", " ".join(out))
print(n, "cipher letters decoded; abbreviation groups kept literal")
