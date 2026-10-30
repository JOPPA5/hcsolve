#!/usr/bin/env python3
"""hcp-1336: check source hashes, print the sign transcription and the
PROVISIONAL word expansion. The expansion is a conjecture table, not a key:
an initial-letter abbreviation cannot be inverted uniquely."""
import hashlib, pathlib, sys
d = pathlib.Path(__file__).resolve().parent.parent
H = {'source/picture-large.jpg': 'b9e14f793469a1972bfd621bc229cab77f13ebac3d93a1283c4196b89ccc4e72',
     'work/hires/pc_hcp_17_pic.JPG': '2101395b0e1c6af550e917446020427da9c254b102bcedab041fa0a25ecfe028',
     'source/address-large.jpg': '60fc11876aaa8637dd6e69fa7a718fea19cbe236695e5bbfe5d30cb791c10d3e',
     'work/hires/pc_hcp_17_adr.JPG': '25aac0a7f5406355e2f41fe735ebb8cfe504bff077880740a57ed5e74b28b504'}
for f, h in H.items():
    if hashlib.sha256((d / f).read_bytes()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + f)
print('hashes OK')
signs = [s for l in (d / 'work/transcription.txt').read_text().splitlines()
         if not l.startswith('#') for s in l.split()]
# (word, tier)  A = fixed by sister-card formula, B = sense plausible, C = guess, - = left as initial
exp = [('My','A'),('Own','B'),('Darling/Dear','B'),('A.','-'),('Arrived','A'),('Home','A'),('Quite','B'),('Safe(ly)','B'),
       ('Dear/Darling','B'),('Had','B'),('[?]','-'),('Good','C'),('[B/R]','-'),('[A]','-'),('[D: Day?/Dear?]','-'),
       ('Hope','A'),('You','A'),('Are','A'),('Feeling','B'),('Better','B'),('Dear/Darling','B'),
       ('With','A'),('Every/Ever-','B'),('Love','A'),('Take','A'),('A','A'),('Fond','A'),('Kiss','A'),('From','A'),('Your','A'),('Ever','A'),
       ('Affectionate','B'),('And','B'),('Devoted','A'),('C.','-')]
assert len(signs) == len(exp) == 35, (len(signs), len(exp))
for s, (w, t) in zip(signs, exp):
    assert s.split('/')[0].rstrip('?')[0] == w.strip('[')[0] or t == '-', (s, w)
print('signs:', ' '.join(signs))
print('expansion:', ' '.join(w for w, _ in exp))
print('tiers:', ''.join(t for _, t in exp))
