#!/usr/bin/env python3
"""Reviewer's independent Caesar decoder: plaintext = cipher letter + shift (default 1)."""
import sys
shift = int(sys.argv[2]) if len(sys.argv) > 2 else 1
t = open(sys.argv[1], encoding='utf-8').read()
t = ''.join(l for l in t.splitlines(True) if not l.startswith('#'))
print(''.join(chr((ord(c) - 65 + shift) % 26 + 65) if 'A' <= c <= 'Z' else c for c in t), end='')
print(sum(c.isupper() for c in t), 'letters')
