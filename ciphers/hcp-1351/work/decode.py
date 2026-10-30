#!/usr/bin/env python3
"""hcp-1351: verify source hashes, decode the frozen transcription with Caesar -1."""
import hashlib, json, os, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {"source/picture-large.jpg": "0adc677cba577e33f5735d5427bb8cf45c25556b1c8e92fc0e3ac41d5c24c336",
     "source/address-large.jpg": "10b150e9cb5aea5c5dababae89e920eb00f34d15c8c6e954563b76e863d7ba27",
     "work/hires/pc_hcp_32_pic.JPG": "28d9226ea307a545333fd4da8e7915aae691d59bb2e983395181c678a9e534ec",
     "work/hires/pc_hcp_32_adr.JPG": "b9296be205be0121b93473cc41f1facf2720273ebdab4762559258b59b0005f2"}
for f, h in H.items():
    if hashlib.sha256(open(os.path.join(R, f), "rb").read()).hexdigest() != h:
        sys.exit("HASH MISMATCH " + f)
print("source hashes OK")
def sh(s, k):
    return "".join(chr((ord(c.lower()) - 97 + k) % 26 + 65) if c.isalpha() else c for c in s)
T = json.load(open(os.path.join(R, "work/transcription.json")))
print(T["plain_heading"], "(plain)")
n = 0
for line in T["lines"]:
    p = [sh(w, -1) for w in line]
    for w, q in zip(line, p):
        assert sh(q, 1).lower() == w.lower(), w
        n += sum(c.isalpha() for c in w)
    print(" ".join(line).ljust(32), "->", " ".join(p))
print(n, "cipher letters, all decoded with one key (Caesar -1)")
