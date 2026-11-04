import sys,re,collections
alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ"
key={i+2:c for i,c in enumerate(alpha)}
txt=open(sys.argv[1]).read()
cnt=collections.Counter(); n=0
for line in txt.splitlines():
    line=re.sub(r'\[[^\]]*\]','',line)
    words=[]
    for w in re.split(r'\s+-\s+|\s-$|-\s*$|\s+',line):
        nums=re.findall(r'\d+',w)
        if not nums: 
            if '!' in w: words.append('!')
            continue
        s=''
        for x in nums:
            v=int(x); n+=1; cnt[v]+=1; s+=key.get(v,'?')
        words.append(s)
    print(' '.join(words))
print('total numbers',n, sorted(cnt.items()))
