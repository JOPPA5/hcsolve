#!/usr/bin/env python3
"""hcp-1331: print the full message; check file hashes and that the hard-coded transcription and expansion agree. Run from the repo root. It does not read the image."""
import hashlib, os, sys
B = 'ciphers/hcp-1331/'
H = {'source/picture-large.jpg': '012ecc1578c291107e3b2ff8ae681e66d3374291f67cc422351a454b09815baf',
     'source/address-large.jpg': 'ca000041f0a6b92e5081118b0982cd247aeb4af1ee71bebaf24bcf0f748ba64a',
     'work/hires/pc_hcp_12_pic.JPG': '1cab08aafd666070da8ebe06662eec8b88876d2ef4db349d404ba907ea88e710',
     'work/hires/pc_hcp_12_adr.JPG': 'd9dad6e432b75abdb310161294e9fd383e271b279e349b72fb65386977377f04'}
for f, h in H.items():
    assert hashlib.sha256(open(B + f, 'rb').read()).hexdigest() == h, f
# Each line is (transcription, expansion); a dot stands for one suppressed letter.
L = [("D..r O.d B.y", "Dear Old Boy"),
     ("Train arrives at Midhurst", None),
     ("9-54. Did M.ss y.u", "9-54. Did miss you"),
     ("l..t n.g.t de...e", "last night dearie"),
     ("I went to the Rehearsal", None),
     ("but we did not have", None),
     ("the Pole last night", None),
     ("rather silly I think", None),
     ("yours with love Ada", None)]
dots = 0
for c, p in L:
    p = p or c
    assert len(c) == len(p), c
    for a, b in zip(c, p):
        if a == '.' and b != '.':
            dots += 1
        else:
            assert a.lower() == b.lower(), (c, p, a, b)
    print(p)
print(f"[hashes OK; {dots} dotted letters restored; transcription and expansion agree (internal check, not against the image)]", file=sys.stderr)
