#!/usr/bin/env python3
"""Reviewer's independent decoder for hcp-1392 (own transcription, all 26 shifts)."""
import sys
lines = ["Nz Pxo. Efbsftu", "Tfoejoh. b. dbse", "up. Z— jotufbe",
         "pg. mfuufs.", "Gspn. zpvs pxo", "Hjsm"]
# reviewer reading of the line-4 tail and the closing group, kept literal:
literal = {"line4_tail": "N & L!  (cf. hcp-1393/1395/1403/1407)", "before_Girl": "N + raised letter, dots below"}
def sh(t, k):
    o = []
    for c in t:
        if c.isupper(): o.append(chr((ord(c)-65-k) % 26 + 65))
        elif c.islower(): o.append(chr((ord(c)-97-k) % 26 + 97))
        else: o.append(c)
    return ''.join(o)
for l in lines: print(f"{l:20s} -> {sh(l,1)}")
print("letters:", sum(c.isalpha() for l in lines for c in l))
print("literal fields:", literal)
print("Solver's 'Ib-Ib' under -1:", sh("Ib-Ib", 1), "; reviewer 'N & L' under -1:", sh("N & L", 1))
joined = ''.join(lines).lower()
for k in range(26):
    if k in (0,1,25): print(k, ''.join(c for c in sh(joined,k) if c.isalpha())[:40])
