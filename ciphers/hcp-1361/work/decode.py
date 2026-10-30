#!/usr/bin/env python3
"""HCP 1361: hash check, Caesar -1 decode of the manual transcription, inverse round trip."""
import hashlib, json, pathlib, datetime
D = pathlib.Path(__file__).resolve().parent.parent
H = {
 "source/picture-large.jpg": "753a5be29c57a1638c7e236a013d7aa7b083b63fb76dfdc7850072e18c34dd81",
 "source/address-large.jpg": "01c73f580fd0b2313b2c251380d046ab761707fbadc9c9e9c48eae2aed4b568c",
 "work/hires/pc_hcp_42_pic.JPG": "aa6e31d352834934c7fb43936c87d85de161aa00f96bcafa8656ac9f8196ad28",
 "work/hires/pc_hcp_42_adr.JPG": "18f2c085d3c147c3b05e52e1be8e191acd9fc22344b38650074b0d78e166ce4f",
}
for p, h in H.items():
    assert hashlib.sha256((D / p).read_bytes()).hexdigest() == h, p
print("hashes OK:", len(H), "files")
def shift(s, k):
    return "".join(chr((ord(c.upper()) - 65 + k) % 26 + 65) if c.isalpha() else c for c in s)
t = json.loads((D / "work/transcription.json").read_text())
assert datetime.date(1907, 7, 6).strftime("%A") == "Saturday"
n = 0
print(t["clear_heading"], "|", t["clear_date"], "(clear; 6 July 1907 was a Saturday)")
for line in t["lines"]:
    out = []
    for kind, tok in line:
        if kind == "c":
            p = shift(tok, -1)
            assert shift(p, 1) == tok.upper()
            n += sum(c.isalpha() for c in tok)
            out.append(p)
        else:
            out.append("[" + tok + "]")
    print(" ".join(tok for _, tok in line), "=>", " ".join(out))
print("enciphered letters decoded:", n)
