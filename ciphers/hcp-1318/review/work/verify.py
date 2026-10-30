"""Independent check: reviewer's own sign-class transcription (from review/work/crops), decoded with the
family key read from hcp-1216/work/graphic-key.json, diffed against the solver's ledger. Run from the cipher dir."""
import json,re
K=json.load(open('../hcp-1216/work/graphic-key.json'))
A=dict(a='two-bars',b='six',d='joined-two-strokes',e='three-bars',f='cross',g='open-loop-descender',H='tall-short-stroke',
 i='dotted-crossed-curve',j='inverted-T',k='section-mark',l='wave',m='three-short-strokes',n='two-short-strokes',o='cursive-loop',
 r='F',s='right-bowl',t='gamma',u='x',v='chevron',z='crossed-diagonal')
def dec(c):
    if c=='Y': return 'y'          # low looped sign, only ever after g (family gy)
    if c=='C': return 'cs'         # opposed bowls
    if c=='H': return 'h'          # h/p form; 'd' from sense in Sándor, de: marked D
    if c=='D': return 'd'
    return K[A[c]]
# one letter = one sign class; capitals H D Y C as above; '.' punctuation; {x} seen only through stain
R="""01 kedvesjolankamtudatom
02 HogYszerenCesenmeger
03 keztem.ijenkorerzem
04 CakHogYmitvesztek
05 enjolankambaelijenkor
06 ismikorelkelvalaunk
07 egYmast{o}lszeretnem
08 sziveme{r}{z}elmeitbeol
09 tanieze{n}{e}desjolankamszi
10 vebeakorjolankamisugY
11 vonzodnaHozamminten
12 magaHozaComakotat
13 adtamsanDornakabela
14 valnembeszelHetem
15 mertnemvoltidom
16 Demostnemirok
17 tobbetmertmeral
18 mosvagYokisten
19 veledesem
20 mindenkielHitte
21 HogYkatonavagYok
s1 Cokol
s2 lom
s3 szam
s4 talan
s5 szor
s6 imado
s7 jaferi"""
mine={}
for L in R.splitlines():
    lab,t=L.split(); out=[]
    for c in re.sub(r'[{}]','',t):
        out.append('.' if c=='.' else dec(c))
    mine[lab]=out
sol={}
for L in open('work/ledger.txt',encoding='utf-8'):
    if L.startswith('#') or not L.strip(): continue
    lab,*ts=L.split()
    sol[lab]=[{'D':'d','ö':'o'}.get(x,x) for x in (re.sub(r"[\[\]'~]",'',t) for t in ts)]
tot=0;diff=0
for l in sol:
    a,b=mine[l],sol[l]; tot+=sum(x!='.' for x in b)
    if a!=b:
        d=[(i,x,y) for i,(x,y) in enumerate(zip(a,b)) if x!=y]; diff+=len(d)
        print('DIFF',l,len(a),len(b),'pos,mine,solver',d)
print('solver signs',tot,'mine',sum(x!='.' for v in mine.values() for x in v),'differences',diff)
from collections import Counter
print(sorted(Counter(x for v in mine.values() for x in v if x!='.').items(),key=lambda p:-p[1]))
