#!/usr/bin/env python3
# hcp-1142: checks source hashes, decodes work/transcription.txt, prints the card. Run from the repo root.
import hashlib, os
D='ciphers/hcp-1142/'
H={'source/picture-large.jpg':'2db2301ada8cc6845c7eea7d3d2f647197ffaf6507e55da4b916197537685995',
 'source/address-large.jpg':'70584586a61a86f59eaf112188c61da6fdbb2eb51fe75a5e7ebdeabeccf98b8d',
 'work/hires/cpc_1906--_HU_Mezokovesd_HU_Szomolya_szomolya-41_pic.jpg':'2b7ecfdafd5d89e96498be4bb2d9466eb29626b5e6e5b0151be4bf06c748fd75',
 'work/hires/cpc_1906--_HU_Mezokovesd_HU_Szomolya_szomolya-41_adr.jpg':'8ad70f596cf55b6a1e2ad85919312b63d3d4fd1d1b9cf7a2b2c35ee83c62f2a7'}
for f,h in H.items():
    assert hashlib.sha256(open(D+f,'rb').read()).hexdigest()==h, f
print('hashes OK (4 files)')
KEY={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á',':1':'ü','1,':'b','2':'c','2,':'cs','2.':'é',
 '3':'d','3,':'r','3.':'v','4':'f','4,':'g','4.':'gy','5':'h','5,':'l','5.':'ly','6':'j','6,':'n','6.':'ny',
 '7':'k','7,':'s','7.':'sz','8':'m','8,':'t','8.':'ty','9':'p','9,':'z'}
n=0; used=set(); lines=[]
for l in open(D+'work/transcription.txt',encoding='utf-8'):
    l=l.strip()
    if not l or l[0]=='#': continue
    if l=='----': lines.append('----'); continue
    ws=[]
    for w in l.split('|'):
        t=w.split(); n+=len(t); used|=set(t)
        ws.append(''.join(KEY[s] for s in t))
    lines.append(' '.join(ws))
print('\n'.join(lines))
print(f'{n} cipher signs, {len(used)} distinct; all in the key')
EXPECT="""kedves margitkám
a lapodat megkaptam
amelynek nagyon meg
örültem vasárnap ha
jo üdö lesz felmegyek
----
aszt mondja szivemnek
mindenik verése
te vagy a világnak
legszebb teremtése
----
e kártyán piciny hely van""".split('\n')
EXPECT+="""nem sokat irhatok
üdvözöllek s aki vol
tam
tenéked az maradok""".split('\n')
assert lines==EXPECT, [ (a,b) for a,b in zip(lines,EXPECT) if a!=b]
print('decoded lines match the stated reading')
print()
print('Open text at the foot: Számtalanszor csókollak mindanyájatokat (?), (Sz. A.)')
print('Address: Tek. / Szépreményü / Sziber Margitka / kisasszonynak / (Szomolya.) / u. p. Bogács / (Borsod m.)')
