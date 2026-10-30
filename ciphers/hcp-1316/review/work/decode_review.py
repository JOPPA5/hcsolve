"""Independent decoder (reviewer). Uses glyph classes, not the solver's tokens or key code. Run from repo root."""
import re,sys,collections
D='ciphers/hcp-1316/'
K={'BAR2':'a','BAR3':'e','B':'b','Lb':'c','Rb':'s','d':'d','CR':'f','LP':'g','h':'h','I':'i','IT':'j','SEC':'k','W':'l','S3':'m','S3#':'m','S3?':'m','S2':'n','O':'o','FF':'r','G':'t','X':'u','X..':'ü','V':'v','Y':'y','Xt':'z',
   'BAR?':'?','ZIG?':'?','B|d?':'?','SEC?':'k','O?':'o','S3?':'m','CANC':''}
mine={}
for l in open(D+'review/work/reading.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    p=l.split(); mine[p[0]]=''.join(K[t] for t in p[1:])
sol={}
SK={'F':'r',')':'s','X':'u','Z':'z','6':'b','+':'f','H':'h','#':'','M#':'m','M?':'m','A?':'?','D?':'?','[K]':'k','[O]':'o','X:diaeresis':'ü','X:double-acute':'ű'}
for l in open(D+'work/ledger.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    p=l.split(); sol[p[0]]=''.join(SK.get(t,t.lower()) for t in p[1:])
d=0;n=0
for k in mine:
    a,b=mine[k],sol[k]
    print(k,a)
    if len(a)!=len(b): print('  LENGTH',a,b)
    for i,(x,y) in enumerate(zip(a,b)):
        n+=1
        if x!=y: d+=1; print(f'  diff {k} pos {i+1}: review {x!r} solver {y!r}')
print('compared',n,'differences',d)
c=collections.Counter(''.join(mine.values())); print(sorted(c.items(),key=lambda t:-t[1]))
