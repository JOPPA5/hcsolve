"""hcp-1038: decode the digit-plus-mark cipher. Run from repo root:
   python3 -I ciphers/hcp-1038/work/decode.py
Transcription by Claude Opus 5.5 (2026-11-03) from work/hires/*_adr.jpg, card rotated 90 deg."""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
 'source/picture-large.jpg': '7520cc53726befd0e8cd4c3f45874d969a40c04b08fa05cf40e71edad9bcdd3d',
 'source/address-large.jpg': '6de39a4c0beabeb1f4d4ce4b28c2f692e9aaf44c5b886c541ccba1d9ff4e1c76',
 'work/hires/cpc_1908-10-16_DE_-Altst_HU_Arad__pic.jpg': 'f051b004fc14e446b9fdeedf38666b1110efa7f78875b43752a55cbf433919a5',
 'work/hires/cpc_1908-10-16_DE_-Altst_HU_Arad__adr.jpg': 'cbfab7c45019fc6471604985f45b3bd6340b223cfd99fe5cbb2e0cfd69c1052c',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    assert got == h, f'hash mismatch {p}'
print('source hashes OK (4 files)')

# sign -> letter.  Marks: '.' dot on baseline, '..' two dots, '*' dot at mid height,
# "'" dot at top, ':' colon, ',' comma below, '^1' dot before (upper left of) the 1.
KEY = {
 '0': 'o', '1..': 'i', '1.': 'a', '1*': 'a', "1'": 'á', '1:': 'e', '^1': 'ü', '1,': 'b',
 '2': 'l', '2.': 'é', '2,': 'cs', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '4.': 'gy',
 '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
 '8': 'm', '8,': 't', '9': 'p', '9,': 'z',
}
# Signs exactly as written on the card; '|' marks the word breaks I insert (the card has none).
LINES = [
 "2. 3 1: 7, | 6 0 2 1.. 7 1* 8",
 "5 1. 5, 5, 0 8, 8, 1. 8 | 6, 1. 4. 0 6, | 7 1.. 7 1. 9 0 8, 8, | 8 1.. 1. 8, 8,",
 "1* 8 | 1.. 4, 1* 9, 1' 6, | 6, 1. 4. 0 6, | 7, 1. 6 6, 1* 5, 0 8 | 3 1: | 2. 6, 1: 8",
 "1.. 7, | 4, 0 6, 3 0 5, 8, 1. 8 | 5 0 4. | 2. 3 1: 7, 1. 9 6 1. | 7 1: 9,",
 "2. 1, 1: | 7 1: 3, ^1 5, 6, 1: 7 | 1. | 5, 1. 9 0 7",
 "7, 0 7 7. 0 3, | 2, 0 7 0 5, 0 8",
 "7, 1. 6. 1..",
 "3. 1* 3, 0 7 | 3. 1* 5 1* 7. 8,",   # line along the bottom edge, below the signature
]
READING = [
 "édes jolikám",
 "hallottam nagyon kikapott miatt",
 "am igazán nagyon sajnálom de énem",
 "is gondoltam hogy édesapja kez",
 "ébe kerülnek a lapok",
 "sokszor csókolom",
 "sanyi",
 "várok választ",
]
def fold(s):
    return s.translate(str.maketrans('áóé', 'aoe'))
n = 0; sense = []
out = []
for i, (ln, rd) in enumerate(zip(LINES, READING)):
    words = []
    for w in ln.split('|'):
        toks = w.split()
        n += len(toks)
        words.append(''.join(KEY[t] for t in toks))
    lit = ' '.join(words)
    # compare ignoring accents the writer leaves out (á/a, ó/o); é is always marked
    if fold(lit) != fold(rd):
        sense.append((i, lit, rd))
    out.append((lit, rd))
print(f'{n} cipher signs, {len(set(t for l in LINES for t in l.replace("|"," ").split()))} distinct')
for lit, rd in out:
    print(f'  {lit:40s} -> {rd}')
print('differences between letters as written and the reading:')
for i, lit, rd in sense:
    print(f'  line {i}: {lit!r} read as {rd!r}')
assert [i for i, _, _ in sense] == [7], sense   # only the 5 (h) in vahaszt -> választ
print()
print('Plaintext (Hungarian):')
print('Édes Jolikám! Hallottam, nagyon kikapott miattam. Igazán nagyon sajnálom, de én nem '
      'is gondoltam, hogy édesapja kezébe kerülnek a lapok. Sokszor csókolom Sanyi')
print('[plain:] Szívélyesen üdvözlöm Sanyi')
print('Várok választ.')
