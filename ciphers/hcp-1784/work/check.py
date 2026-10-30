import re,hashlib,collections,random,math,sys
b='ciphers/hcp-1784/'
for f,h in [('source/address-large.jpg','8ce2a584aaa68694546aff1967908243461f7304cde0648a0c0cbc7d7d271363'),('source/picture-large.jpg','4cc21c76558911a9c43f5dffa7060963fc6815d7e041ab207d52fc61c83ca1a1')]:
    assert hashlib.sha256(open(b+f,'rb').read()).hexdigest()==h,f
lines=[l.split('[')[0] for l in open(b+'work/transcription.txt') if l[0] not in '#-']
s=''.join(re.findall('[A-Z]',''.join(lines)))
print(len(s),s); print(collections.Counter(s).most_common())
# trigram model from the system word list, then random-restart hill climb over all substitutions
tri=collections.Counter()
for w in open('/usr/share/dict/words'):
    w=w.strip().upper()
    if w.isalpha() and len(w)<9:
        for i in range(len(w)-2): tri[w[i:i+3]]+=1
T=sum(tri.values())
sc=lambda t:sum(math.log((tri[t[i:i+3]]+.1)/T) for i in range(len(t)-2))
A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'; random.seed(1); seen={}
for r in range(40):
    k=list(A); random.shuffle(k); d=lambda k:''.join(k[ord(c)-65] for c in s); best=sc(d(k))
    imp=True
    while imp:
        imp=False
        for i in range(26):
            for j in range(i):
                k[i],k[j]=k[j],k[i]; v=sc(d(k))
                if v>best: best=v; imp=True
                else: k[i],k[j]=k[j],k[i]
    seen[d(k)]=best
top=sorted(seen.items(),key=lambda x:-x[1])[:5]
print('best substitution fits (distinct:',len(seen),'of 40 restarts):')
for t,v in top: print(round(v,1),t)
