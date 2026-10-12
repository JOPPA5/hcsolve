from pathlib import Path
import sys,time,json
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model

def enc(p,k):return ''.join(p[i]for col in k for i in range(col,len(p),len(k)))
def solve(p,c,seconds=45,hints=None,known=None):
 n=len(p);m=cp_model.CpModel();ws=[21,19,20];maps=[];allkeys=[]
 for stage,w in enumerate(ws):
  q,r=divmod(n,w);key=[m.new_int_var(0,w-1,f'key{stage}_{i}')for i in range(w)];rank=[m.new_int_var(0,w-1,f'rank{stage}_{i}')for i in range(w)];m.add_inverse(key,rank);long=[m.new_bool_var(f'long{stage}_{i}')for i in range(w)];starts=[0]
  for i in range(w):m.add_element(key[i],[int(col<r)for col in range(w)],long[i]);starts.append(m.new_int_var(0,n,f'prefix{stage}_{i+1}'));m.add(starts[-1]==starts[-2]+q+long[i])
  m.add(starts[-1]==n);colstarts=[];intervals=[]
  for col in range(w):
   st=m.new_int_var(0,n-(q+(col<r)),f'start{stage}_{col}');m.add_element(rank[col],starts[:-1],st);colstarts.append(st);intervals.append(m.new_interval_var(st,q+(col<r),st+q+(col<r),f'int{stage}_{col}'))
  m.add_no_overlap(intervals);mapping=[colstarts[i%w]+i//w for i in range(n)];m.add_all_different(mapping);maps.append(mapping);allkeys.append(key)
  if hints:
   for i,col in enumerate(hints[stage]):m.add_hint(key[i],col);m.add_hint(rank[col],i);m.add_hint(long[i],int(col<r))
   at=0
   for i,col in enumerate(hints[stage]):
    m.add_hint(colstarts[col],at);at+=q+(col<r);m.add_hint(starts[i+1],at)
  if known:
   for i,col in enumerate(known[stage]):m.add(key[i]==col)
 mid=[];final=[]
 for i,ch in enumerate(p):
  v=m.new_int_var(0,n-1,f'mid{i}');m.add_element(maps[0][i],maps[1],v);mid.append(v);f=m.new_int_var_from_domain(cp_model.Domain.from_values([j for j,a in enumerate(c)if a==ch]),f'final{i}');m.add_element(v,maps[2],f);final.append(f)
 m.add_all_different(mid);m.add_all_different(final);assert not m.validate(),m.validate();s=cp_model.CpSolver();s.parameters.num_search_workers=4;s.parameters.max_time_in_seconds=seconds;s.parameters.random_seed=396202612;t=time.monotonic();status=s.solve(m);out=dict(status=s.status_name(status),seconds=time.monotonic()-t,known_keys=known is not None,generic_hints=hints is not None,branches=s.num_branches,conflicts=s.num_conflicts)
 if status in [cp_model.OPTIMAL,cp_model.FEASIBLE]:
  keys=[[s.value(x)for x in k]for k in allkeys];x=p
  for k in keys:x=enc(x,k)
  assert x==c;y=c
  for k in keys[::-1]:
   a=['']*n;at=0
   for col in k:
    for i in range(col,n,len(k)):a[i]=y[at];at+=1
   y=''.join(a)
  assert y==p;out.update(keys=keys,plaintext=p,ciphertext=c,full50_reencryption_exact=True,full50_inverse_exact=True)
 return out
if __name__=='__main__':
 b=Path(__file__).resolve().parent;j=int(sys.argv[1]);tr=json.loads((b/'controls-truth.json').read_text())[j];hint=json.loads((b/f'cp-lns-control{j}.json').read_text())['keys'];known=solve(tr['plaintext'],tr['ciphertext'],5,known=tr['keys']);assert known['status']in ['OPTIMAL','FEASIBLE'];(b/f'rank-known{j}.json').write_text(json.dumps(known,indent=2)+'\n');r=solve(tr['plaintext'],tr['ciphertext'],45,hints=hint);(b/f'rank-control{j}.json').write_text(json.dumps(r,indent=2)+'\n');print(j,r['status'],r['seconds'],flush=True)
