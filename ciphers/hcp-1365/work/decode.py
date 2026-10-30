#!/usr/bin/env python3
"""hcp-1365: Caesar -1 decoder. Run from repo root: python3 -I ciphers/hcp-1365/work/decode.py
{..} = abbreviation kept literal (not shifted); & is literal."""
import hashlib, json, os, datetime
D = os.path.join("ciphers", "hcp-1365")
H = {"source/picture-large.jpg":"d61da03f5248be7389ed3a7f001a943f081902def02f139898d131001362cce4",
     "source/address-large.jpg":"c4c5d665cc68b774343bd6ad08e2cfe286aeaf75374b79dfb1153c467178412e",
     "work/hires/pc_hcp_46_pic.JPG":"3e550d8b831f337c2e6bc8588928dc0aa8ff9fd634d1156c5d3333e660ff45da",
     "work/hires/pc_hcp_46_adr.JPG":"eedc99d7ccffb0cd70b933bfd8aa641d83a502c732223d4c4e8834f7895a700f"}
for p, h in H.items():
    assert hashlib.sha256(open(os.path.join(D, p), "rb").read()).hexdigest() == h, p
print("source hashes OK:", len(H))
def shift(s, k):
    o = ""
    for c in s:
        if c.isalpha():
            b = 65 if c.isupper() else 97
            o += chr((ord(c) - b + k) % 26 + b)
        else:
            o += c
    return o
T = json.load(open(os.path.join(D, "work/transcription.json")))
print(T["heading_plain"], "[plain]")
n = 0
for line in T["lines"]:
    out = []
    for t in line:
        if t.startswith("{"):
            out.append("[" + t.strip("{}") + "]")
        else:
            p = shift(t, -1).upper()
            assert shift(p.lower(), 1).lower() == t.lower()
            n += sum(c.isalpha() for c in t)
            out.append(p)
    print(f"{' '.join(line):32} {' '.join(out)}")
print("enciphered letters decoded:", n)
print("22 Jul 1907 is a", datetime.date(1907, 7, 22).strftime("%A"))
