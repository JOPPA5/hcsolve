#!/usr/bin/env python3
"""Decode a manual visual transcript, check immutable images; this is not OCR."""
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'source'
# Wall labels: t=top, b=bottom, l=left, r=right; . means internal dot.
# For angled glyphs v/down, >/right, </left, ^/up, . is the internal dot.
KEY = {
    'br':'A', 'br.':'B', 'lbr':'C', 'lbr.':'D',
    'bl':'E', 'bl.':'F', 'tbr':'G', 'tbr.':'H',
    'tblr':'I', 'tblr.':'K', 'tbl':'L', 'tbl.':'M',
    'tr':'N', 'tr.':'O', 'tlr':'P', 'tlr.':'Q',
    'tl':'R', 'tl.':'S', 'v':'T', 'v.':'U',
    '>':'V', '>.':'W', '<':'X', '<.':'Y', '^':'Z',
}
# The two extra dots on r4's second v. are an umlaut, not a new alphabet cell.
KEY['v.:umlaut'] = 'Ü'
# Each row: source bounding box, whitespace-delimited groups of literal shapes,
# original punctuation, and expected literal decode. Glyph numbers are 1-based.
ROWS = [
 ('r1', [704,411,980,457],
  'tbl tblr bl br. bl tl | bl tr tbr bl tbl', '!', 'LIEBER ENGEL'),
 ('r2', [703,461,983,505],
  'lbr. tblr tl | ^ v. | tbr bl bl. br tbl tbl bl tr', '', 'DIR ZU GEFALLEN'),
 ('r3', [694,504,935,542],
  'tblr. tr. tbl. tbl. bl | tbr. tr. tl tbr bl tr', '', 'KOMME HORGEN'),
 ('r4', [668,540,1002,584],
  ' ^ v. tl v.:umlaut lbr tblr. | br. tblr tl. | tl. tr. tr tr',
  ['', '.', '', '='], 'ZURÜCK BIS SONN'),
 ('r5', [18,583,982,625],
  'v br tbr | tr br lbr tbr. | lbr. bl tl | tbl. bl tl. tl. bl | '
  '> bl tl br. tbl bl tblr br. bl | v. tr v bl tl | '
  'tbr. bl tl ^ tbl tblr lbr tbr. bl tbl.', '',
  'TAG NACH DER MESSE VERBLEIBE UNTER HERZLICHEM'),
 ('r6', [285,625,997,665],
  'tbr tl v. tl. tl. | v. tr lbr. | tblr. v. tl. tl. | '
  'lbr. bl tblr tr | lbr. tblr lbr tbr. | '
  'tbl tblr bl br. bl tr lbr. bl tl | tbl.', '',
  'GRUSS UND KUSS DEIN DICH LIEBENDER M'),
]

def main():
    manifest = json.loads((HERE/'source-hashes.json').read_text())
    for filename, expected in manifest.items():
        actual = hashlib.sha256((SOURCE/filename).read_bytes()).hexdigest()
        assert actual == expected, f'Changed source: {filename}'
    inventory = []
    total = 0
    for name, box, shapes, punctuation, expected in ROWS:
        groups = shapes.split('|')
        decoded = [''.join(KEY[x] for x in group.split()) for group in groups]
        assert ' '.join(decoded) == expected, (name, decoded)
        n = 0
        for group_number, group in enumerate(groups, 1):
            for shape in group.split():
                n += 1
                inventory.append({'id':f'{name}.{n:02}', 'row_box':box,
                                  'word':group_number, 'shape':shape,
                                  'literal':KEY[shape]})
        total += n
        if isinstance(punctuation, list):
            # r4 has a sentence stop after ZURÜCK and a continuation after SONN.
            shown = decoded[0]+'. '+decoded[1]+' '+decoded[2]+'='
        else:
            shown = ' '.join(decoded)+punctuation
        print(f'{name} ({n}): {shown}')
    assert total == 117, total
    # Re-encode every literal symbol to its transcribed shape, including Ü.
    reverse = {v:k for k,v in KEY.items()}
    assert len(reverse) == len(KEY)
    for entry in inventory:
        assert reverse[entry['literal']] == entry['shape']
    print('117/117 glyphs decoded and re-encoded; immutable source hashes match.')
    print('Literal HORGEN is retained: r3.06 is tbr. (H), not tbl. (M).')
    print('Unattested alphabet cells: '+', '.join(k+'='+v for k,v in KEY.items()
                                                if k not in {r['shape'] for r in inventory}))
    if '--write-transcript' in sys.argv:
        (HERE/'transcript.json').write_text(json.dumps({
            'provenance':'Manual visual transcription, not pixel OCR. Row boxes use original 1024x678 picture.jpg coordinates.',
            'glyphs':inventory}, ensure_ascii=False, indent=2)+'\n')

if __name__ == '__main__':
    main()
