toks=['abc','ly','xuder','comde','h','lz','kncv','pne','pnvvx','cn']
voc=set(l.split()[0] for l in open('ciphers/hcp-1500/work/tests/vocab.txt'))|{'a','i'}
txt=''.join(toks); lens=[len(t) for t in toks]
res=[]
seen=set()
for w in open('/usr/share/dict/words'):
    k=w.strip().lower()
    if not k.isalpha() or len(k)>10 or k in seen: continue
    seen.add(k)
    kk=[ord(c)-97 for c in k];L=len(kk)
    for mode in range(3):
        o=[]
        for i,c in enumerate(txt):
            x=ord(c)-97;y=kk[i%L]
            o.append(chr(((x-y) if mode==0 else (y-x) if mode==1 else (x+y))%26+97))
        s=''.join(o);p=0;sc=0;ws=[]
        for l in lens:
            ww=s[p:p+l];p+=l;ws.append(ww)
            if ww in voc: sc+=l
        if sc>=12: res.append((sc,k,mode,' '.join(ws)))
res.sort(reverse=True)
for r in res[:25]: print(r)
