#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 1437 (reads my own as-seen reading)."""
import sys, collections
digits = {'1':'A','2':'E','3':'I','4':'O','5':'U','6':'T','7':'N','8':'S','9':'R'}
raw = open(sys.argv[1]).read()
print(''.join(digits.get(c, c.upper()) for c in raw), end='')
d = [c for c in raw if c.isdigit()]; l = [c for c in raw if c.isalpha()]
print(f'\n{len(d)+len(l)} letter positions: {len(d)} digits, {len(l)} Latin letters')
print('digit counts', dict(sorted(collections.Counter(d).items())))
print('Latin letters used', ''.join(sorted(set(c.lower() for c in l))))
