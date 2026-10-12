from pathlib import Path
import sys,time,json
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model

def enc(p,k):return ''.join(p[i]for col in k for i in range(col,len(p),len(k)))
def solve(p,c,seconds=60,hints=None,known=None):
 n=len(p);assert n==50 and len(c)==n;model=cp_model.CpModel();ws=[21,19,20];maps=[];allstarts=[]
 for stage,w in enumerate(ws):
  q,r=divmod(n,w);starts=[];intervals=[]
  for col in range(w):
   length=q+(col<r);possible=set()
   for rank in range(w):
    longs=r-(col<r);shorts=w-r-(col>=r)
    for beforelong in range(max(0,rank-shorts),min(rank,longs)+1):
     at=q*rank+beforelong
     if at+length<=n:possible.add(at)
   st=model.new_int_var_from_domain(cp_model.Domain.from_values(sorted(possible)),f'st{stage}_{col}');starts.append(st);intervals.append(model.new_interval_var(st,length,st+length,f'interval{stage}_{col}'))
  model.add_no_overlap(intervals);mapping=[starts[i%w]+i//w for i in range(n)];model.add_all_different(mapping);maps.append(mapping);allstarts.append(starts)
  for key,hard in [(hints,False),(known,True)]:
   if key:
    at=0
    for col in key[stage]:
     if hard:model.add(starts[col]==at)
     else:model.add_hint(starts[col],at)
     at+=q+(col<r)
 # Each occurrence is traced; final occurrence domains retain the repeated-letter alternatives.
 middle=[];final=[]
 for i,ch in enumerate(p):
  v=model.new_int_var(0,n-1,f'mid{i}');model.add_element(maps[0][i],maps[1],v);middle.append(v)
  occ=[j for j,x in enumerate(c)if x==ch];f=model.new_int_var_from_domain(cp_model.Domain.from_values(occ),f'final{i}');model.add_element(v,maps[2],f);final.append(f)
 model.add_all_different(middle);model.add_all_different(final)
 assert not model.validate(),model.validate();solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=seconds;solver.parameters.num_search_workers=4;solver.parameters.random_seed=39638712;t=time.monotonic();status=solver.solve(model);r=dict(status=solver.status_name(status),seconds=time.monotonic()-t,timeout=seconds,booleans=solver.num_booleans,branches=solver.num_branches,conflicts=solver.num_conflicts,hints_from_generic_search=hints is not None,known_keys=known is not None)
 if status in [cp_model.OPTIMAL,cp_model.FEASIBLE]:
  ks=[sorted(range(w),key=lambda col:solver.value(allstarts[s][col]))for s,w in enumerate(ws)];pred=p
  for k in ks:pred=enc(pred,k)
  assert pred==c;rev=c
  for k in ks[::-1]:
   out=['']*n;at=0
   for col in k:
    for i in range(col,n,len(k)):out[i]=rev[at];at+=1
   rev=''.join(out)
  assert rev==p;r.update(keys=ks,plaintext=p,ciphertext=c,full50_reencryption_exact=True,full50_inverse_exact=True)
 return r
if __name__=='__main__':
 b=Path(__file__).resolve().parent;j=int(sys.argv[1]);tr=json.loads((b/'controls-truth.json').read_text())[j];lines=(b/f'control{j}-result.txt').read_text().splitlines();hint=[list(map(int,l.split()))for l in lines[1:4]]
 hard=solve(tr['plaintext'],tr['ciphertext'],5,known=tr['keys']);assert hard['status']in ['OPTIMAL','FEASIBLE'];(b/f'cp-known{j}.json').write_text(json.dumps(hard,indent=2)+'\n')
 r=solve(tr['plaintext'],tr['ciphertext'],45,hints=hint);(b/f'cp-control{j}.json').write_text(json.dumps(r,indent=2)+'\n');print(j,r['status'],r['seconds'],flush=True)
