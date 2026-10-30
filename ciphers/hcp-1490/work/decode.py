#!/usr/bin/env python3
"""HCP 1490: decode the manual Pigpen transcription (no OCR); verifies source hashes."""
from pathlib import Path
import hashlib

root = Path(__file__).resolve().parents[1]
SHA = {
    'address-large.jpg': '549fb70f66cfa2768ea8a293d4dc08c052fc630eca74555a91c43fe85434c909',
    'picture-large.jpg': 'f16fa0cb07e75eee25eef1239247cab4c89527746d67ecb87cfd00f14e4fc5d6',
    'metadata.md': 'b9c7b43cac25f76643c6f0e59678dbbe74b73fabb44285465afe9e146fa5ea83',
}
for name, h in SHA.items():
    if hashlib.sha256((root / 'source' / name).read_bytes()).hexdigest() != h:
        raise SystemExit(f'source hash mismatch: {name}')
print('source hashes OK')

shapes = ['BR', 'B', 'BL', 'R', 'C', 'L', 'TR', 'T', 'TL']
# Standard tic-tac-toe Pigpen layout; dot count 0/1/2 selects A-I / J-R / S-Z.
std = {f'{s}{d}': chr(65 + d * 9 + i) for d in range(3) for i, s in enumerate(shapes) if d * 9 + i < 26}
# Observed on this card: B2 stands where the text needs U and BL2 where it needs T
# (the standard layout has them the other way round) - see SOLUTION.md.
card = dict(std, B2='U', BL2='T')
special = {'C*': '?', 'TL2x': 'I', '[b]': '[b]'}

def dec(tokens, key, mark):
    out = []
    for t in tokens:
        if t == '|':
            out.append(' ')
        elif t in special:
            out.append(special[t] if not mark else '(' + special[t] + ')')
        else:
            out.append(key[t])
    return ''.join(out)

rows = []
for line in (root / 'work' / 'transcription.txt').read_text().splitlines():
    if line.strip() and not line.startswith('#'):
        label, toks = line.split(':', 1)
        rows.append((label.strip(), toks.split()))

print('\nLiteral, standard layout (special signs in parentheses):')
for label, toks in rows:
    print(f'  {label:9} {dec(toks, std, True)}')
print('\nReading with the card key (B2=U, BL2=T):')
for label, toks in rows:
    print(f'  {label:9} {dec(toks, card, True)}')
n = sum(1 for _, t in rows for x in t if x != '|')
print(f'\n{n} cipher signs; ? = unresolved sign, (I) = anomalous sign read by its outline, [b] = clear-script sign.')
print('\nFull message: the clear text is a MANUAL transcription of the card (hard-coded below);')
print('only the capitalised cipher passages come from the decoder above:')
print('  Hello (?)ONEY [= HONEY?] / how is times with you - they are fine with me. /'
      ' I want to see you at the Party to-morrow night not SUNDAY NIGHT'
      ' be sure and come. I must stop from a friend [b]DK')
