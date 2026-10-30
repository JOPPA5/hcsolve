#!/usr/bin/env python3
"""HCP 1382: verify source hashes, then decode the manual transcription (Caesar -1)."""
import hashlib, datetime, pathlib, sys
D = pathlib.Path(__file__).resolve().parent.parent
H = {"source/picture-large.jpg": "bcb1f80a659fe107a70f74a68699c13af9e9112e6a50f9d1bcd72d0371c340ee",
     "source/address-large.jpg": "160d54d65e49e04a1b2bdfc62a39c3684f3917de33747dcba6052f05e4ea735d",
     "work/hires/pc_hcp_63_pic.JPG": "fcce460f31c61dde90468a66910f58ec464dabf6e749b0fc3339e3fef55594a7",
     "work/hires/pc_hcp_63_adr.JPG": "0f89ce2e4a1804b32e8d11516894877bb89e9c86438c18441d55d2d5e36e12f9"}
for f, h in H.items():
    if hashlib.sha256((D / f).read_bytes()).hexdigest() != h:
        sys.exit("HASH MISMATCH " + f)
print("source hashes OK")
def dec(s):
    return "".join(chr((ord(c) - (65 if c.isupper() else 97) - 1) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in s)
# (kind, text): P plain writing, C enciphered, A abbreviation kept literal
T = [("P", "Tues. Morning G. H."), ("P", "I am enjoying"), ("P", "myself Dear[?]"),
     ("C", "pomz."), ("C", "Xjti"), ("C", "zpv."), ("C", "Xfsf"), ("C", "Ifsf."), ("C", "bt."), ("C", "Xfmm."),
     ("A", "M-L."), ("C", "Gspn"), ("C", "Zpvs"), ("C", "Pxo"), ("A", "E.L."), ("C", "Hjsm"), ("P", "24th Sep 07")]
out = [dec(t) if k == "C" else t for k, t in T]
n = sum(c.isalpha() for k, t in T if k == "C" for c in t)
print(" ".join(out)); print("enciphered letters:", n)
assert datetime.date(1907, 9, 24).strftime("%A") == "Tuesday"
print("1907-09-24 is a Tuesday")
