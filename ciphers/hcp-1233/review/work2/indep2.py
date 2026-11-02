# Independent decode: own token->letter table, written from the HCP1216 legend, not imported from decode.py
import re,sys
tab={'A':'a','6':'b','D':'d','E':'e','+':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','F':'r',')':'s','T':'t','X':'u','V':'v','Y':'y','Z':'z','CS':'cs','?':'·'}
from collections import Counter
c=Counter();out=[];br=0
for l in open('work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    r,*t=l.split();s=''
    for x in t:
        b=x.startswith('[');x=x.strip('[]');x0=x.split(':')[0]
        c[x0]+=1;br+=b
        s+=tab[x0].upper() if b else tab[x0]
    out.append(s);print(r,s)
print('tokens',sum(c.values()),'classes',len(c),'bracketed',br);print(''.join(out));print(sorted(c.items(),key=lambda k:-k[1]))
