#!/usr/bin/env python3
"""HCP 1378: verify source hashes, decode every enciphered token (Caesar: subtract 1), round-trip check."""
import hashlib, json, pathlib, datetime
D = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
 "source/picture-large.jpg": "d6886480f9f5daf398a389fe6476722c925d38a2863b09e1e4d85e617d5ffd3a",
 "source/address-large.jpg": "621bc56848b1bde1e340317f01761a0d1c6307320fd46f0e5da1e8e7278f0e13",
 "work/hires/pc_hcp_59_pic.JPG": "f3711fd105c9cee719b6e85d8733b28a0afbce319644a4d8f09652467a2412db",
 "work/hires/pc_hcp_59_adr.JPG": "1605ba528aa1039d9c47058985d936b6d4fc07a0fb69886447062dc589c1e829",
}
for p, h in HASHES.items():
    got = hashlib.sha256((D / p).read_bytes()).hexdigest()
    assert got == h, p
print("source hashes OK:", len(HASHES))
def shift(s, k):
    return "".join(chr((ord(c.upper()) - 65 + k) % 26 + 65) if c.isalpha() else c for c in s)
n = kept = 0
out = []
for line in json.loads((D / "work/transcription.json").read_text())["lines"]:
    if line["mode"] == "plain":
        out.append("[plain] " + line["text"])
        continue
    words = []
    for t in line["tokens"]:
        if t.startswith("="):
            words.append("[" + t[1:] + "]"); kept += 1
        else:
            p = shift(t, -1)
            assert shift(p, 1) == t.upper()
            words.append(p); n += sum(c.isalpha() for c in t)
    out.append(" ".join(words))
print("\n".join(out))
print(f"enciphered letters decoded: {n}; literal abbreviation letters: {kept}")
assert datetime.date(1907, 11, 14).strftime("%A") == "Thursday"
print("14 Nov 1907 is a Thursday: OK")
