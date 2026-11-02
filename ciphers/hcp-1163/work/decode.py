#!/usr/bin/env python3
"""hcp-1163: verify scan hashes, decode work/transcription.txt, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '5af3200e4ed97d7b869002ab8598df469c5bf5dc1b2938c32106259fa5c7bb98',
     'source/address-large.jpg': 'e716fb7607400bad2f1a677247106593240e146fa21a99037af95ba960093f06',
     'work/hires/cpc_1916-02-26_HU_Mezokovesd_HU_Szomolya_szomolya-20_pic.jpg': 'b0f32b1ef6b98e2bdfc4d2df0b315518e9119903d5e6f6560b5ab7d12d4f1024',
     'work/hires/cpc_1916-02-26_HU_Mezokovesd_HU_Szomolya_szomolya-20_adr.jpg': '7d088dbdcc2205d89e41d85e1d8c00df4dc6668897afd3556a635467c6bb977a'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '.1': 'u', '1,': 'b',
       '2': 'c', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
       '4': 'f', '4,': 'g', '4.': 'gy', '5': 'h', '5,': 'l', '5~l': 'l',
       '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z', '(': '(', ')': ')'}
out, toks = {}, []
for ln in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip():
        continue
    tag, body = ln.split(':', 1) if not ln.startswith(':') else (None, None)
    words = []
    for w in body.split('/'):
        ts = w.split()
        toks += ['5,' if t == '5~l' else t for t in ts if t not in '()']   # 5~l is one sign, l, not a type of its own
        words.append(''.join(KEY[t] for t in ts))   # KeyError = sign outside the key
    out[tag] = words
    print('%-4s %s' % (tag, ' '.join(words)))
# Reading = the raw decode with Hungarian accents and the word joins the sense needs.
READ = '''[Édes Margitkám!]
Értesítlek, hogy csütörtökön küldtem egy cédulát, nem tudom meg-
kaptad-e. Ha igen, akkor írd meg és felelj valamit a tartalmáról,
aztán írjál sokat.

V  Boldog csak úgy lehetek én,
   hogyha te leszel az enyém.
VI Nem szeretek mást, csak téged,
   csókkal teszek rá pecsétet.

Hogyha rád gondolok: boldogságom álma!
Istenem! ha egykor ez valóra válna.
Hogyha magaménak mondhatnálak téged,
megáldanám érte a nagy mindenséget.

Számtalanszor csókolva és üdvözölve maradok hűséges kedvesed és imádód (Árpád)'''
F = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'u', 'ű': 'ü'})
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha()).translate(F)
raw = ''.join(''.join(w) for w in out.values())
want = norm(READ.replace('\nV  ', '\n').replace('\nVI ', '\n').replace('V  ', '').replace('VI ', ''))
if norm(raw) != want:
    sys.exit('READING DOES NOT MATCH DECODE\n%s\n%s' % (norm(raw), want))
print('\nsigns: %d, distinct %d; reading matches the decode letter for letter (length of vowels folded only)\n'
      % (len(toks), len(set(toks))))
print(READ)
print('\nOpen: Mezőkövesd, 1916. II/26.')
print('Address: Őnagysága / Szépreményű / Sziber Margitka / kisasszonynak / (Borsodmegye) / Szomolya / u. p. (Bogács.)')
