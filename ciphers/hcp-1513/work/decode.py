"""Decode hcp-1513. Run from repo root:
python3 -I ciphers/hcp-1513/work/decode.py"""
import hashlib, json, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
H = {"source/address-large.jpg": "0efe27aaf4b2b3073f0d8dc3172be89b2a65c4e7d5754abde6bf5a3b8bda34a6",
     "source/picture-large.jpg": "0cb95fe0b5bc7d5a34ccd36d9c43d651fecf05c1a32e818cf13f287c8887f70e",
     "source/metadata.md": "a82ea0b640852ae6d0a34e9ec6eeb41a75f72f85474b101f39adccffc261e1a3"}
for f, h in H.items():
    got = hashlib.sha256(open(os.path.join(D, f), "rb").read()).hexdigest()
    if got != h:
        sys.exit("hash mismatch: " + f)
print("source hashes OK")
key = json.load(open(os.path.join(D, "work/key.json")))
out = []
for line in open(os.path.join(D, "work/transcription.txt"), encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        if line.startswith("# Margin"): out.append("--- margin ---")
        continue
    words = []
    for tok in line.split():
        if tok in {",", ".", ":-"}:
            words.append(tok); continue
        if tok.startswith("#"):
            words.append(tok[1:]); continue
        w = ""
        for s in tok.split("."):
            ins = s.startswith("[")
            c = key[s.strip("[]")]  # KeyError = unknown sign
            w += c.lower() if ins else c
        words.append(w)
    out.append(" ".join(words))
print("\n".join(out))
print("\n(lower-case letter = sign written above the line as an insertion)")
