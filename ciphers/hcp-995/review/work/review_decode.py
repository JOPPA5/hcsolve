#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 995 (does not import solver code).

Transcription made by the reviewer from source/picture.jpg crops (review/work/*.png).
Grid cells numbered by position in a 3x3 tic-tac-toe grid:
  1 2 3      1 = ┘   2 = ⊔   3 = └
  4 5 6      4 = ⊐   5 = □   6 = ⊏
  7 8 9      7 = ┐   8 = ⊓   9 = ┌
'*' = interior dot, '"' = two umlaut strokes above.
Extra signs: '|' single upright stroke, 'chk' check-like V, '^' upward wedge.
'/' = word separator (dash on the card), punctuation kept as is.
"""
import collections

KEY = {}
for i, ch in enumerate('ABCDEFGHI', 1):
    KEY[str(i)] = ch
for i, ch in enumerate('KLMNOPQRS', 1):
    KEY[str(i) + '*'] = ch
KEY.update({'|': 'T', 'chk': 'U', '^': 'W', '^*': 'Z', '1"': 'Ä', 'chk"': 'Ü'})

REGIONS = [
    ('initials in prose line "von ... hoffen"', '3* . 1* 2* . 9* . 3* .'),
    ('main row 1', '^ 9 5 / 7 5 6 1" 2* 2* | / 4 9 8* / 4 9 5 / 1* 1 8* | 5 ? 9* 9 4* 4'),
    ('main row 2', '4 9 5 / 2 5 9 4 5 4* / 4* 9 3 8 | / ^* chk / '
                   '2 5 4* 5 9 4 5 4* ? / 8 5 8* ^* 2* / 7 8* / [u] 1* chk" 9* 9* 5 .'),
]
used = collections.Counter()
total = 0
for name, row in REGIONS:
    out = []
    for tok in row.split():
        if tok == '/':
            out.append(' ')
        elif tok in {'.', '?', ','}:
            out.append(tok)
        elif tok == '[u]':
            out.append('u ')   # ordinary cursive, not a cipher glyph
        else:
            out.append(KEY[tok])
            used[tok] += 1
            total += 1
    print(f'{name}: ' + ''.join(out))
print('cipher glyphs:', total)
print('distinct cipher signs used:', len(used))
