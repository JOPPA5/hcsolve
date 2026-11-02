#!/usr/bin/env python3
"""hcp-1158: check scan hashes, decode work/transcription.txt with the Mezokovesd digit key, print the text."""
import hashlib, os, sys, re
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = 'cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44'
H = {'source/picture-large.jpg': '77b36d882316918e786bb51ec1763be7d053a6328570e960a6f853f13d0e846f',
     'source/address-large.jpg': 'a4ae2723aa61dd5e03f5fdc33f6dcf4aa2c95ea6608b192139de62895d922606',
     'work/hires/%s_pic.jpg' % B: '238337e6c1ac41fa2539d8c6a4899fc4df873dfbcf1ec2a92b9a2b554189320f',
     'work/hires/%s_adr.jpg' % B: 'b3f11439296f411b448e424d0ff7e8ae619ec7a5a75c28957a0a55d33dbca645'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '1,': 'b',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
READ = {'T': 'édes margitkám', '1': 'terem virág kis kertemben', '2': 'terem künn a réten',
        '3': 'de a legszebb virág te vagy', '4': 'édes mindenségem',
        '5': 'ha egymáshoz kincsem', '6': 'igaz szivvel leszünk', '7': 'a boldogság révébe',
        '8': 'meglásd beevezünk', '9': 'ird meg nékem édes szentem', '10': 'drága virágszálom',
        '11': 'leszel-e hogy ha meg kérlek', '12': 'a szeretö párom', '13': 'ez t a pár sort küldöm',
        '14': 'neked szép babám', '15': 'légy boldog és gondolj', '16': 'néha-néha rám',
        '17': 'számtalanszor üdvözöl és', '18': 'csokol hü kedvesed árpád'}
n = odd = 0; out = {}
for ln in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    k, rest = ln.split(' ', 1); words = []
    for w in rest.split(' / '):
        s = ''
        for t in w.split():
            if t == '-': s += '-'; continue
            m = re.fullmatch(r'(.+)<(.+)>', t)
            if m: s += m.group(2); odd += 1
            else: s += KEY[t]
            n += 1
        words.append(s)
    out[k] = ' '.join(words)
for k, v in READ.items():
    a = out[k].replace(' ', ''); b = v.replace(' ', '')
    if a != b: sys.exit('MISMATCH line %s: %r vs %r' % (k, out[k], v))
print('cipher signs: %d; %d decode by the table, %d by sense' % (n, n - odd, odd))
print('distinct signs: %d\n' % len(KEY))
for k in READ: print('%-3s %s' % (k, out[k]))
print('''
Plain on card (head of message), literal: Ha lapomat megkapod és / válaszolni fogsz légyél szíves- /
megirni a Pista címét / mert szeretnek már neki- / is irni.
Normalised: Ha lapomat megkapod és válaszolni fogsz légyél szíves megirni a Pista címét
mert szeretnék már neki is irni.
Margin: Mezőkövesd: 1916, I/11.
Address: Őnagysága / Rózsareményü / Sziber Margitka / kisasszonynak / (Borsod m.) Szomolya / u. p. Bogács''')
