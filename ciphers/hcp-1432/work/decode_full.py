#!/usr/bin/env python3
"""HCP 1432: verify source hashes, decode the full Morse transcript literally
(International Morse A-Z), then apply the three disclosed editorial readings.
'(-)' in the transcript marks a dash crossed by the letter-closing slash; it is
decoded literally (as a full dash).
Run from the repo root:  python3 -I ciphers/hcp-1432/work/decode_full.py"""
from pathlib import Path
import hashlib, json
d = Path(__file__).resolve().parents[1]
for name, digest in json.loads((d/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((d/'source'/name).read_bytes()).hexdigest() == digest, name
print('source hashes OK')
codes = ('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- '
         '.-. ... - ..- ...- .-- -..- -.-- --..').split()
key = dict(zip(codes, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
# Disclosed editorial readings (row, group index) -> (letter, reason)
EDIT = {('home-1', 3): ('C', 'written .-.- (elements of C -.-. reversed); REA?HED HOME'),
        ('tired-1', 1): ('E', "written .- with the closing slash drawn through the dash (A = VARY); dash taken as struck out; VERY TIRED"),
        ('closing', 1): ('R', 'written -. (N); R is .-. ; no leading dot visible; YOUR ?RUE FRIEND')}
lit, ed, n = {}, {}, 0
for line in (d/'work/transcription-full.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    rid, body = [s.strip() for s in line.split('|')]
    groups = [g.strip() for g in body.split('/')]
    a, b = '', ''
    for i, g in enumerate(groups):
        n += 1
        g = g.replace('(', '').replace(')', '')
        L = key.get(g, '{' + g + '}')
        a += L
        b += EDIT[(rid, i)][0].lower() if (rid, i) in EDIT else L
    lit[rid], ed[rid] = a, b
    print(f'{rid:10s} {body:45s} literal {a:10s} read {b}')
print(f'{n} Morse groups, {sum(1 for g in "".join(lit.values()) if g=="{")} non-alphabet group(s), {len(EDIT)} editorial reading(s):')
for (r, i), (L, why) in EDIT.items():
    print(f'  {r}[{i}] -> {L}: {why}')
T = lambda k: ''.join(ed[r] for r in k)
print('\nLITERAL :', ' | '.join(lit.values()))
print('PLAINTEXT (Morse parts, editorial spacing; lower case = editorial reading):')
print('  ' + ' / '.join([T(['thanks-1', 'thanks-2', 'thanks-3']), T(['tired-1', 'tired-2']),
                         T(['home-1', 'home-2']), T(['closing'])]))
