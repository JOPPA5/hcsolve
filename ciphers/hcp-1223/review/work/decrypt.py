# Independent decoder: own mapping from shape names, written from hcp-1216's table, applied to the reviewer's own row-19 correction.
import sys,re
shape={'S':'s','Z':'z','E':'e','R':'r','T':'t','D':'d','J':'j','O':'o','L':'l','A':'a','N':'n','K':'k','M':'m','V':'v','G':'g','H':'h','P':'p','I':'i','B':'b','U':'u','Y':'y','LY':'ly','CS':'cs','FF':'f','HD':'d','.':'.'}
rows={}
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    p=l.split(); rows[p[0]]=p[1:]
tot=0;un=set()
for k,v in rows.items():
    out=''
    for t in v:
        b=t.split(':')[0]; a=t.split(':')[1] if ':' in t else ''
        if b not in shape: un.add(b); continue
        out+=shape[b]+{'':'','acute':"'",'diaeresis':'"'}[a]; tot+= b!='.'
    print(k,out)
print('signs',tot,'unknown',un)
from collections import Counter
c=Counter(t.split(':')[0] for v in rows.values() for t in v if t!='.')
print(c.most_common())
