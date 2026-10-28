#!/usr/bin/env python3
"""Decode a manual scan transcription, verify immutable scans; this is not OCR."""
import hashlib
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
HASHES = {
    'picture.jpg': 'e273cd4c77a91914cff08543f23ec199965de6086a294aeb664f707332aa0d70',
    'address.jpg': '1b702e33c8a54ec6665b1d5d2c6a131a0100013aa6ad0198103792ee1d60fdc1',
}
# Names identify the lines actually drawn, not the opening's direction.
KEY = {'SE':'A','S':'B','SW':'C','E':'D','O':'E','W':'F','NE':'G','N':'H','NW':'I',
       'SE.':'K','S.':'L','SW.':'M','E.':'N','O.':'O','W.':'P','NE.':'Q','N.':'R','NW.':'S',
       'I':'T','check':'U','up':'W','up.':'Z','SE~':'Ä','check~':'Ü'}
# Pipe separates word groups. Interior dot '.', umlaut '~'. Coordinates are approximate
# glyph centers in original 1024x678 picture.jpg; inspect pixels, not just readings.
ROWS = [
 ('embedded initials', 588, [130,173,194,233,260], 'SW. | SE. S. | NW. | SW.'),
 ('main 1', 598, [417,439,460,490,513,538,558,584,609,630,653,675,698,722,744,768,792,813,836,854,876,913,935,955,976],
  'up NW O | NE O W SE~ S. S. I | E NW N. | E NW O | SE. SE N. I O | NW. NW E. E'),
 ('main 2', 633, [40,60,84,126,151,174,193,219,243,276,296,315,337,354,382,411,455,478,499,521,543,564,588,609,655,682,707,728,750,788,814,861,884,907,929,950],
  'E NW O | S O NW E O E. | E. NW SW N I | up. check | S O E. O NW E O E. | N O N. up. S. | NE N. | SE. check~ NW. NW. O')
]
records = []
outputs = []
for name,y,xs,text in ROWS:
    out = []
    n = 0
    for token in text.split():
        if token == '|':
            out.append(' ')
            continue
        reading = KEY[token]
        out.append(reading)
        x = xs[n]
        records.append({'id':f'{name}.{n+1:02}', 'xy':[x,y],
                        'box':[x-11,y-19,x+11,y+19], 'shape':token, 'reading':reading})
        n += 1
    assert n == len(xs), (name,n,len(xs))
    outputs.append(''.join(out))
    print(name+': '+outputs[-1])
assert outputs == ['M KL S M', 'WIE GEFÄLLT DIR DIE KARTE SIND',
                   'DIE BEIDEN NICHT ZU BENEIDEN HERZL GR KÜSSE']
assert len(records) == 66
print('Encrypted glyphs:',len(records),'(5 embedded initials + 25 main first line + 36 main second line).')
print('Editorial punctuation: M. KL. S. M.; WIE GEFÄLLT DIR DIE KARTE, SIND')
print('DIE BEIDEN NICHT ZU BENEIDEN? HERZL - GR - u. KÜSSE.')
print('The u. is ordinary cursive between GR and KÜSSE, not an encrypted glyph.')
print('Uncertain ordinary cursive margin, prose abbreviation and final monogram are outside this glyph inventory.')
for name,expected in HASHES.items():
    actual = hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest()
    assert actual == expected, (name,actual)
    print('SHA256 verified',name,actual)
print('Observed shape assignments:', ' '.join(f'{s}={KEY[s]}' for s in sorted({r['shape'] for r in records})))
if '--write-transcript' in sys.argv:
    (HERE/'transcript.json').write_text(json.dumps({
        'source':'picture.jpg', 'dimensions':[1024,678],
        'coordinates':'Pixel x/y from upper left, approximate manual centers and bounding boxes; not image recognition.',
        'records':records},indent=2,ensure_ascii=False)+'\n')
