"""Reviewer's independent decode of HCP1293. Own transcription by sign CLASS (one char per written sign),
made from review/work/crops, key typed from the class table in ciphers/hcp-1216/SOLUTION.md.
Run from repo root: python3 -I ciphers/hcp-1293/review/work/review_decode.py
Classes: 2 two bars,3 three bars,6 six,M three strokes,N two strokes,) right bowl,T gamma,F F-sign,O loop,I dotted loop,
S section sign,~ wave,X crossed diagonal,+ plain cross,f upright cross,G open loop w. descender,Y low descender,^ chevron,
J inverted T,H tall+RIGHT tick (h/p),D tall+LEFT tick (d, here also the p of row 14),C opposed bowls, Ö dotted loop, b=6"""
import re,sys,os
KEY=dict(zip('236MN)TFOISX~+fGY^JHDCÖ',['a','e','b','m','n','s','t','r','o','i','k','z','l','u','f','g','y','v','j','h','d','cs','ö']))
R={'01':')X3F3T3T3D3)3GY3T~3N','02':'F3M3NY3MN3H2F2G+DJONF2M','03':'HOGYOJ2N)OS2^2F2SOX','04':'T2TT2MH3IJ3N)OS2M3G',
'05':')OH2)3MT2FTOTT2^3X3N','06':'~3)MINTMO)TMISOF^3G3','07':'^O~T3~M3NT3M3N3D3)3M','08':'M2G2TS3F3)T3MD3N3MT2',
'09':'~2~T2M3)2XTGOND O~','10':'T2M3D3)3MHOGYH2X2','11':'M3NT3SD3)3NI)H2X2M3N','12':'T3M2TÖ~TÖXT3M3)','13':'M3NT3M)XO~G2~2T62',
'14':'3)3D3N63~3DT3MM2F)XO','15':'~ITOTT2SI)2N3^3M','16':'3)FÖGTÖN3~+TT2M','17':'MITN3MI)S3~MOND2','18':'NOMDF2G2CI~~2GOM',
'19':'2~IG^2FOMHOGY','20':'^I)X)X2JÖJ3S~3GJO66','21':')X3F3TN3S3D3)3M3X2~2TT2','22':'2FÖ^IDIDO2~2TMINDIG',
'23':'M2~3T2~3NIS3FJ3SI6OC2N2TOM2THOGY3~)3M6+','E1':'C+XT2M^I)XONT~2T2)F2MISOF2','T1':'MISOFIG3FTH2^2~2MI~','B1':'SÖX63','B2':'N3MJÖN',
'S1':'COSO','S2':'~OM','S3':')X2M','S4':'T2~2N','S5':')XOF','S6':'f3FI'}
L={}
for l in open('ciphers/hcp-1293/work/ledger.txt',encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        a,*t=l.split(); L[a]=''.join(x.split(':')[0].lower()+('̈' if ':' in x else '') for x in t)
import unicodedata as u
tot=0
for k,v in R.items():
    s=''.join(KEY[c] for c in v.replace(' ',''))
    tot+=len(v.replace(' ',''))
    a=u.normalize('NFC',L[k])
    print(k,s,'' if s==a else '  <> solver: '+a)
print('signs',tot,'unmapped none')
