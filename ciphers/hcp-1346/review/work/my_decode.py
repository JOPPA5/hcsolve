# independent decoder: keys typed by reviewer from the digit-order table, no import of solver files except transcription text
import re,collections,sys
plain=dict(zip('0123456789','MEFGHIKLNO')); dot=dict(zip('0123456789','ABCDPZRSTU'))
txt=open('ciphers/hcp-1346/work/transcription.txt').read()
ct=collections.Counter(); out=[]
for l in txt.splitlines():
    if l[:1]=='#' or not l.strip(): continue
    t,b=l.split(':'); ws=[]
    for w in b.split('|'):
        s=''
        for tok in w.split():
            m=re.fullmatch(r'(\d)(\.?)(~?)',tok); assert m,tok
            ct[m[1]+m[2]]+=1
            s+=(dot if m[2] else plain)[m[1]]
        ws.append(s)
    out.append((t,' '.join(ws)))
for o in out: print(*o)
print(sum(ct.values()),'signs',len(ct),'types'); print(sorted(ct.items(),key=lambda x:-x[1]))
s=''.join(o[1].replace(' ','') for o in out); n=len(s)
f=collections.Counter(s); print('IC',sum(v*(v-1) for v in f.values())/(n*(n-1)))
print('tilde',txt.count('~')-txt.split('\n')[1].count('~'))
