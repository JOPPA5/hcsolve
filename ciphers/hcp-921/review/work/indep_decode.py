#!/usr/bin/env python3
"""Reviewer's independent decode of HCP 921 from the reviewer's own sign reading
(review/work/cipher_rot90.png, card rotated 90 deg CCW from the scan).
Interleaved Pigpen built from first principles: grid cells in reading order
(TL-cell .. BR-cell) carry pairs A/B .. Q/R; X quadrants top, left, right,
bottom carry S/T, U/V, W/X, Y/Z.  Sign = shape of the cell's borders."""
import string
cells = ['BR','B','BL','R','C','L','TR','T','TL']   # shape of cell 1..9
wedges = ['V','>','<','^']                            # top,left,right,bottom quadrant
key = {}
letters = iter(string.ascii_uppercase)
for s in cells + wedges:
    key[s+'0'] = next(letters); key[s+'1'] = next(letters)
# reviewer's own reading, '#' = blotted sign, '.' = writer's dot (punctuation)
lines = ['TR0 C0 # >1 >1 . TR0 BR0 ^0 .', 'B1 C0 BL0 B1 .']
for alt in ({}, {'>1':'S'}):
    k = dict(key, **alt)
    print(' / '.join(''.join(k.get(t, '?' if t=='#' else t) for t in l.split()) for l in lines), alt)
