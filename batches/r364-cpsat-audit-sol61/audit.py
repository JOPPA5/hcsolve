from pathlib import Path
import sys,json,itertools,random,time,importlib.util,hashlib
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent;R=P.parents[1];code=R/'batches/r364-cpsat-main/solve.py';spec=importlib.util.spec_from_file_location('independent_cp_model',code);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
# Independent explicit position-map codec (no imported encoder/decoder).
def stage_map(n,key):return [row*len(key)+col for col in key for row in range((n-col+len(key)-1)//len(key))]
def encrypt(plain,keys):
 for k in keys:plain=''.join(plain[i] for i in stage_map(len(plain),k))
 return plain
def decrypt(cipher,keys):
 for k in reversed(keys):
  out=['']*len(cipher)
  for i,c in zip(stage_map(len(cipher),k),cipher):out[i]=c
  cipher=''.join(out)
 return cipher
def maps(n,widths,alignments):
 options=[]
 for j,w in enumerate(widths):options.append([k for k in itertools.permutations(range(w)) if alignments is None or k.index(0)+1==alignments[j]])
 for keys in itertools.product(*options):
  mapping=list(range(n))
  for key in keys:mapping=[mapping[i] for i in stage_map(n,key)]
  yield keys,mapping

def exhaust(plain,cipher,allmaps,budget):
 minimum=len(cipher)+1;count=0;sample=None
 for keys,mapping in allmaps:
  predicted=''.join(plain[i] if plain[i]!='?' else cipher[j] for j,i in enumerate(mapping));distance=sum(a!=b for a,b in zip(predicted,cipher));minimum=min(minimum,distance)
  # One unknown filler is independently optimized exactly: it appears once under a permutation.
  if distance<=budget:count+=1;sample=sample or dict(keys=keys,predicted_ciphertext=predicted,conditional_plaintext=decrypt(predicted,keys))
 return dict(minimum_mismatches=minimum,satisfying_keysets=count,witness=sample,enumerated_keysets=len(allmaps))
results=[];started=time.monotonic();rng=random.Random(364915061);initial_hash=hashlib.sha256(code.read_bytes()).hexdigest()
for widths,n in [([2,3,4],7),([3,4,5],11)]:
 schemes=[('unaligned',None)]+[(f'constant{rank}',[rank]*3) for rank in range(1,min(widths)+1)]+[(f'progressive{rank}',[rank+j for j in range(3)]) for rank in range(1,min(w-j for j,w in enumerate(widths))+1)]
 for label,alignments in schemes:
  allmaps=list(maps(n,widths,alignments))
  for kind,plain in [('unique','abcdefghijk'[:n]),('repeated','abacabadaba'[:n])]:
   keys=list(rng.choice(allmaps)[0]);ct=encrypt(plain,keys);unknown=n//2;template=plain[:unknown]+'?'+plain[unknown+1:];position=next(i for i,x in enumerate(dict((tuple(k),m) for k,m in allmaps)[tuple(keys)]) if x==unknown);damaged=ct[:1]+'z'+ct[2:];unknown_damage=ct[:position]+'z'+ct[position+1:];shuffle=list(ct);rng.shuffle(shuffle);shuffle=''.join(shuffle)
   cases=[('planted0',plain,ct,0),('damage0',plain,damaged,0),('damage1',plain,damaged,1),('filler0',template,ct,0),('filler_changed0',template,unknown_damage,0),('shuffled0',plain,shuffle,0),('shuffled1',plain,shuffle,1),('filler_shuffled0',template,shuffle,0),('filler_shuffled1',template,shuffle,1)]
   for test,p,c,errors in cases:
    exact=exhaust(p,c,allmaps,errors);cp=module.solve(p,c,widths,seconds=3,errors=errors,alignments=alignments);expected=exact['satisfying_keysets']>0;actual=cp['status'] in ['OPTIMAL','FEASIBLE'];assert cp['status'] in ['OPTIMAL','FEASIBLE','INFEASIBLE'],cp
    if expected!=actual:
     r=dict(widths=widths,alignment=label,kind=kind,test=test,plain=p,cipher=c,errors=errors,enumeration=exact,cp=cp,agreement=False);(P/'BUG.json').write_text(json.dumps(r,indent=2)+'\n');raise AssertionError(r)
    if actual:
     witness=cp['conditional_plaintext'];ks=cp['keys'];prediction=encrypt(witness,ks);assert prediction==cp['predicted_ciphertext'];assert decrypt(prediction,ks)==witness;assert sum(a!=b for a,b in zip(prediction,c))<=errors;assert all(a=='?' or a==b for a,b in zip(p,witness));assert not alignments or all(k.index(0)+1==a for k,a in zip(ks,alignments));assert any(tuple(map(tuple,ks))==tuple(k) for k,m in allmaps)
    r=dict(widths=widths,alignment=label,alignment_ranks=alignments,kind=kind,test=test,plain=p,cipher=c,errors=errors,enumeration=exact,cp=cp,agreement=True,independent_witness_verification=actual);results.append(r)
    with (P/'results.jsonl').open('a') as f:f.write(json.dumps(r)+'\n')
  print(widths,label,'complete',len(results),flush=True)
assert hashlib.sha256(code.read_bytes()).hexdigest()==initial_hash
summary=dict(cases=len(results),all_agree=True,sat=sum(r['enumeration']['satisfying_keysets']>0 for r in results),unsat=sum(r['enumeration']['satisfying_keysets']==0 for r in results),enumerated_keysets_total=sum(r['enumeration']['enumerated_keysets'] for r in results),seconds=time.monotonic()-started,model_sha256=initial_hash,model_file=str(code),model_unchanged=True,ortools_version=module.ortools.__version__,no_actual364_solver=True,no_truthseed_or_knownkeys_for_cp=True)
(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(summary,flush=True)
