from pathlib import Path
from collections import Counter
import sys,json,time,random
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
b=Path(__file__).resolve().parent

def enc(p,k):return ''.join(p[i]for col in k for i in range(col,len(p),17))
def inv(c,k):
 a=['']*50;at=0
 for col in k:
  for i in range(col,50,17):a[i]=c[at];at+=1
 return ''.join(a)
def build(p,c):
 assert len(p)==len(c)==50 and Counter(p)==Counter(c)
 s=z3.SolverFor('QF_FD');s.set(random_seed=396171762)
 ranks=[[[z3.Bool(f'r{stage}_{col}_{r}')for r in range(17)]for col in range(17)]for stage in range(3)]
 for layer in ranks:
  for bits in layer:s.add(z3.PbEq([(x,1)for x in bits],1))
  for r in range(17):s.add(z3.PbEq([(layer[col][r],1)for col in range(17)],1))
 for r in range(17):s.add(ranks[0][0][r]==ranks[1][0][r],ranks[0][0][r]==ranks[2][0][r])
 route=[];forward=[];backward=[]
 for st in range(3):
  cuts=[z3.Bool(f'cut{st}_{r}')for r in range(17)]
  for r in range(17):s.add(cuts[r]==z3.Or(ranks[st][16][:r]))
  fw=[[]for _ in range(50)];bw=[[]for _ in range(50)]
  for i in range(50):
   col,row=i%17,i//17
   for r in range(17):
    shifts=[0]if col==16 else([0]if r==0 else[1]if r==16 else[0,1])
    for sh in shifts:
     dst=3*r-sh+row
     if not 0<=dst<50:continue
     bit=z3.Bool(f'map{st}_{i}_{r}_{sh}');s.add(bit==z3.And(ranks[st][col][r],cuts[r]if sh else z3.Not(cuts[r])))
     fw[i].append((dst,bit));bw[dst].append((i,bit))
  for opts in fw+bw:s.add(z3.Or([bit for _,bit in opts]))
  forward.append(fw);backward.append(bw)
 clauses=0
 # Complete endpoint support in both directions, no intermediate character guesses.
 for i,ch in enumerate(p):
  for pos1,b0 in forward[0][i]:
   for pos2,b1 in forward[1][pos1]:
    support=[bit for dst,bit in forward[2][pos2]if c[dst]==ch];s.add(z3.Or(z3.Not(b0),z3.Not(b1),*support));clauses+=1
 for dst,ch in enumerate(c):
  for pos2,b2 in backward[2][dst]:
   for pos1,b1 in backward[1][pos2]:
    support=[bit for src,bit in backward[0][pos1]if p[src]==ch];s.add(z3.Or(z3.Not(b2),z3.Not(b1),*support));clauses+=1
 return s,ranks,clauses
if __name__=='__main__':
 p=Path('batches/repeat396-387-sol61/preferred-prepared-plaintext50.txt').read_text().strip();assert len(p)==50;rng=random.Random(396617261);n=rng.randrange(1,18);keys=[];c=p
 for _ in range(3):k=rng.sample(range(1,17),16);k.insert(n-1,0);keys.append(k);c=enc(c,k)
 (b/'control-input.json').write_text(json.dumps(dict(p=p,c=c,common_alignment_unknown=True),indent=2)+'\n');(b/'control-truth.json').write_text(json.dumps(dict(p=p,c=c,n=n,keys=keys,seed=396617261),indent=2)+'\n')
 t=time.monotonic();s,ranks,clauses=build(p,c);buildtime=time.monotonic()-t;rows=[];print('built',clauses,buildtime,flush=True)
 for r in range(17):
  s.set(timeout=3000);t=time.monotonic();status=s.check(ranks[0][0][r]);out=dict(n=r+1,status=str(status),seconds=time.monotonic()-t,timeout_ms=3000)
  if status==z3.sat:
   md=s.model();ks=[sorted(range(17),key=lambda col:next(rr for rr,bit in enumerate(layer[col])if z3.is_true(md.eval(bit))))for layer in ranks];pred=p;dec=c
   for k in ks:pred=enc(pred,k)
   for k in ks[::-1]:dec=inv(dec,k)
   assert pred==c and dec==p;out.update(keys=ks,p=p,c=c,full50_encoder_inverse_exact=True,true_key_identity_not_required=True)
  elif status==z3.unknown:out['reason']=s.reason_unknown()
  rows.append(out);(b/'control-results.json').write_text(json.dumps(dict(build_seconds=buildtime,clauses=clauses,incremental_n_assumptions=True,forward_backward_support=True,results=rows),indent=2)+'\n');print('control n',r+1,status,flush=True)
  if status==z3.sat:break
 if not any(r['status']=='sat'for r in rows):print('CONTROL GATE FAILED: no actual search',flush=True)
