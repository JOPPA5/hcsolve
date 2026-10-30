#!/usr/bin/env python3
"""Manual pixel-location audit; enumerate, rather than guess, row-3 dot cuts."""
from pathlib import Path
import hashlib
import json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
# Fresh manual inspection of picture-large.jpg, row centred at y=605.
# After the earlier -. . .-.. -.-. prefix there are six dot-like marks.
# These are approximate centres, NOT machine-detected measurements.
dot_centres = [411, 427, 441, 455, 473, 492]
print('Manual row-3 tail dot-like centres:', dot_centres)
print('Successive approximate centre gaps:', [b-a for a,b in zip(dot_centres,dot_centres[1:])])
print('Thin crossing strokes near x458 and x483 are not interpreted as dashes.')
print('Next broad horizontal mark is around x535; final question-like mark around x573.')
print('Six consecutive dots have no standard A-Z Morse value.')
# All partitions into E/I/S/H using only the six dot-like marks.
# This does not assert any cuts are physically correct, or any dots survive cancellation.
key = {1:'E', 2:'I', 3:'S', 4:'H'}
def partitions(n):
    if n == 0:
        yield []
    for k in range(1, min(4,n)+1):
        for rest in partitions(n-k):
            yield [k]+rest
candidates = [(' '.join('.'*k for k in ks), ''.join(key[k] for k in ks)) for ks in partitions(6)]
print('Possible dot-run segmentations with no deletion:', len(candidates))
for tokens, letters in candidates:
    print(tokens, '=>', letters)
assert len(candidates) > 1
assert ('.... ..', 'HI') in candidates
print('HI is merely one cut among these alternatives; HIT is not established.')
print('No new frozen plaintext positions. Original source hashes passed.')
