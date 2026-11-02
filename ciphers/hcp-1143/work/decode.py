#!/usr/bin/env python3
"""Run from the repo root: python3 -I ciphers/hcp-1143/work/decode.py
Checks the scan hashes, decodes every sign by work/key.json, asserts each decoded word equals the
stated reading (long vowels folded), and prints the plaintext. {sign|x} signs are counted separately."""
import hashlib, json, pathlib, sys
d = pathlib.Path("ciphers/hcp-1143")
n = "work/hires/cpc_1916-05-04_HU_Mezokovesd_HU_Szomolya_szomolya-33_"
H = {"source/picture-large.jpg": "35a00cabaaea07c69ec5bdde7df853bb7934f92533be58cb753146e47a379322",
     "source/address-large.jpg": "be936722c398f12ef4198da9526345e45d7bdf87e0fdabcaaa473c70fddcb527",
     n + "pic.jpg": "afacb5bcca43fd4c470f7790eacf99e6fe4edf6099531b92d7ac83c96f1b249a",
     n + "adr.jpg": "5f9d9ca4996045ea95c36861233a2ce1e044810aa5d9e00b19e99d495e038c59"}
for f, h in H.items():
    if hashlib.sha256((d / f).read_bytes()).hexdigest() != h:
        sys.exit("HASH MISMATCH " + f)
print("hashes ok")
key = json.loads((d / "work/key.json").read_text(encoding="utf-8"))
fold = str.maketrans("óőíúű", "oöiuü")
clean = odd = 0
section = None
out = {}
for line in (d / "work/transcription.txt").read_text(encoding="utf-8").splitlines():
    if line.startswith("## "):
        section = line[3:]; out[section] = []; continue
    if not line.strip() or line.startswith("#"):
        continue
    signs, word = [x.strip() for x in line.split("|", 1)] if "{" not in line else (line.rsplit(" | ", 1))
    raw = ""
    for t in signs.split():
        if t.startswith("{"):
            raw += t[1:-1].split("|")[1]; odd += 1
        else:
            raw += key[t]; clean += 1
    assert raw == word.lower().translate(fold), (raw, word)
    out[section].append(word)
for s, w in out.items():
    print(f"\n[{s}]\n" + " ".join(w))
print(f"\n{clean} signs by the table, {odd} by sense or restoration, {len(set(key))} table signs")
