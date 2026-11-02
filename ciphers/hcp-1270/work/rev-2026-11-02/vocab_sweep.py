import re,glob,collections
V=collections.Counter()
for f in glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1[12]*/SOLUTION.md'):
    t=open(f,encoding='utf8').read()
    if 'olánk' not in t: continue
    for s in re.findall(r'## Hungarian.*?(?=\n## )',t,re.S):
        for w in re.findall(r"[a-záéíóöőúüű]+",s.lower()): V[w]+=1
print(len(V))
tr=str.maketrans('áéíóőúű','aeioöuü')
def n(w): return w.translate(tr).replace('ö','o').replace('ü','u').replace('ll','l').replace('tt','t').replace('ss','s').replace('kk','k').replace('nn','n')
W=collections.Counter()
for w,c in V.items(): W[n(w)]+=c
s='sohamostvazazoltonyamitmabistud'
alts={'h':'hp','d':'dn','a':'ae','i':'io','z':'zs','k':'kg','b':'bg','u':'uo','o':'oa'}
def m(seg,w):
    return len(seg)==len(w) and all(c==d or d in alts.get(c,c) for c,d in zip(seg,w))
res=[]
for i in range(len(s)):
  for j in range(i+2,min(i+13,len(s))+1):
    seg=s[i:j]
    for w,c in W.items():
      if m(seg,w): res.append((i,j,seg,w,c))
for r in sorted(res): print(r)
