# Independent decoder: own row reading -> letters via the graphic classes of hcp-1216/work/graphic-key.json; compares with solver's ledger.
import json,re,sys
key=json.load(open('../../../hcp-1216/work/graphic-key.json'))
G={'=':'two-bars','E':'three-bars','6':'six','S':'section-mark','~':'wave','M':'three-short-strokes','N':'two-short-strokes','O':'cursive-loop',
   'D':'joined-two-strokes','I':'dotted-crossed-curve','T':'inverted-T','F':'F',')':'right-bowl','(':'left-bowl','G':'gamma','+':'cross','g':'open-loop-descender','y':'low-descender','V':'chevron'}
def dec(c):
    if c=='P':return 'h'
    if c=='X':return '#'     # u/z left open
    if c=='U':return 'ü'
    if c=='Q':return 'ö'
    if c in 'anl':return c
    if c=='-':return ''
    return key[G[c]]
mine={};
for l in open('my_reading.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip():continue
    k,t=l.split(None,1); mine[k]=''.join(dec(c) for c in t if c not in ' \n')
sol={}
strip=str.maketrans('áéíóőú','aeioou')
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip():continue
    k,*t=l.split(); s=''
    for x in t:
        if x=='|':continue
        b=x.split(':')[0].rstrip('!')
        if b.endswith('*'): s+=b[0].lower(); continue
        b=b.lower(); acc=x.split(':')[1] if ':' in x else ''
        s+={'o':'ö','u':'ü'}[b] if acc=='d' else b
    sol[k]=s
n=bad=0
for k in sol:
    a=mine[k]; b=re.sub('[uz]','#',sol[k]).replace('ő','o')
    a2=a.replace('cs','cs')
    ok=a==b; n+=len(b); bad+=not ok
    print(k,'OK ' if ok else 'DIFF',a if ok else f'{a}  <>  {b}')
print('rows',len(sol),'chars',n,'rows differing',bad)
print('cross signs (u/z left open):',sum(v.count('#') for v in mine.values()))
from collections import Counter
print(sorted(Counter(''.join(sol.values())).items()))
