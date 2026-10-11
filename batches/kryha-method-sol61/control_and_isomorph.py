from pathlib import Path
import sys,json,random,unicodedata,math,time,hashlib
p=Path(__file__).resolve().parent;repo=p.parents[1]
g=json.loads((repo/'batches/kryha-wheel-sol61/wheel52.json').read_text());a=g['adjacent_distances'];coord=g['unwrapped_effective_coordinates']
source=repo/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';sentences=[];words=[]
for line in source.read_text().splitlines()+['']:
 if not line:
  if words:sentences.append(words);words=[]
 elif not line.startswith('#'):
  f=line.split('\t')
  if f[0].isdigit():
   w=''.join(c for c in unicodedata.normalize('NFD',f[1].lower())if 'a'<=c<='z')
   if w:words.append(w)
heldout='j'.join('j'.join(s)for s in sentences[int(.8*len(sentences)):])
rng=random.Random(17952261011);m=26;stops=sorted(rng.sample(range(1,53),m));phase=rng.randrange(m);P=list(range(26));O=list(range(26));rng.shuffle(P);rng.shuffle(O);I={v:i for i,v in enumerate(P)};inv={v:i for i,v in enumerate(O)};jumps=[]
for h,to in zip(stops,stops[1:]+stops[:1]):
 at=h;jump=0
 while True:
  jump+=a[at-1];at=at%52+1
  if at==to:break
 jumps.append(jump)
assert sum(jumps)==179
prefix=heldout[2700:2740];msgs=[];plains=[];shifts=rng.sample(range(26),9)
for r,shift in enumerate(shifts):
 plain=prefix+heldout[3400+600*r:3400+600*r+345];d=shift;j=phase;ct=[]
 for ch in plain:
  ct.append(chr(97+inv[(I[ord(ch)-97]+d)%26]));presses=2 if ch=='j'else 1
  for _ in range(presses):d=(d+jumps[j])%26;j=(j+1)%m
 ct=''.join(ct);msgs.append(ct);plains.append(plain)
 # Independent inverse based solely on fixed coordinates, not generated jumps.
 dec=[];d=shift;j=phase
 for ch in ct:
  q=P[(O[ord(ch)-97]-d)%26];dec.append(chr(97+q))
  for _ in range(2 if q==9 else 1):d=(d+(coord[stops[(j+1)%m]-1]-coord[stops[j]-1])%179)%26;j=(j+1)%m
 assert ''.join(dec)==plain
(p/'control-ciphertexts.json').write_text(json.dumps(msgs,indent=2));(p/'control-truth.json').write_text(json.dumps(dict(plaintexts=plains,output_positions=O,input_slots=P,active_holes=stops,phase=phase,initial_shifts=shifts,common_prefix_length=40,cycle=179,selective_J=True,rng_seed=17952261011,corpus_sha256=hashlib.sha256(source.read_bytes()).hexdigest()),indent=2))
# Operative solver receives only ciphertexts and proposed shared positions; neither plaintext nor mask/rings.
from isomorph_solver import solve_isomorph
report=solve_isomorph(json.loads((p/'control-ciphertexts.json').read_text()),40)
# Only post-search diagnostic uses truth; affine ring decimations are unavoidable here.
units=[u for u in range(26)if math.gcd(u,26)==1];equiv=[[u*(x-O[0])%26 for x in O]for u in units];report['expected_affine_solutions']=len(equiv);report['all_found_equivalent_diagnostic']=bool(report['rings']) and all(o in equiv for o in report['rings']);report['equivalent_found_diagnostic']=sum(o in report['rings']for o in equiv);report['control_encode_inverse_exact']=True;report['not_full_plaintext_recovery']=True
(p/'isomorph-verification.json').write_text(json.dumps(report,indent=2));print({k:v for k,v in report.items()if k!='rings'})

checks=[]
for w in [8,12,20]:
 r=solve_isomorph(msgs,w);checks.append(dict(width=w,nullity=r['nullity'],status=r['status'],rings=len(r['rings'])))
bad=list(msgs);ch=bad[1][10];bad[1]=bad[1][:10]+chr(97+(ord(ch)-97+1)%26)+bad[1][11:];r=solve_isomorph(bad,40);checks.append(dict(scope='one deliberately false shared-position pair',nullity=r['nullity'],status=r['status'],rings=len(r['rings'])))
(p/'sensitivity.json').write_text(json.dumps(checks,indent=2));print(checks)
