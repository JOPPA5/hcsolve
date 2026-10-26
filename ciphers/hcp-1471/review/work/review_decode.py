#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 1471: every letter is written as the
letter BEFORE it in the alphabet (plaintext = cipher + 1); 'a^' (a with a caret
written beneath) stands for plaintext A.  Reading from body-rot.png, w12.png,
w3a.png, w3b.png in this dir (image rotated 52 deg clockwise)."""
MINE = 'a^qd vd cnvmgda^qsdc?'
out, i = [], 0
while i < len(MINE):
    ch = MINE[i]
    if MINE[i:i+2] == 'a^': out.append('A'); i += 2; continue
    out.append(chr((ord(ch)-ord('a')+1) % 26 + ord('A')) if ch.isalpha() else ch); i += 1
print(''.join(out))
print('letters:', sum(c.isalpha() for c in MINE.replace('a^','A')))
# what a pure Caesar wrap would give for a plain 'a', and the alternatives the solver lists
for alt in ['aqd vd cnvmgdaqsdc?', 'a^qd vd cnwmgda^qsdc?', 'a^qd vd cnvmgda^qsde?', 'a^qd vd envmgda^qsde?']:
    s = alt.replace('a^','@')
    print(f'{alt:24s} ->', ''.join('A' if c=='@' else chr((ord(c)-97+1)%26+65) if c.isalpha() else c for c in s))
