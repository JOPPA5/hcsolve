#!/usr/bin/env python3
"""Decode frozen manual American-Morse transcription, not the image pixels."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEY = {
    'A': '.-', 'B': '-...', 'C': '.. .', 'D': '-..', 'E': '.',
    'F': '.-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '-.-.',
    'K': '-.-', 'L': '=', 'M': '--', 'N': '-.', 'O': '. .',
    'P': '.....', 'Q': '..-.', 'R': '. ..', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '.-..',
    'Y': '.. ..', 'Z': '... .',
}
inverse = {v: k for k, v in KEY.items()}
assert len(inverse) == 26
for filename, expected in json.loads((ROOT / 'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((ROOT / 'source' / filename).read_bytes()).hexdigest() == expected
transcript = json.loads((ROOT / 'work/transcript.json').read_text())
count = 0
for n, col in enumerate(transcript['columns'], 1):
    words = []
    for box in col:
        codes = box.split(' / ')
        word = ''.join(inverse[code] for code in codes)
        assert [KEY[c] for c in word] == codes
        count += len(word)
        words.append(word)
    print(f'Column {n}: ' + ' '.join(words))
print(f'{count} mapped letters; source hashes and transcript/key roundtrips pass.')
# Terminal signature item (two rows of larger dots after HOME), decoded with the
# same key; patterns from work/terminal-scope.json. Kept apart from the 137 letters.
scope = json.loads((ROOT / 'work/terminal-scope.json').read_text())
sig = ''.join(inverse[scope[r]['manual_pattern']]
              for r in ('terminal_top_row', 'terminal_bottom_row'))
assert sig == 'RS'
print(f'Signature (terminal larger dots, separate item): {sig[0]}. {sig[1]}.')
print('Cancelled box (column 1, between A and HOLE): illegible under hatching, unread.')
print('These checks do not independently validate the manual reading of image pixels.')
