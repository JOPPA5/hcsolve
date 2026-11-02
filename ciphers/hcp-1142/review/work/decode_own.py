# independent decoder: own table typed from hcp-1174/1178/1179 SOLUTION tables, plus proposed new values flagged
import re,collections
F={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á',':1':'ü','2,':'cs','2.':'é','3':'d','3,':'r','3.':'v','4,':'g','5':'h','5,':'l','6,':'n','7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z','1,':'b'}
N={'2':'c','4':'f','4.':'gy','5.':'ly','6':'j','6.':'ny','8.':'ty'}
c=collections.Counter();out=[]
for l in open('../../work/transcription.txt',encoding='utf-8'):
    l=l.strip()
    if not l or l[0]=='#' or l=='----':continue
    r=''
    for tok in l.split():
        if tok=='|': r+=' ';continue
        c[tok]+=1
        r+=F.get(tok) or ('['+N[tok]+']')
    out.append(r)
print('\n'.join(out));print(sum(c.values()),len(c));print(sorted(c.items()))
print('new-value tokens',sum(v for k,v in c.items() if k in N),{k:c[k] for k in N})
