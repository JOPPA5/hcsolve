#!/usr/bin/env python3
"""hcp-1172: verify scan hashes, decode work/transcription.txt, print the PARTIAL reading."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '7bac2d2cf5bf5e5c234be1ad6762fe07c5483ed179e4e7c5101c859081f69acd',
     'source/address-large.jpg': 'b77709657191810701979d52f0587c3551b60ef622c5ba8ad50ac0c5520389cb',
     'work/hires/cpc_1915-11-02_HU_Mezokovesd_HU_Szomolya_szomolya-04_pic.jpg': '475f0d60f92892cb84b8a75ad7310dd513c4f56ac467c2e2d143aa9953d1571e',
     'work/hires/cpc_1915-11-02_HU_Mezokovesd_HU_Szomolya_szomolya-04_adr.jpg': '4ee0af659d05dda54ea3ff257f9b9072b4e907c9c520b6b6003aaacb300a0910'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0':'o','1':'i','1.':'a','1:':'e',"1'":'á','.1':'u','1,':'b','2':'[2]','2,':'cs','2.':'é',
       '3':'d','3,':'r','3.':'v','4,':'g','4.':'gy','5':'h','5,':'l','6':'j','6,':'n','6.':'ny',
       '7':'k','7,':'s','7.':'sz','8':'m','8,':'t','8.':'t'}
out = []
for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    t = [KEY[x.rstrip('?')] for x in l.split()]
    out.append(''.join(t)); print(l.strip().ljust(46), ''.join(t))
s = ''.join(out)
print('\nraw:', s)
print('signs:', sum(len(l.split()) for l in open(os.path.join(D,'work/transcription.txt')) if not l.startswith('#')))
print('reading: (Kedves Margitkám) | a kártában aszt kérdesztem hogy kere[2]e te is írnál mindig számokkal'
      ' hogy ne tudja seki a olvasni | számtalanszor csókollak mindnyájatokat')
