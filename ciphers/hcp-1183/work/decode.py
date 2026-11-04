"""Decode hcp-1183. Run from repo root: python3 -I ciphers/hcp-1183/work/decode.py"""
import hashlib, json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
    "source/picture-large.jpg": "06800783d34363721d30eeffb80b547ac9a5433309284e5e9ee04bbbaaeeef8b",
    "source/address-large.jpg": "2094e85c7ad4553edd0574086bb4160ce2e28e1f7379eb96c01ea21a41a95391",
    "work/hires/cpc_-06-25_USA_Santa-Clara,-California_USA_San-Jose,-California__pic.jpg":
        "6f0f16e1eb6dbb718bf01912e356b7d64d0f79f16b4b5f7af63b5af0ede1685a",
}
ok = True
for rel, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, rel), "rb").read()).hexdigest()
    print(("OK  " if got == h else "BAD ") + rel)
    ok &= got == h
key = json.load(open(os.path.join(D, "key.json")))
for line in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    words = []
    for w in line.split(" / "):
        out = ""
        for t in w.split():
            if t not in key:
                sys.exit("unknown sign " + t)
            out += key[t]
        words.append(out)
    print(" ".join(words).replace(" .", ".").replace(" ,", ","))
sys.exit(0 if ok else 1)
