# independent decoder: table retyped from hcp-1174/1179 + card-specific additions, ignores solver's READ list and ~ overrides
import re,collections,sys
T={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á',':1':'ü','1,':'b','2,':'cs','2.':'é','3':'d','3,':'r','3.':'v',
'4':'f','4,':'g','4.':'gy','5':'h','5,':'l','5.':'ly','6':'j','6,':'n','6.':'ny','7':'k','7,':'s','7.':'sz','8':'m','8,':'t','8.':'ty','9':'p','9,':'z'}
out=[];c=collections.Counter();n=0
for l in open(sys.argv[1],encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    s=l.split()[1:]; w=''
    for t in s:
        if t=='|': out.append(w);w='';continue
        if t=='=': continue
        raw=t.split('~')[0]; n+=1;c[raw]+=1; w+=T[raw]
    out.append(w+('+' if s[-1]=='=' else ''))
print(n,len(c)); print(' '.join(out).replace('+ ','')); print(sorted(c.items(),key=lambda x:-x[1]))
