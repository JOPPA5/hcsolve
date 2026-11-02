#!/usr/bin/env python3
"""hcp-1169: verify scan hashes, decode work/transcription.txt, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '3ec4c551c3e28f853366a015308a771c03da40a240a1dcbaa2f4cbb282f16b9b',
     'source/address-large.jpg': 'aa0aa81d9899607b337214e101583a3573177289911fd381f4d2546380958d31',
     'work/hires/cpc_1915-12-29_HU_Mezokovesd_HU_Szomolya_szomolya-14_pic.jpg': 'f35c8b3b6dae5a81ff45cddf05a998242674c16b30d265fd8358fbee135dacbb',
     'work/hires/cpc_1915-12-29_HU_Mezokovesd_HU_Szomolya_szomolya-14_adr.jpg': '07ad286b25fab0692a520168e0a7f57b162114629ff32198ea41c3f77c59bc4a'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '1,': 'b',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '5.': 'ly', '6': 'j', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9,': 'z', '9': 'p'}
ODD = {'1~': 'i',    # esik: a tiny dot beside the 1, not counted as a mark
       '7~': 'sz'}   # szívű: in shape a short 7, (literal sívű); sz by word sense, see SOLUTION.md
K = {**KEY, **ODD}
EXPECT = """drága jó margitkám elhozta a jó isten az üjévet is melyet már oly nagyon vártam hogy
mégis közelebb legyek a szabadulás ideéhez no de majd elérkezik az is akor esik le szívemről egy
malomkő és hejébe te fogsz rajta fügni boldogan mint gyenge szívü fehér galamba fészkében midön
tojássait költi üdvözölve és csókolva téged hü kedvessed árpád""".split()
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'ü', 'u': 'ü', 'ű': 'ü', 'ý': 'y'})
EXPECT = [w.translate(FOLD) for w in EXPECT]
words, cur, odd, n = [], '', 0, 0
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    for tok in line.split():
        if tok == '/':
            if cur: words.append(cur); cur = ''
            continue
        if tok == '-':
            continue
        if tok.startswith('{'):
            if cur: words.append(cur); cur = ''
            continue
        if tok.endswith('}'):
            continue
        cur += K[tok]; n += 1; odd += tok in ODD
    if not line.rstrip().endswith('-') and cur:
        words.append(cur); cur = ''
if cur: words.append(cur)
print('ciphertext signs: %d - %d by the table, %d read by sense' % (n, n - odd, odd))
print('decoded:', ' '.join(words))
exp = ' '.join(EXPECT).replace('galamba', 'galamb a')
if ' '.join(words).replace('galamba', 'galamb a') != exp:
    sys.exit('MISMATCH\n' + exp)
print('decoded letters match the stated reading\n')
print('''[Drága jó Margitkám!]
[Elhozta a jó Isten az újévet is, melyet már oly nagyon vártam, hogy mégis közelebb
legyek a szabadulás ideéhez, no de majd elérkezik az is, akor esik le szívemről egy
malomkő és hejébe te fogsz rajta fügni boldogan mint gyenge szívű fehér galamb a
fészkében midőn tojássait költi.]
Most pedig [üdvözölve és csókolva téged) hű kedvessed Árpád]

Boldog ujévet kivánok mindnyájatoknak még a kis haragos Mariskónak is
nemigen megfek[t/f]el(?) 1915. XII/29 Mezőkövesd

Address: Tek. Szépreményü Sziber Margitka kisasszonynak / Szomolya) Bogács- / (Borsod m[?] u. p.
[ ] = enciphered on the card; spellings as on the card.''')
