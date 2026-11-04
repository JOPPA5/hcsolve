#!/usr/bin/env python3
"""Independent reviewer decode of hcp-1094 (place-value number alphabet).
Transcription read by the reviewer from rotated 2x crops of the hires address scan
(review/work/col1..3.jpg); '200:' marks the diaeresis written above 200."""
import string
alpha = [c for c in string.ascii_lowercase if c != 'j']  # i/j merged
val = {}
for idx, c in enumerate(alpha):
    tier, pos = divmod(idx, 9)
    val[(pos + 1) * 10 ** tier] = c
groups = ["400.200:.40.90.3.8.100", "4.9.80", "4.5.9.40", "9.50.8.1.40.40"]
out = []
for g in groups:
    w = ''
    for t in g.split('.'):
        uml = t.endswith(':')
        n = int(t.rstrip(':'))
        ch = val[n]
        w += {'u': 'ü', 'a': 'ä', 'o': 'ö'}[ch] if uml else ch
    out.append(w)
print(' '.join(out))
used = sorted({int(t.rstrip(':')) for g in groups for t in g.split('.')})
print('values used:', used, 'all in key:', all(u in val for u in used))
