import sys,re,collections
D='/Users/tomaspavuk/Desktop/hcsolve/batches/scoring-sol61/german/source/'
freq=collections.Counter()
for line in open(D+'de_gsd-ud-train.conllu',encoding='utf8'):
    p=line.split('\t')
    if len(p)>2 and p[0].isdigit(): freq[p[1].lower()]+=1
words=set(freq)
for line in open(D+'de_DE_frami.dic',encoding='latin-1'):
    w=line.split('/')[0].strip().lower()
    if w.isalpha(): words.add(w)
def pat(s): 
    m={};return tuple(m.setdefault(c,len(m)) for c in s)
def find(cipher,fixed={}):
    P=pat(cipher);out=[]
    for w in words:
        if len(w)!=len(cipher) or pat(w)!=P: continue
        if all(w[i]==v for i,v in fixed.items()): out.append(w)
    return sorted(out,key=lambda w:-freq[w])
if __name__=='__main__':
    for c in sys.argv[1:]:
        r=find(c); print(c,len(r),r[:60])
