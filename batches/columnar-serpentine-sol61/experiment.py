from pathlib import Path
import json,random,subprocess,unicodedata,concurrent.futures,hashlib
P=Path(__file__).resolve().parent;REPO=P.parents[1];MODELS=REPO/'batches/columnar-stratified'
def normalize(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower())if'a'<=c<='z')
def encrypt(s,key,up):
 out=[]
 for rank,col in enumerate(key):
  positions=list(range(col,len(s),len(key)))
  if(rank+up)%2:positions=positions[::-1]
  out.extend(s[i]for i in positions)
 return ''.join(out)
def inverse(ct,key,up):
 out=['']*len(ct);at=0
 for rank,col in enumerate(key):
  positions=list(range(col,len(ct),len(key)))
  if(rank+up)%2:positions=positions[::-1]
  for i in positions:out[i]=ct[at];at+=1
 return ''.join(out)
def attack(name,ct,w,kind,up):
 f=P/f'{name}-up{up}-input.txt';f.write_text(ct+'\n');proc=subprocess.run([str(P/kind),str(MODELS),str(f),str(w),'10000',str(up)],text=True,capture_output=True,timeout=180);assert proc.returncode==0,proc.stderr
 (P/f'{name}-up{up}-result.txt').write_text(proc.stdout);candidates=[]
 for line in proc.stdout.splitlines():
  sc,k,plain=line.split();seq=[int(x)for x in k.rstrip(',').split(',')];read=[seq.index(i)for i in range(w)];assert encrypt(plain,read,up)==ct;assert inverse(ct,read,up)==plain
  candidates.append(dict(score=float(sc),chunk_order=seq,readout_columns=read,readout_directions=['up'if(i+up)%2 else'down'for i in range(w)],start_up=up,plaintext=plain))
 candidates.sort(key=lambda c:c['score'],reverse=True);return candidates

def controls():
 test=REPO/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';train=REPO/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';training={l[9:]for l in train.read_text().splitlines()if l.startswith('# text = ')};sentences=[l[9:]for l in test.read_text().splitlines()if l.startswith('# text = ')and l[9:]not in training];rows=[]
 for j,(length,w,kind)in enumerate([(85,17,'beam'),(100,20,'beam'),(115,23,'beam'),(400,20,'beam'),(85,21,'one-long'),(100,11,'one-long'),(115,19,'one-long'),(400,19,'one-long')]):
  selected=[];text=''
  for s in sentences[250+70*j:]:
   selected.append(s);text+=normalize(s)
   if len(text)>=length:break
  pt=text[:length];assert len(pt)==length;rng=random.Random(61179101+j);key=list(range(w));rng.shuffle(key);up=j%2;ct=encrypt(pt,key,up);assert inverse(ct,key,up)==pt
  name=f'control-{length}-{w}';candidates=[]
  for u in [0,1]:candidates+=attack(name,ct,w,kind,u)
  candidates.sort(key=lambda c:c['score'],reverse=True);ranks=[i for i,c in enumerate(candidates)if c['plaintext']==pt];row=dict(length=length,width=w,model=kind,plaintext=pt,ciphertext=ct,planted_readout_columns=key,planted_start_up=up,source_sentences=selected,excluded_from_training=True,rng_seed=61179101+j,exact_best=candidates[0]['plaintext']==pt,true_ranks=ranks,all_retained_reencrypt_exact=True,candidates=candidates);rows.append(row);(P/'controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False));print('control',length,w,row['exact_best'],ranks,flush=True)
 provenance=dict(test_sha256=hashlib.sha256(test.read_bytes()).hexdigest(),train_sha256=hashlib.sha256(train.read_bytes()).hexdigest(),frozen_models={str(n):hashlib.sha256((MODELS/f'model{n}.tsv').read_bytes()).hexdigest()for n in range(2,6)},truth_never_search_input=True)
 (P/'provenance.json').write_text(json.dumps(provenance,indent=2))
if __name__=='__main__':controls()
