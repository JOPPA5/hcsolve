# independent re-encipher/decode check: my own by-eye sign reading of rows, compared with solver literal
key={'F':'r','6':'b','+':'f','H':'h','X':'u','CS':'cs',')':'s'}
import re,sys,subprocess,collections
L=[l.split() for l in open('work/ledger.txt',encoding='utf-8') if l.strip() and l[0]!='#']
c=collections.Counter()
for r in L:
    for t in r[1:]:
        t=t.strip('[]').split(':')[0]; c[t]+=1
print(sum(c.values()),sorted(c.items(),key=lambda x:-x[1]))
txt=''.join(key.get(t.strip('[]').split(':')[0],t.strip('[]').split(':')[0].lower()) for r in L for t in r[1:])
print(txt)
