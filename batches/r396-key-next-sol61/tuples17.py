from pathlib import Path
import json,sys,time
from collections import Counter
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model
B=Path(__file__).resolve().parent

def enc(p,k):return ''.join(p[i]for col in k for i in range(col,len(p),17))
def solve(p,c,seconds=30,known=None):
 assert len(p)==len(c)==50;m=cp_model.CpModel();n=m.new_int_var(1,17,'n');d=m.new_bool_var('progressive');m.add(n+2*d<=17);keys=[];ranksets=[];stages=[[ord(x)-97 for x in p]];vocab=sorted(ord(x)-97 for x in set(p));domain=cp_model.Domain.from_values(vocab)
 for stage in range(3):
  ranks=[m.new_int_var(0,16,f'rank{stage}_{j}')for j in range(17)];key=[m.new_int_var(0,16,f'key{stage}_{j}')for j in range(17)];m.add_inverse(key,ranks);keys.append(key);ranksets.append(ranks);m.add(ranks[0]==n-1+stage*d)
  if known:
   for j,col in enumerate(known[stage]):m.add(key[j]==col)
  target=[ord(x)-97 for x in c]if stage==2 else[m.new_int_var_from_domain(domain,f'char{stage}_{i}')for i in range(50)];source=stages[-1]+[0]
  if stage==2:
   tuples=[]
   for sh in range(17):
    for rr in range(17):
     if rr==sh:continue
     start=3*rr-int(rr>sh);tuples.append([sh,rr,*[ord(c[start+k])-97 for k in range(3)]])
   for col in range(16):m.add_allowed_assignments([ranks[16],ranks[col],source[col],source[17+col],source[34+col]],tuples)
   m.add_allowed_assignments([ranks[16],source[16],source[33]],[[sh,ord(c[3*sh])-97,ord(c[3*sh+1])-97]for sh in range(17)])
   stages.append(target);continue
  for j in range(50):
   after=m.new_bool_var(f'aftercut{stage}_{j}');m.add(j>=3*ranks[16]+2).only_enforce_if(after);m.add(j<3*ranks[16]+2).only_enforce_if(after.Not())
   vals=[]
   for shift in [0,1]:
    rank,row=divmod(j+shift,3);v=m.new_int_var(0,25,f'piece{stage}_{j}_{shift}');m.add_element(key[rank],source[row*17:(row+1)*17],v);vals.append(v)
   m.add(target[j]==vals[0]).only_enforce_if(after.Not());m.add(target[j]==vals[1]).only_enforce_if(after)
  stages.append(target)
 # Counts are redundant but expose whole-symbol propagation to the SAT core.
 for stage,cells in enumerate(stages[1:-1]):
  for ch,count in Counter(p).items():
   bs=[]
   for i,v in enumerate(cells):
    b=m.new_bool_var(f'count{stage}{ch}{i}');m.add(v==ord(ch)-97).only_enforce_if(b);m.add(v!=ord(ch)-97).only_enforce_if(b.Not());bs.append(b)
   m.add(sum(bs)==count)
 m.add_decision_strategy([ranksets[2][16],ranksets[1][16],ranksets[0][16]],cp_model.CHOOSE_FIRST,cp_model.SELECT_MIN_VALUE);m.add_decision_strategy(keys[2]+keys[1]+keys[0],cp_model.CHOOSE_MIN_DOMAIN_SIZE,cp_model.SELECT_MIN_VALUE)
 assert not m.validate(),m.validate();s=cp_model.CpSolver();s.parameters.search_branching=cp_model.FIXED_SEARCH;s.parameters.num_search_workers=4;s.parameters.max_time_in_seconds=seconds;s.parameters.random_seed=396171714;t=time.monotonic();status=s.solve(m);out=dict(status=s.status_name(status),seconds=time.monotonic()-t,widths=[17]*3,alignment_unknown_constant_or_progressive=True,known_key_check=known is not None,branches=s.num_branches,conflicts=s.num_conflicts)
 if status in [cp_model.OPTIMAL,cp_model.FEASIBLE]:
  ks=[[s.value(x)for x in key]for key in keys];x=p
  for k in ks:x=enc(x,k)
  assert x==c;y=c
  for k in ks[::-1]:
   a=['']*50;at=0
   for col in k:
    for i in range(col,50,17):a[i]=y[at];at+=1
   y=''.join(a)
  assert y==p;out.update(keys=ks,p=p,c=c,n=s.value(n),progressive=s.value(d),full50_reencryption_exact=True,full50_inverse_exact=True)
 return out
if __name__=='__main__':
 # Exact proof that the virtual source cell50 never participates in selected output.
 for short in range(17):
  for j in range(50):
   shift=int(j>=3*short+2);rank,row=divmod(j+shift,3);assert not(rank==short and row==2)
 controls=json.loads((B/'equal17-control-truth.json').read_text())
 for tr in controls:
  hard=solve(tr['p'],tr['c'],5,known=tr['keys']);assert hard['status']in ['FEASIBLE','OPTIMAL'];(B/f"tuples17-known-{tr['label']}.json").write_text(json.dumps(hard,indent=2)+'\n');r=solve(tr['p'],tr['c'],30);(B/f"tuples17-blind-{tr['label']}.json").write_text(json.dumps(r,indent=2)+'\n');print(tr['label'],r['status'],r['seconds'],flush=True)
