"""Reviewer's independent decoder: own key table (from hcp-1216 legend) and own row transcription
made by reading the reviewer's crops; compares with solver ledger. Run: python3 -I review/work/decode_review.py (from cipher dir)"""
import re,collections
K={'bb':'a','6':'b','()':'cs','tl':'d','3b':'e','+':'f','G':'g','tr':'h','i':'i','T':'j','S':'k','~':'l','3s':'m','2s':'n','O':'o','F':'r',')':'s','L':'t','x':'u','^':'v','Y':'y','Z':'z'}
R=''') Z 3b F 3b L 3b L 3b tl 3b ) T O ~ bb 2s
S bb 3s S i ^ bb 2s O 3s tr O G Y bb
~ 3b G T O 6 6 S 3b tl ^ 3b 6 3b 2s L bb
~ bb ~ T bb ) O F bb i 3s ) Z 3b F 3b ~
3s 3b 3s 2s 3b tr bb F bb G x tl T O 2s
F ? 3s tr O G Y 2s 3b 3s 3s 3b tr 3b L
L 3b 3s ~ 3b L x tl ? L O 3s tr O G Y
() x L O L O S O 2s O S ^ 3b L
~ 3b 2s ~ 3b 3s 3b G Y 3b S bb 3s x ~ bb L
) bb G 6 bb i G bb Z tr O G Y S 3b ^ 3b )
bb tr 3b 2s Z 3b 3s tl 3b 3s bb T tl ) Z 3b
F 3b 2s Y 3b 2s S O ~ L 3b S 3b Z # ^ 3b
O 2s i ) 6 3b + O G T bb ~ bb L 2s i
3b tl 3b ) 3b 3s tr O G Y i T 3b 2s tr 3b T
Z 3b L 6 3b ^ bb G Y 2s 3b 3s L 3b tr 3b L 3b S
F O ~ bb tl 3b 3b Z L 2s 3b 3s + O G T bb
3b ) Z F 3b ^ 3b 2s 2s i F O ~ bb 3s 3s bb T tl
) 3b 2s S i () bb S 3s bb G bb 3b tl 3b ) 3b 3s
tl F bb G bb () i ~ ~ bb G O 3s ~ 3b G Y 3b 2s
L x F 3b ~ 3b 3s 3s 3b ~ 3b tl 3b ) 3b 3s
() x L O F L O S i G i ) L 3b 2s ^ 3b
~ 3b 3b tl 3b ) 3b 3s ^ i ) Z O 2s L ~ bb
L bb ) F bb i 3s bb tl O T bb + 3b F i
() O S O ~ L 3s
) Z bb 3s L bb
~ bb 2s ) Z O F
) i F i tr x
S 3b tl ^ 3b ) ) 3b
x 3b F i'''
out=[]
for l in R.split('\n'):
    s=''
    for t in l.split():
        t=t.split(':')[0]
        s+={'?':'?','#':'#'}.get(t) or K[t]
    out.append(s)
import os
sol=[]
for l in open('work/ledger-opus.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab,*toks=l.split()
    m={'F':'r',')':'s','X':'u','6':'b','+':'f','H':'h','D':'d',"D'":'d','CS':'cs','M?':'m','a?':'?','e!':'#','T?':'t'}
    s=''
    for t in toks:
        t=t.split(':')[0]
        if t in'<>-': continue
        s+=m.get(t,t.lower())
    sol.append(s)
tot=0
for i,(a,b) in enumerate(zip(out,sol),1):
    print(f'{i:2}',a,'' if a==b else 'DIFF solver='+b)
j=''.join(sol)
print(len(R.split()),'reviewer signs')
for w in ['hogy','edesem','nem','feri','esem','csut']:
    print(w,j.count(w))
print(sorted(collections.Counter(j).items()))
