from pathlib import Path
from collections import Counter
import json,random,unicodedata,subprocess,time,hashlib
P=Path(__file__).resolve().parent;R=P.parents[1];M=R/'ciphers/hcp-350/work';steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9];log=P/'results.jsonl'
def markers():
 return {str(n):sorted(x.name for x in (R/f'ciphers/hcp-{n}').iterdir() if x.name=='FINAL' or x.name.startswith(('DONE','REVIEWED'))) for n in [350,351,334]}
def save(r):
 r['marker_scan']=markers()
 with log.open('a') as f:f.write(json.dumps(r)+'\n')
 print(r['label'],r.get('phase'),r['language_score'],r.get('exact_plaintext'),r['seconds'],flush=True)
def encrypt(plain,slots,O,phase,sign):
 I={letter:i for i,letter in enumerate(slots)};oi={pos:c for c,pos in enumerate(O)};d=0;ct=[]
 for i,c in enumerate(plain):ct.append(chr(97+oi[(I[ord(c)-97]+d)%26]));d=(d+sign*steps[(phase+i)%17])%26
 return ''.join(ct)
def reflected(slots,O):return [slots[(-i)%26] for i in range(26)],[(-x)%26 for x in O]
def parse(text):
 lines=text.splitlines();return dict(language_score=float(lines[0].split()[0]),plaintext=lines[0].split()[1],input_slots=[int(x) for x in lines[1].split(',') if x],output_positions=[int(x) for x in lines[2].split(',') if x])
def verify(r,ct,phase):
 assert encrypt(r['plaintext'],r['input_slots'],r['output_positions'],phase,1)==ct;r['independent_reencryption_exact']=True
 I={letter:i for i,letter in enumerate(r['input_slots'])};d=0;plain=[]
 for i,c in enumerate(ct):plain.append(chr(97+r['input_slots'][(r['output_positions'][ord(c)-97]-d)%26]));d=(d+steps[(phase+i)%17])%26
 assert ''.join(plain)==r['plaintext'];r['independent_inverse_exact']=True

def pipeline(label,ct,phase,truth=None,plant=None):
 prior=[json.loads(x) for x in log.read_text().splitlines()] if log.exists() else []
 if any(x['label']==label and x['phase']==phase for x in prior):return
 folder=P/label/f'phase{phase}';folder.mkdir(parents=True,exist_ok=True);file=folder/'cipher.txt';file.write_text(ct+'\n');start=time.monotonic()
 def command(binary,args,out):
  path=folder/out
  if not path.exists():
   (P/'state.json').write_text(json.dumps(dict(label=label,phase=phase,stage=binary,started_unix=time.time(),marker_scan=markers()))+'\n')
   with path.with_suffix('.partial').open('w') as f:subprocess.run([str(P/'ring_profile') if binary=='ring_profile' else str(P/'ring_profile_masc') if binary=='ring_ic_masc_batch' else str(R/'batches/kryha-framing-sol61'/binary)]+list(map(str,args)),stdout=f,check=True)
   path.with_suffix('.partial').rename(path)
  return path.read_text()
 ic=command('ring_profile',[file,phase,1,3000,M/'ring-unigrams.tsv'],'ic.txt');batch=command('ring_ic_masc_batch',[M,file,phase,1,folder/'ic.txt'],'masc-batch.txt');lines=batch.splitlines();assert len(lines)==4*len(ic.splitlines());rows=[]
 for j,line in enumerate(ic.splitlines()):
  assert int(lines[4*j].split()[0])==j;r=parse('\n'.join(lines[4*j+1:4*j+4]));r.update(ic_candidate_index=j,profile_score=float(line.split()[0]));verify(r,ct,phase);rows.append(r)
 rows.sort(key=lambda x:x['language_score'],reverse=True);(folder/'language-reranked.json').write_text(json.dumps(rows,indent=2)+'\n');top=rows[0];seed=folder/'seed.txt';seed.write_text(' '.join(map(str,top['input_slots']+top['output_positions']))+'\n');r=parse(command('ring_ic_refine',[M,file,phase,1,seed],'refine.txt'));verify(r,ct,phase);r.update(label=label,length=len(ct),phase=phase,search_sign=1,seconds=time.monotonic()-start,candidate_count=len(rows),language_seed_rank=0,ic_candidate_index=top['ic_candidate_index'],masc_score=top['language_score'],framing_is_hypothesis=truth is None)
 if truth is not None:
  r.update(exact_plaintext=r['plaintext']==truth,matching_letters=sum(a==b for a,b in zip(r['plaintext'],truth)),planted=plant,truth_used_for_selection=False)
  trueO=plant['reflected_output_positions'] if plant['sign']==-1 else plant['output_positions'];d=0;counts=Counter()
  for i,c in enumerate(ct):counts[(trueO[ord(c)-97]-d)%26]+=1;d=(d+steps[(phase+i)%17])%26
  true=sum(v*v for v in counts.values());rng=random.Random(35073026+len(ct)+phase);null=[]
  for _ in range(10000):
   O=list(range(26));rng.shuffle(O);d=0;counts=Counter()
   for i,c in enumerate(ct):counts[(O[ord(c)-97]-d)%26]+=1;d=(d+steps[(phase+i)%17])%26
   null.append(sum(v*v for v in counts.values()))
  r['ic_calibration']=dict(true_concentration=true,null_count=10000,null_min=min(null),null_max=max(null),null_mean=sum(null)/len(null),null_at_least_true=sum(x>=true for x in null),optimized_profile_min=min(x['profile_score'] for x in rows),optimized_profile_max=max(x['profile_score'] for x in rows))
 (folder/'result.json').write_text(json.dumps(r,indent=2)+'\n');save(r)
digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
def prepare(tokens):
 out=[]
 for word,pos in tokens:
  s=''.join(digits[int(c)] if c.isdigit() and c.isascii() else c for c in word);s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
  if s:out.append('q'+s+'q' if pos=='PROPN' else s)
 return ''.join(out)+'x'
sentences=[];words=[];corpus=R/'ciphers/hcp-393/work/sk_snk-ud-train.conllu'
for line in corpus.read_text().splitlines()+['']:
 if not line:
  if words:sentences.append(words);words=[]
 elif not line.startswith('#'):
  f=line.split('\t')
  if f[0].isdigit():words.append((f[1],f[3]))
bound=int(.8*len(sentences));heldout=[prepare(s) for s in sentences[bound:]]
for n,sign,offset,phase in [(385,1,500,7),(365,-1,650,12)]:
 plain=''.join(heldout[offset:])[:n];rng=random.Random(35199100+n+offset);slots=rng.sample(range(26),26);O=rng.sample(range(26),26);rs,ro=reflected(slots,O);ct=encrypt(plain,slots,O,phase,sign);plant=dict(input_slots=slots,output_positions=O,reflected_input_slots=rs,reflected_output_positions=ro,phase=phase,sign=sign,heldout_sentence_offset=offset,plaintext=plain,ciphertext=ct,training_sentence_boundary=bound)
 folder=P/f'fresh{n}-sign{sign}'/f'phase{phase}';folder.mkdir(parents=True,exist_ok=True);(folder/'plant.json').write_text(json.dumps(plant,indent=2)+'\n')
 pipeline(f'fresh{n}-sign{sign}',ct,phase,plain,plant)
(P/'state.json').write_text(json.dumps(dict(stage='complete',marker_scan=markers()))+'\n')
