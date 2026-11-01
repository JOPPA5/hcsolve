#!/usr/bin/env python3
"""Run from the repo root: python3 -I ciphers/hcp-1179/work/decode.py
Raw decode, one word per line. [x] = taken by sense, not from the pixels; t? = dotted 8 read as 8,.
Spelling stands as on the card (legszeb, one b)."""
import hashlib, json, pathlib, sys
d = pathlib.Path("ciphers/hcp-1179")
H = {"source/picture-large.jpg": "e0ecf18320b8e59868b889d7b2d0507bf4e4a12fb9b6fcfe1deb9d06c98bd103",
     "source/address-large.jpg": "0b2c595c95c49998211030a308beb9f4c73412dbdf1223764e24a0c2f1a64fa4",
     "work/hires/cpc_1915-09-26_HU_Mezokovesd_HU_Szomolya_szomolya-01_pic.jpg": "f43c8971cfa778c977ece66cb6fe33225605478ddc89083be2d64cfef5e5fcfa",
     "work/hires/cpc_1915-09-26_HU_Mezokovesd_HU_Szomolya_szomolya-01_adr.jpg": "920375c1dbfe28995ae791b8ac9fae89e5664c8950a7f0dec7e59c12ad191808"}
for f, h in H.items():
    if hashlib.sha256((d / f).read_bytes()).hexdigest() != h:
        sys.exit("HASH MISMATCH " + f)
print("hashes ok")
key = json.loads((d / "work/key.json").read_text(encoding="utf-8"))
words = []
for line in (d / "work/transcription.txt").read_text(encoding="utf-8").splitlines():
    if line.startswith("#"):
        continue
    out = "".join("[" + key[t[1:-1]] + "]" if t.startswith("[") else key[t] for t in line.split())
    print(f"{line:45} {out}")
    words.append(out)
print("Plaintext:", " ".join(words))
