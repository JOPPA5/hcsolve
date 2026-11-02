import re,collections,sys
p='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1149/work/transcription.txt'
# my own key, written from the hcp-1174 table plus consonant-series logic; not imported from the solver
K={'o':'0','ö':'0,','i':'1','a':'1.','e':'1:','á':"1'",'ü':':1','b':'1,','c':'2','cs':'2,','é':'2.','d':'3','r':'3,','v':'3.','f':'4','g':'4,','gy':'4.','h':'5','l':'5,','ly':'5.','j':'6','n':'6,','ny':'6.','k':'7','s':'7,','sz':'7.','m':'8','t':'8,','p':'9','z':'9,'}
inv={v:k for k,v in K.items()}
c=collections.Counter();words=[]
for l in open(p,encoding='utf-8'):
    l=l.strip()
    if not l or l.startswith('#'):continue
    ws=[]
    for seg in l.split(' ; '):
        if seg.startswith('open:'): ws.append('['+seg[5:].strip()+']');continue
        for w in seg.split('|'):
            r=''
            for t in w.split():
                if t in '()': r+=t
                else: c[t]+=1; r+=inv[t]
            ws.append(r)
    words.append(' '.join(ws)); print(words[-1])
print(sum(c.values()),len(c)); print(sorted(c.items(),key=lambda x:x[1]))
