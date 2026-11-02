"""Reviewer's independent decode of HCP1227: my own sign-class transcription made from
review/work crops, with values from the sister card's key file only; diff against work/ledger.txt.
Run from repo root: python3 -I ciphers/hcp-1227/review/work/decode_review.py
Classes: a two bars, e three bars, n two short, m three short, o loop, s right bowl, k section,
T gamma, U x (u), Z crossed diagonal, F r, W wave, D long+tick d, H tall+tick h/p, I dotted curve,
G open loop, Y low descender, B six, V chevron, J inverted T, P cross f, C opposed bowls.
"""
import json, os, difflib
R=os.path.dirname(os.path.abspath(__file__)); D=os.path.join(R,'..','..')
gk=json.load(open(os.path.join(D,'..','hcp-1301','work','graphic-key.json'),encoding='utf-8'))
M={'a':'two-bars','e':'three-bars','n':'two-short-strokes','m':'three-short-strokes','o':'cursive-loop',
 's':'right-bowl','k':'section-mark','T':'gamma','U':'x','Z':'crossed-diagonal','F':'F','W':'wave',
 'D':'joined-two-strokes','H':'two-tall-strokes','I':'dotted-crossed-curve','G':'open-loop-descender',
 'Y':'low-descender','B':'six','V':'chevron','J':'inverted-T','P':'cross'}
rows='''01 s Z e F e T e T T e D e s J o W a n k a m
02 B e C e s s o F a I T m e G k a H T a m m I T
03 n a G Y o F o m m e W P o G a D o k
04 e s k o s Z o n o k s o F a I n n e m
05 T U D o k e W I G a Z o D n I H o G Y
06 s Z o m B a T o n G Y o n e V a G Y
07 2 8 a n m e F e Z k e T o e n
08 H a T e H e T a m s Z o m B a T o n
09 V a F o m V a W a H o W D e H o G Y
10 H o W a Z T e n n e m T U D U m m e G
11 J e G Y Z e m a Z T I s H o G Y e n
12 n e m a Z o n a F a k o s o n V a G Y o k
13 a m e W I k a Z o n a V o n a W o n
14 V a n e n a n Y U G a T I o W D a W o n
15 V a G Y o k e s a F F a k e F e m H o G Y
16 a n e m D o H a n Y Z o s Z a k a s Z
17 B a U T a Z Z o n H o G Y e s e T
18 W e G k o n Y e n m m e G T a W a W
19 J a m e s e D e s e m m e F P e W
20 a T U W V a s U T a s F U H a T o W
21 a n Y I F a H o G Y W a T n I s e a k a F
22 B e n n | e H e D I G a Z e W s o T a W a W k o Z a s o m a B a W e s Z
23 m e F T H a s I k e F U a V o n a T o n T a W k o Z n I C a k I s
24 a B B a W e s Z e k'''
def val(t):
    if t in '28|': return t
    if t=='C': return 'cs'
    return gk[M[t]]
mine={}
for r in rows.split('\n'):
    l,*t=r.split(); mine[l]=''.join(val(x) for x in t)
sol={}
for line in open(os.path.join(D,'hcp-1227','work','ledger.txt'),encoding='utf-8') if False else open(os.path.join(R,'..','..','work','ledger.txt'),encoding='utf-8'):
    if line[0]=='#' or not line.strip(): continue
    l,*t=line.split()
    if l[0]=='S': continue
    sol[l]=''.join(x.split(':')[0] for x in t)
tot=0
for l in mine:
    # h/p near-homograph: compare with p folded to h
    a=mine[l].replace('p','h'); b=sol[l].replace('p','h'); tot+=len(a)
    if a!=b:
        print(l,'solver',sol[l]); print(l,'review',mine[l])
print('rows',len(mine),'chars',tot, 'solver chars',sum(len(v) for v in sol.values()))
