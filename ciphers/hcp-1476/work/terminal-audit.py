#!/usr/bin/env python3
"""Inventory a frozen manual transcription; optionally reproduce the scan crop.

No OCR or automated identification of the terminal ink is performed.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io
import runpy
import sys

here = Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()) as checked:
    state = runpy.run_path(str(here / 'decode.py'))
print(checked.getvalue(), end='')
print('position\tline\ttoken\treading')
position = 0
for row, line in enumerate((here / 'transcription.txt').read_text().splitlines(), 1):
    for token in line.split():
        if token in state['key']:
            position += 1
            print(f"{position}\t{row}\t{token}\t{state['key'][token]}")
        elif token == 'END_MARK':
            print(f'after {position}\t{row}\tEND_MARK\tnot a letter (probably printed ornament)')
assert position == 22
print('Terminal region: upright coordinates x=450..549, y=425..494;')
print('upright = original address-large.jpg rotated 90 degrees clockwise.')
print('Two curved uprights, connecting bar, central dark deposit: visual observations.')
print('End mark judged a printed ornament of the card divider (review 1, F3); not cipher.')
if '--crop' in sys.argv:
    from PIL import Image
    original = Image.open(here.parent / 'source/address-large.jpg')
    upright = original.transpose(Image.Transpose.ROTATE_270)
    upright.crop((450, 425, 550, 495)).resize((1000, 700)).save(
        here / 'terminal-context-20261026.png')
    print('Wrote terminal-context-20261026.png; 10x display enlargement, no new detail.')
