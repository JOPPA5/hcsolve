#!/usr/bin/env python3
"""Reviewer's independent A1Z26 decoder for HCP 1463.
Transcription below is the reviewer's own sign-by-sign reading of
source/address-large.jpg (crops r01-03.png ... r13-14.png, z-*.png in this dir).
'T' marks the plaintext time group "7.30 & 8" which is not enciphered."""
import sys, pathlib
MINE = """13 25 - 4 5 1 18 - 1 4 1
20 8 1 14 11 19 - 6 15 18 - 12 5 20 20 5 18
20 8 9 19 - 13 15 18 14 9 14 7
23 9 12 12 - 3 15 13 5 - 1 14 5
19 5 5 - 25 15 21 - 20 15 13 15 18 18 15 23
14 9 7 8 20 - 4 5 1 18 - 23 9 12 12
3 15 13 5 - 2 5 20 23 5 5 14
T - 7 15 15 4 14 9 7 8 20
4 5 1 18 5 19 20 - 9 20 - 23 9 12 12
19 15 15 14 - 2 5 - 8 5 18 5
23 9 20 8 - 13 21 3 8 - 12 15 22 5
6 18 15 13 - 25 15 21 18 - 15 23 14
11 11 11 11 11 11 - 23 1 12 20"""
def dec(tokens):
    out=[]
    for t in tokens:
        if t in ('-','/'): out.append(' ')
        elif t.startswith('T') or t.startswith('{TIME'): out.append('7.30&8')
        else:
            n=int(t); assert 1<=n<=26, t; out.append('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[n-1])
    return ''.join(out)
mine=[l.split() for l in MINE.splitlines()]
print('\n'.join(dec(l) for l in mine))
nums=[t for l in mine for t in l if t.isdigit()]
print('letter positions:', len(nums), ' distinct values:', sorted(set(map(int,nums))))
if len(sys.argv)>1:
    sol=[l.split() for l in pathlib.Path(sys.argv[1]).read_text().splitlines()]
    a=[t for l in mine for t in l if t.isdigit()]
    b=[t for l in sol for t in l if t.isdigit()]
    print('solver letter positions:', len(b), ' identical sequence:', a==b)
