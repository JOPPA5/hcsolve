#!/usr/bin/env python3
"""HC Portal 1501: decode the Morse transcription of the address side.
Run from the repo root:  python3 ciphers/hcp-1501/work/decode.py
Standard library only. Verifies source and transcription hashes first."""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
    'source/address-large.jpg': '6b3a77a208b47fbd5c76fccfd9d5859c85b546f4a3995f6177fe53cf2dfc153f',
    'source/picture-large.jpg': '59a66774fef109a8202db33d515197518f39e788c687166e6f6cd37e51fa7bf5',
    'source/metadata.md': '0cdaf0e79108e276923acc885736fc33ee2cd6e2e6dee480e51b7d5486e5c4e3',
    'work/transcription.txt': '46950f2da30211047b646c1780cfdccc449192912b86d03df6421889bd0562c2',
}
for rel, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, rel), 'rb').read()).hexdigest()
    if got != h:
        sys.exit(f'hash mismatch: {rel}')
MORSE = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H',
 '..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q',
 '.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
lines = [l.split(':', 1)[1] for l in open(os.path.join(D, 'transcription.txt')) if l.startswith('L')]
def decode(block):
    text = ''
    for l in block:
        for tok in l.split():
            text += ' ' if tok == '/' else MORSE[tok]   # KeyError = invalid code group
    return ' '.join(text.split())
letter = decode(lines[8:])
ps = decode(lines[:8])
print('Line-by-line (physical order):')
for i, l in enumerate(lines, 1):
    print(f'  L{i:02d}: ' + ''.join(' ' if t == '/' else MORSE[t] for t in l.split()))
print()
print('LETTER (lines 9-33):', letter)
print('P.S.   (lines 1-8, written at the top):', ps)
