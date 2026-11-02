#!/usr/bin/env python3
"""hcp-1147: run from repo root: python3 -I ciphers/hcp-1147/work/decode.py
Checks source hashes, decodes work/transcription.txt with the key below, asserts every word
against the stated reading, prints the plaintext. Open text (address, date) is hard-coded."""
import hashlib, pathlib, re, sys
D = pathlib.Path('ciphers/hcp-1147')
H = {'source/picture-large.jpg': 'ecbbb4f8650c7fe36a1e2dc1f34717c51c95b28284b89c802fcfb1a0f3d16e66',
     'source/address-large.jpg': '2dc168eb936fcd6217397a7317f51d2451c281e6aebbb39bf921c144187cc0e9',
     'work/hires/cpc_1916-04-20_HU_Mezokovesd_HU_Szomolya_szomolya-29_pic.jpg': '2cf393854245eee1e1a3f0bff56a3166705a6e42885835ee13c40241454dbc0c',
     'work/hires/cpc_1916-04-20_HU_Mezokovesd_HU_Szomolya_szomolya-29_adr.jpg': '779541988a20f41e4c84c3f4bbd11d84c922d65e454b0c6b1419fb5157132cc0'}
for f, h in H.items():
    if hashlib.sha256((D / f).read_bytes()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + f)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '·1': 'u', ':1': 'ü', '1,': 'b',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '8.': 'ty', '9': 'p', '9,': 'z'}
EXPECT = {
 'H1': 'édes margitkám',
 'L1': 'ha pista húsvétra kap szabadságot',
 'L2': 'légy szíves írd meg neki hogy hacsak',
 'L3': 'lehet nálatok töltse el a hús=',
 'L4': 'vétot mert nagyon',
 'L5': 'szeretnék vele ta=',
 'L6': 'lálkozni hátha többet nem',
 'L7': 'beszélhetek vele most egyéb',
 'L8': 'újságot nem írok majd szóval töb=',
 'L9': 'bet',
 'M1': 'hozzád repül a távolból',
 'M2': 'kis angyalom a madárka',
 'M3': 'oda száll az ablakomra',
 'M4': 'csőrében egy képes kártya',
 'D1': 'északon és délen',
 'D2': 'képed itt van vélem',
 'D3': 'keleten nyugaton',
 'D4': 'te vagy gondolatom',
 'N1': 'kicsi házban falu végén',
 'N2': 'hogy ha laknám veled én',
 'N3': 'azt mondanám ottan lakom',
 'N4': 'a világ közepén',
 'R1': 'most többet', 'R2': 'nem tudok', 'R3': 'írni mert', 'R4': 'nem fér',
 'R5': 'sok csókkal', 'R6': 'és ölelés=', 'R7': 'sel maradok',
 'R8': 'hozzád mindig', 'R9': 'hű imádód', 'R10': 'árpád'}
FOLD = str.maketrans('úóíőű', 'uoiöü')
n = odd = 0
out = {}
for line in (D / 'work/transcription.txt').read_text(encoding='utf-8').splitlines():
    if not line or line[0] == '#':
        continue
    lab, body = line.split(None, 1)
    words = []
    for w in body.split('|'):
        s = ''
        for t in w.split():
            if t == '=':
                s += '='
            elif t[0] == '{':
                s += t[1:-1]
            elif '~' in t:
                sign, letter = t.split('~')
                s += letter; n += 1; odd += 1
            else:
                s += KEY[t]; n += 1
        words.append(s)
    got = ' '.join(words).replace(' =', '=')
    want = EXPECT[lab]
    if got != want.translate(FOLD):   # the cipher does not mark vowel length of o, i, u, ö, ü
        sys.exit('MISMATCH %s: %r vs %r' % (lab, got, want))
    out[lab] = want
print('cipher signs: %d; %d by the table, %d taken by sense (marked ~ in the transcription)' % (n, n - odd, odd))
print('every line matches its stated reading\n')
J = lambda *ls: ' '.join(out[l] for l in ls).replace('= ', '')
print('Őnagysága. Rózsa Reményü Sziber Margitka Kisasszonynak Szomolya u.p. (Bogács)')
print('(Mezőkövesd, 1916. IV/20.)  [open text; postmarks APR 20]\n')
print(out['H1'] + '!')
print(J('L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9'))
print()
print(J('M1', 'M2', 'M3', 'M4'))
print()
for l in 'D1 D2 D3 D4'.split(): print(out[l])
print()
for l in 'N1 N2 N3 N4'.split(): print(out[l])
print()
print(J('R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9'), '(' + out['R10'] + ')')
