#!/usr/bin/env python3
"""hcp-1367: Caesar -1 decoder. Run from the repo root: python3 -I ciphers/hcp-1367/work/decode.py"""
import hashlib, json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
want = {
 "source/picture-large.jpg": "37b8dcec3d43c60616edb5849f68a64bd052f24c3f2e645ce95ad9c4540fe20a",
 "source/address-large.jpg": "00e02aae3bcbe3256185fa342bf0cffb6f25bf6662739fc830f127bd95146ee0",
 "work/hires/pc_hcp_48_pic.JPG": "80a47adeeae0c0ecbab8a9160aa30faaab5fe006950c722d687fd24ef25b35b1",
 "work/hires/pc_hcp_48_adr.JPG": "494649aa8cbab3f323f82e139816577051a6a26ccd2aa66cf1408b625aa0ec54",
}
for name, h in want.items():
    got = hashlib.sha256((root / name).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f"HASH MISMATCH {name}")
print("source hashes OK:", len(want))

def dec(ch):
    return chr((ord(ch.upper()) - 65 - 1) % 26 + 65)
def enc(ch):
    return chr((ord(ch) - 65 + 1) % 26 + 65)

t = json.loads((root / "work/transcription.json").read_text())
print("[plain heading]", t["plain_heading"])
n = 0
literal = []
for line in t["lines"]:
    out = []
    for tok in line:
        if tok[0] in "[{":          # abbreviation or plain date: kept as written
            out.append(tok)
            continue
        p = "".join(dec(c) for c in tok)
        assert "".join(enc(c) for c in p) == tok.upper()   # round trip
        n += len(tok)
        out.append(p)
    print(" ".join(line).ljust(34), "->", " ".join(out))
    literal += out
lit = " ".join(literal)
print("\nLITERAL :", lit)
for a, b in t["intended"].items():
    lit = lit.replace(a, b)
print("INTENDED:", lit)
print("enciphered letters:", n)
