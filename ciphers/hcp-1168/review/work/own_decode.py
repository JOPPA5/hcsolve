#!/usr/bin/env python3
# Independent decoder (reviewer). Own key dict built from hcp-1174 table + the solver's 7 new values
# marked separately; no code shared with work/decode.py. Reports frequency of each sign + token.
import sys,collections
base={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á',':1':'ü','2,':'cs','2.':'é','3':'d','3,':'r','3.':'v','4,':'g','5':'h','5,':'l','6,':'n','7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z'}
new={'1,':'b','2':'c','4':'f','4.':'gy','5.':'l','6':'j','6.':'ny','.1':'u'}
K={**base,**new}
c=collections.Counter()
for l in open(sys.argv[1],encoding='utf-8'):
    if l.startswith('#') or not l.strip():continue
    tag,rest=l.rstrip('\n').split(' ',1)
    out=[]
    for t in rest.split():
        if t=='|':out.append(' ');continue
        if t=='=':continue
        t0=t.split('~')[0]; c[t0]+=1
        out.append(K[t0].upper() if '~' in t else K[t0])
    print(tag,''.join(out))
print(sum(c.values()),len(c)); print(sorted(c.items(),key=lambda x:-x[1]))
print('new-value counts',{k:c[k] for k in new})
