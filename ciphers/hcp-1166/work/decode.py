#!/usr/bin/env python3
"""hcp-1166: check scan hashes, decode work/transcription.txt, print and verify the plaintext."""
import hashlib, os, re, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '06fe1fff1355861d89455197679db7a964cb43ae8f7688af98e6fcf32058b161',
     'source/address-large.jpg': 'dc844feb103ee0484db1e5fbb532735cb413ad463637b746b9dc368e8f5b4143',
     'work/hires/cpc_1916-04-11_HU_Mezokovesd_HU_Szomolya_szomolya-27_pic.jpg': '29afbdadb3438b7a1ea239b634931c6f8dd55758f611b748702a738e0d91e668',
     'work/hires/cpc_1916-04-11_HU_Mezokovesd_HU_Szomolya_szomolya-27_adr.jpg': '37e7bbb7364774a281b997bbe5c184abc62f58f7fe08fb3adb308dd75d663c1f'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '1,': 'b',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '5.': 'l', '6': 'j', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '8.': 'ty', '9': 'p', '9,': 'z'}
EXPECT = {  # literal decoded words of each line, letters as the signs give them
 'L01': 'édes margitkám', 'L02': 'szerencsésen hazaérkeztünk nagyon szép',
 'L03': 'és meleg idö volt egy negyed ketöre ér', 'L04': 'tünk haza a kertekig',
 'L05': 'danolaztünk de aztán álmos', 'L06': 'lettünk és csak ügy mentünk',
 'L07': 'némán egymás ütán erröl', 'L08': 'most többet nem irok szervüsz',
 'P09': 'Sehol nincs a világon', 'P10': 'Margitkának párja', 'P11': 'Adjatok egy kis kártyát',
 'P12': 'Hadd irom izt rája', 'P13': 'Udvarloid seregében', 'P14': 'Minő helet adsz nekem',
 'P15': 'Utolsonak ne hagyj engem', 'P16': 'Végy elsönek édesem',
 'P17': 'M betüvel ir most a tollam', 'P18': 'S rád gondolok margitkám',
 'P19': 'Üdvözletem küldöm neked', 'P20': 'S azt kivánom légy vidám',
 'B21': 'üdvözlettel sok csokkal és öleléssel', 'B22': 'maradok hü kedvesed árpád'}
n = odd = 0; dec = {}
for ln in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    tag, body = ln.split(':', 1)
    body = re.sub(r'\{.*?\}', '', body); words = []
    for w in body.split(' / '):
        out = ''
        for t in w.split():
            if t[0] == '=':
                out += t[1:]
                continue
            n += 1
            if '~' in t: odd += 1; out += t.split('~')[1]
            else: out += KEY[t]
        words.append(out)
    s = ' '.join(words)
    s = re.sub(r'\s+', ' ', s).strip()
    dec[tag] = s
    if s != EXPECT[tag]: sys.exit('MISMATCH %s: %r vs %r' % (tag, s, EXPECT[tag]))
print('cipher signs: %d; %d decode by the key as written, %d taken by word sense (marked ~)\n' % (n, n - odd, odd))
print('[literal decode, line by line; open text kept]')
for k, v in dec.items(): print(k, v)
print('''
[reading]
Mezőkövesd, 1916. IV/11.

Édes Margitkám!
Szerencsésen hazaérkeztünk, nagyon szép és meleg idő volt, egy negyed kettőre
értünk haza a kertekig, danolásztunk, de aztán álmos lettünk és csak úgy mentünk
némán egymás után) erről most többet nem írok) Szervusz.

Sehol nincs a világon
Margitkának párja,
Adjatok egy kis kártyát,
Hadd írom ezt rája.

Udvarlóid seregében
Minő helyet adsz nekem?
Utolsónak ne hagyj engem,
Végy elsőnek, édesem.

M betűvel ír most a tollam,
S rád gondolok, Margitkám,
Üdvözletem küldöm neked,
S azt kívánom: légy vidám!

Üdvözlettel, sok csókkal és öleléssel maradok hű kedvesed) Árpád)

Address (open): Őnagysága. / Rózsa reményű. / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács.''')
