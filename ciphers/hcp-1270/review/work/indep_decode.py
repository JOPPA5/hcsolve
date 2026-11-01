# independent decoder: own sign-name -> letter map, ledger read as data; re-segments words, checks
import re,collections,sys
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1270/work/ledger.txt'
M=dict(F='r',X='u');M[')']='s';M['6']='b';M['+']='f';M['H']='h';M['CS']='cs'
rows=[];c=collections.Counter()
for l in open(D,encoding='utf-8'):
    if l.startswith('#') or not l.strip():continue
    p=l.split();s=''
    for t in p[1:]:
        c[t]+=1
        b=t.split(':')[0].strip('[]')
        if b in '#|':continue
        v=M.get(b,b.lower())
        s+=v.replace('o','ö').replace('u','ü') if ':d' in t else v
    rows.append((p[0],s))
for r in rows:print(*r)
print(sum(c.values()));print(sorted(c.items(),key=lambda x:-x[1]))
