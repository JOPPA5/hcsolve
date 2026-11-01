"""Reviewer's own decoder. rows = reviewer's transcription made from crops, keyed by ../../../hcp-1216/work/graphic-key.json,
then compared on base letters with the solver's ledger. # marks reviewer's hump sign (cursive m shape)."""
import json,re,unicodedata,os
H=os.path.dirname(os.path.abspath(__file__))
g=json.load(open(H+'/../../../hcp-1216/work/graphic-key.json'))
C={'2':'two-bars','3':'three-bars','6':'six','S':'section-mark','~':'wave','M':'three-short-strokes','N':'two-short-strokes',
'D':'joined-two-strokes','o':'cursive-loop','g':'open-loop-descender','T':'gamma','J':'inverted-T','x':'x','z':'crossed-diagonal',
'v':'chevron','i':'dotted-crossed-curve','y':'low-descender','R':'F','s':'right-bowl','C':None,'H':None}
rows='''S3Dv3sJo~2NS2M
HJ2TM3~y3TN2
gyoNSoszoNoSig2
z2NoRoMM3~v3T
T3MTxDoM2sx~Hogy
sz3R3NCs3s3NM3g
3RS3z3TD3M3gN2gyo66
oRoMM3MR3szo~g2~
H2sz3R3NCs3visz2
3RS3ziSS3Dv3s3M
HogyMx~2ToTJ2sz
63R3Ny632DJ22TSo
szoN3T3M3Ti~oNS2xNo
S2Nov3RN3S62RisM3R3T
~3Nv2gyoS3~oT33s2D
J22TxDvoz~3T3M3TM2g2M
R3sz3Ro#2si~2HoNisT3Nv3~3soR2iTv2Rv2
sz3R3T3T3~'''.split()
def d(c):
    if c=='#':return '#'
    if c=='H':return 'H'
    if c=='C':return 'c'
    return g[C[c]]
mine=[''.join(d(c) for c in r) for r in rows]
led=[]
for l in open(H+'/../../work/ledger.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip():continue
    t=[]
    for k in l.split()[1:]:
        if k[0]=='~':continue
        k=k.rstrip("':\"")
        t.append({'{lm}':'#','.':'','=':'','F':'r','X':'u','6':'b','CS':'cs','GY':'gy','H':'H','P':'H'}.get(k,k.lower()))
    led.append(''.join(t))
n=0
for i,(a,b) in enumerate(zip(mine,led),1):
    ok=a==b; n+=len(a)
    print(f'{i:02d}','SAME' if ok else 'DIFF',a,'' if ok else b)
print('letters compared',n)
from collections import Counter
print(sorted(Counter(''.join(mine)).items()))
