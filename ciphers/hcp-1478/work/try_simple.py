#!/usr/bin/env python3
"""Bounded attempts over a disclosed uncertain manual transcription."""
from pathlib import Path
import string
p = Path(__file__).resolve().parent
raw = (p/'provisional.txt').read_text()
abc = string.ascii_lowercase
def show(label, key):
    print(label)
    print(''.join(key.get(c,c) for c in raw))
for n in range(26):
    show(f'Caesar {n}', dict(zip(abc, abc[n:]+abc[:n])))
show('Atbash', dict(zip(abc,abc[::-1])))
keyboard = 'qwertyuiopasdfghjklzxcvbnm'
show('QWERTY to alphabet', dict(zip(keyboard,abc)))
show('Alphabet to QWERTY', dict(zip(abc,keyboard)))
for n in [-1,1]:
    key = {row[i]:row[(i+n)%len(row)]
           for row in ['qwertyuiop','asdfghjkl','zxcvbnm']
           for i in range(len(row))}
    show(f'Adjacent keyboard {n} (row wrap)', key)
