# independent decode: own key written from 1174 table + card; parses transcription, reports frequency and tokens
import re,collections,sys
K=dict(zip("0|0,|1|1.|1:|1'|:1|1,|2,|2.|3|3,|3.|4,|4.|5|5,|5.|6|6,|7|7,|7.|8|8,|8.|9|9,".split('|'),
 "o|ö|i|a|e|á|ü|b|cs|é|d|r|v|g|gy|h|l|ly|j|n|k|s|sz|m|t|ty|p|z".split('|')))
c=collections.Counter();n=0
for l in open('../../work/transcription.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip():continue
    t,b=l.split(':',1); b=re.sub(r'\{.*?\}','',b); o=[]
    for w in b.split(' / '):
        s=''
        for x in w.split():
            if x[0]=='=': s+='['+x[1:]+']';continue
            x=x.split('~')[0]; n+=1;c[x]+=1; s+=K[x]
        o.append(s)
    print(t,' '.join(o))
print(n,len(c),sorted(c.items(),key=lambda a:-a[1]))
