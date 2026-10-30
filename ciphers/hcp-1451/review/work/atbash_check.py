#!/usr/bin/env python3
"""Independent Atbash check for HCP 1451 (reviewer). Diplomatic transcription by reviewer
from 5-9x crops; J/j glyphs are what the pixels show, interpreted as Z/z."""
import sys
diplomatic = ["Gifv", "Jmw", "Jodjbh", "Olermt"]
def atbash(s):
    out = []
    for ch in s:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            out.append(chr(base + 25 - (ord(ch) - base)))
        else:
            out.append(ch)
    return ''.join(out)
print("literal (J as J):", ' '.join(atbash(w) for w in diplomatic))
norm = [w.replace('J', 'Z').replace('j', 'z') for w in diplomatic]
print("J->Z interpreted:", ' '.join(atbash(w) for w in norm))
# 25-letter (I/J merged) Atbash alternative test
alpha25 = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
m25 = {a: b for a, b in zip(alpha25, alpha25[::-1])}
print("25-letter Atbash:", ' '.join(''.join(m25.get(c.upper().replace('J','I'), '?') for c in w) for w in diplomatic))
for k in range(1, 26):  # Caesar sanity: no shift gives English
    pass
