from pathlib import Path
import json,random,string,subprocess,time,hashlib,concurrent.futures,unicodedata
P=Path(__file__).resolve().parent;ROOT=P.parents[1];M=ROOT/'ciphers/hcp-350/work'
models={n:dict((g,float(v)) for g,v in (line.split() for line in (M/f'ring-{n}grams.tsv').read_text().splitlines())) for n in [4,5]}
def enc(p,s,r,k):
 a={c:i for i,c in enumerate(s)}
 return ''.join('?' if c=='?' else (chr(97+(a[c]+r[i%len(r)])%26) if k==1 else s[(ord(c)-97+r[i%len(r)])%26]) for i,c in enumerate(p))
def dec(ct,s,r,k):
 a={c:i for i,c in enumerate(s)}
 return ''.join('?' if c=='?' else (s[(ord(c)-97-r[i%len(r)])%26] if k==1 else chr(97+(a[c]-r[i%len(r)])%26)) for i,c in enumerate(ct))
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
for k in [1,2]:
 for T in [3,9,15]:
  folder=P/f'control-Q{k}-T{T}';folder.mkdir(exist_ok=True);rng=random.Random(334120061+k*100+T);w,s=rng.choice(eligible);r=[rng.randrange(1,26) for _ in range(T)];offset=100+k*300+T*7;p=''.join(held[offset:])[:150];full=enc(p,s,r,k);ct=''.join('?' if i in [70,94] else c for i,c in enumerate(full));fixture=dict(keyword=w,slots=s,shifts=r,plaintext=p,full_ciphertext=full,ciphertext=ct,seed=334120061+k*100+T,heldout_offset=offset,split=bound);(folder/'planted.json').write_text(json.dumps(fixture,indent=2))
  # Complete forward maps and inverse, every symbol/phase, before blind search.
  assert dec(full,s,r,k)==p
  for rr in r:
   mapped=enc(string.ascii_lowercase,s,[rr],k);assert len(set(mapped))==26 and dec(mapped,s,[rr],k)==string.ascii_lowercase
  result=search(folder,ct,T,k);chosen=result;expected=''.join('?' if i in [70,94] else c for i,c in enumerate(p));result.update(matches=sum(x==y for x,y in zip(chosen['plaintext'],expected) if y!='?'),full_maps_equal=all(enc(string.ascii_lowercase,chosen['slots'],[chosen['shifts'][i]],k)==enc(string.ascii_lowercase,s,[r[i]],k) for i in range(T)),fixture=fixture,truth_used_for_search=False);(folder/'result.json').write_text(json.dumps(result,indent=2));print('CONTROL',k,T,result['matches'],result['full_maps_equal'],result['keyword'],flush=True)
# Only independently passing period/type controls open target branches.
groups=(ROOT/'ciphers/hcp-334/work/transcription.txt').read_text().split();assert groups[14]=='?DZQR' and groups[18]=='FWXX?';sourcepaths=[ROOT/'ciphers/hcp-334/work/transcription.txt',ROOT/'ciphers/hcp-334/source/cryptogram.jpg'];hashes={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in sourcepaths}
items=[]
for k in [1,2]:
 for T in [3,9,15]:
  gate=json.loads((P/f'control-Q{k}-T{T}/result.json').read_text())
  if gate['matches']==148 and gate['full_maps_equal']:items += [(k,T,gap) for gap in range(5)]
def target(item):
 k,T,gap=item;g=groups.copy();g[18]='FWXX'[:gap]+'?'+'FWXX'[gap:];ct=''.join(g).lower();assert len(ct)==150 and ct.count('?')==2 and ct.count('w')==1;folder=P/'targets'/f'Q{k}-T{T}-gap{gap}';r=search(folder,ct,T,k);r.update(gap=gap,ciphertext=ct,conditional=True);(folder/'result.json').write_text(json.dumps(r,indent=2));print('TARGET',k,T,gap,r['score'],r['keyword'],r['plaintext'],flush=True);return {key:v for key,v in r.items() if key!='stages'}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(target,items))
assert hashes=={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in sourcepaths}
(P/'target-summary.json').write_text(json.dumps(results,indent=2));(P/'manifest.json').write_text(json.dumps(dict(source_hashes=hashes,corpus_hash=hashlib.sha256(corpus.read_bytes()).hexdigest(),dictionary_hash=hashlib.sha256((P/'alphabets.tsv').read_bytes()).hexdigest(),dictionary_count=len(alph),split=bound,frozen_model_hashes={str(n):hashlib.sha256((M/f'ring-{n}grams.tsv').read_bytes()).hexdigest() for n in [4,5]},all_absolute_shifts_free=True,selection='highest frozen 5gram after identical all-dictionary screen/top128 4gram refinement/top64 5gram refinement',ACA_example_checks=True),indent=2))
