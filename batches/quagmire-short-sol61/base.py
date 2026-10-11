from pathlib import Path
import json,random,string,subprocess,time,hashlib,concurrent.futures,unicodedata
P=Path(__file__).resolve().parent;ROOT=P.parents[1];M=ROOT/'ciphers/hcp-350/work'
models={n:dict((g,float(v)) for g,v in (line.split() for line in (M/f'ring-{n}grams.tsv').read_text().splitlines())) for n in [4,5]}
def enc(p,s,r,k):
 a={c:i for i,c in enumerate(s)}
 return ''.join('?' if c=='?' else (chr(97+(a[c]+r[i%len(r)])%26) if k==1 else s[((ord(c)-97 if k==2 else a[c])+r[i%len(r)])%26]) for i,c in enumerate(p))
def dec(ct,s,r,k):
 a={c:i for i,c in enumerate(s)}
 return ''.join('?' if c=='?' else (s[(ord(c)-97-r[i%len(r)])%26] if k==1 else (chr(97+(a[c]-r[i%len(r)])%26) if k==2 else s[(a[c]-r[i%len(r)])%26])) for i,c in enumerate(ct))
def parse(file,ct,n,k):
 rows=[]
 for line in file.read_text().splitlines():
  score,w,s,rs,p=line.split();r=[int(v) for v in rs.split(',') if v];assert set(s)==set(string.ascii_lowercase) and len(s)==26
  assert dec(ct,s,r,k)==p and enc(p,s,r,k)==ct
  sc=sum(models[n].get(p[i:i+n],-n) for i in range(len(p)-n+1) if '?' not in p[i:i+n]);assert abs(sc-float(score))<.03
  rows.append(dict(score=float(score),keyword=w,slots=s,shifts=r,plaintext=p,inverse_reencryption=True))
 return rows
def search(folder,ct,T,k):
 folder.mkdir(parents=True,exist_ok=True);(folder/'cipher.txt').write_text(ct+'\n');start=time.monotonic()
 with (folder/'progress.txt').open('w') as f:subprocess.run([str(P/'search'),str(M),str(folder/'cipher.txt'),str(T),str(P/'alphabets.tsv'),str(folder/'candidates'),str(k)],stdout=f,stderr=f,check=True)
 stages={label:parse(folder/f'candidates-{label}.txt',ct,n,k) for label,n in [('screen',4),('four',4),('five',5)]}
 return dict(kind=k,period=T,**stages['five'][0],seconds=time.monotonic()-start,stages=stages)
# Independently reconstruct TEST sentences; all keywords are immutable TRAIN candidates.
corpus=ROOT/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';sentences=[];words=[];digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',''.join(digits[int(c)] if c.isascii() and c.isdigit() else c for c in s).lower()) if 'a'<=c<='z')
for l in corpus.read_text().splitlines()+['']:
 if not l:
  if words:sentences.append(words);words=[]
 elif not l.startswith('#'):
  f=l.split('\t')
  if f[0].isdigit():words.append((f[1],f[3]))
bound=int(.8*len(sentences));held=[''.join('q'+n+'q' if pos=='PROPN' else n for form,pos in s if (n:=norm(form)))+'x' for s in sentences[bound:]]
alph=[l.split() for l in (P/'alphabets.tsv').read_text().splitlines()];assert len(alph)==18098;eligible=[(w,a) for w,a in alph if len(set(w))>=7]
# Published ACA worked examples independently fix orientation and absolute offsets.
s=''.join(dict.fromkeys('springfever'+string.ascii_lowercase))
assert enc('thequa',s,[22,2,5,13,21,8],1)=='qpmgqr'
assert enc('intheq',s,[s.index(c) for c in 'flower'],2)=='jicico'
