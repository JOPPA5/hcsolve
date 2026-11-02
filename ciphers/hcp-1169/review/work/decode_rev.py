# independent reviewer decoder: own key typed from hcp-1174 table plus the four card-specific values
import re,collections,sys
key=dict(x.split('=') for x in """0=o 0,=ö 1=i 1.=a 1:=e 1'=á :1=ü 1,=b 2,=cs 2.=é 3=d 3,=r 3.=v 4=f 4,=g 4.=gy 5=h 5,=l 5.=ly 6=j 6,=n 7=k 7,=s 7.=sz 8=m 8,=t 9=p 9,=z""".split())
out=[];c=collections.Counter();un=[]
for l in open('../../work/transcription.txt',encoding='utf-8'):
    if l[0]=='#':continue
    l=re.sub(r'\{.*?\}',' ',l)
    s=''
    for t in l.split():
        if t in '/-': s+=' ' if t=='/' else ''; continue
        c[t]+=1
        b=t.rstrip('~')
        s+=key[b] if b in key else '?'
        if t!=b: un.append(t)
    out.append(s)
print('\n'.join(out));print(sum(c.values()),len(c),un);print(sorted(c.items(),key=lambda x:-x[1]))
