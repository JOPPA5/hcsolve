#!/usr/bin/env python3
"""Reviewer's independent check: own sign-by-sign transcription, every Caesar shift, diff with solver file."""
import json, sys
from pathlib import Path
base = Path(sys.argv[1])
MINE = ["Nz Pxo Efbsftu Cpz", "uijt jt Tpnfuijoh ofx", "boe pof pg oz", "gpwpvsjuf Iznot", "Mpwf Gspn Zpvst", "Hjsm"]
def shift(s, k):
    o = []
    for c in s:
        if c.isalpha():
            a = 65 if c.isupper() else 97
            o.append(chr((ord(c) - a - k) % 26 + 65))
        else:
            o.append(c)
    return ''.join(o)
WORDS = set("MY OWN DEAREST BOY THIS IS SOMETHING NEW AND ONE OF LOVE FROM YOURS GIRL HYMNS".split()) | set("THE TO A I IN IT YOU HE SHE WE ME AT ON NO SO BE AS AN".split())
text = ' '.join(MINE)
best = []
for k in range(26):
    p = shift(text, k).split()
    best.append((sum(len(w) for w in p if w in WORDS), k))
best.sort(reverse=True)
print('best shifts (letters in recognised words, shift):', best[:4])
for r in MINE:
    print(f'{r:24}{shift(r, 1)}')
print('letters:', sum(c.isalpha() for c in text))
sol = json.loads((base / 'work/transcription.json').read_text())['rows']
norm = lambda r: r.replace('.', '')
print('identical to solver rows:', [norm(x) for x in sol] == MINE)
