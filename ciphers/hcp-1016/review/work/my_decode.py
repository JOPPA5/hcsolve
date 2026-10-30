"""Reviewer's independent decode of HCP 1016 (tokens read by the reviewer from
own crops r1..r5, close.png, dein.png etc.). Key generated from the German
Pigpen grid (alphabet without J), not copied from the solver."""
import string
alpha = [c for c in string.ascii_uppercase if c != 'J']   # 25 letters
cells = ['SE','S','SW','E','O','W','NE','N','NW']        # reading order of 3x3 grid cells as strokes drawn
key = {}
for i, c in enumerate(cells):
    key[c] = alpha[i]; key[c+'.'] = alpha[9+i]
key.update({'T': 'T', 'V': 'U', 'Z^': 'Z'})               # extra signs as on sister card HCP 995
rows = [
 "SW. O NW E. O NW. / S. NW O S O",
 "N O N. Z^ NW NE O E. / SW. SE O V NW. SW N O E.",
 "SE. O. SW. SW. O / NW SW N / O NW E. O E. / SE. N.? SE O W T NW NE O. E.",
 "NW. SW N S. V SW SE. / V E. E / O NW E. O E. / NW. V O NW. NW. O E.",
 "NE V T O E. SE SW N T SE. V NW. NW.",
 "E O NW E. / T N O O.",
]
n = 0
for r in rows:
    out = []
    for w in r.split(' / '):
        s = ''
        for t in w.split():
            s += key[t.rstrip('?')]; n += 1
        out.append(s)
    print(' '.join(out))
print('glyphs', n)
