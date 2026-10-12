from pathlib import Path
import json,sys,time,random
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model
B=Path(__file__).resolve().parent

def enc(p,k):return ''.join(p[i]for col in k for i in range(col,len(p),17))
def solve(p,c,seconds=30,known=None,condition_align=True):
 assert len(p)==len(c)==50;m=cp_model.CpModel();maps=[];keys=[];ranksets=[]
 if condition_align:
  n=m.new_int_var(1,17,'n');d=m.new_bool_var('progressive');m.add(n+2*d<=17)
 for stage in range(3):
  ranks=[m.new_int_var(0,16,f'rank{stage}_{j}')for j in range(17)];key=[m.new_int_var(0,16,f'key{stage}_{j}')for j in range(17)];m.add_inverse(key,ranks);keys.append(key);ranksets.append(ranks);starts=[]
  for col in range(17):
   after=m.new_bool_var(f'aftershort{stage}_{col}');m.add(ranks[col]>ranks[16]).only_enforce_if(after);m.add(ranks[col]<=ranks[16]).only_enforce_if(after.Not());start=m.new_int_var(0,48 if col==16 else 47,f'start{stage}_{col}');m.add(start==3*ranks[col]-after);starts.append(start)
  mapping=[starts[i%17]+i//17 for i in range(50)];m.add_all_different(mapping);maps.append(mapping)
  if condition_align:m.add(ranks[0]==n-1+stage*d)
  if known:
   for j,col in enumerate(known[stage]):m.add(key[j]==col)
 mid=[];final=[]
 for i,ch in enumerate(p):
  v=m.new_int_var(0,49,f'mid{i}');m.add_element(maps[0][i],maps[1],v);mid.append(v);f=m.new_int_var_from_domain(cp_model.Domain.from_values([j for j,a in enumerate(c)if a==ch]),f'final{i}');m.add_element(v,maps[2],f);final.append(f)
 m.add_all_different(mid);m.add_all_different(final)
 # Exact residue-band invariant for one short column: input row is
 # (destination + [destination >= 3*shortRank+2]) modulo 3.
 rows=[]
 for stage in range(3):
  rr=[];cut=3*ranksets[stage][16]+2
  for i in range(50):
   src=i if stage==0 else maps[0][i] if stage==1 else mid[i];dst=maps[0][i] if stage==0 else mid[i] if stage==1 else final[i]
   row=m.new_int_var(0,2,f'row{stage}_{i}');m.add_division_equality(row,src,17);aft=m.new_bool_var(f'aftcut{stage}_{i}');m.add(dst>=cut).only_enforce_if(aft);m.add(dst<cut).only_enforce_if(aft.Not());m.add_modulo_equality(row,dst+aft,3);rr.append(row)
  rows.append(rr)
 for ch in sorted(set(p)):
  inds=[i for i,a in enumerate(p)if a==ch]
  for row in range(3):
   bs=[]
   for i in inds:
    yes=m.new_bool_var(f'inrow{ch}_{row}_{i}');m.add(rows[2][i]==row).only_enforce_if(yes);m.add(rows[2][i]!=row).only_enforce_if(yes.Not());bs.append(yes)
   count=m.new_int_var(0,len(inds),f'count{ch}_{row}');m.add_element(ranksets[2][16],[sum(a==ch and (j+int(j>=3*s+2))%3==row for j,a in enumerate(c))for s in range(17)],count);m.add(sum(bs)==count)
 assert not m.validate(),m.validate();s=cp_model.CpSolver();s.parameters.num_search_workers=4;s.parameters.max_time_in_seconds=seconds;s.parameters.random_seed=396171712;t=time.monotonic();status=s.solve(m);out=dict(status=s.status_name(status),seconds=time.monotonic()-t,widths=[17]*3,alignment_unknown_constant_or_progressive=condition_align,known_key_check=known is not None,branches=s.num_branches,conflicts=s.num_conflicts)
 if status in [cp_model.OPTIMAL,cp_model.FEASIBLE]:
  ks=[[s.value(x)for x in k]for k in keys];x=p
  for k in ks:x=enc(x,k)
  assert x==c;y=c
  for k in ks[::-1]:
   a=['']*50;at=0
   for col in k:
    for i in range(col,50,17):a[i]=y[at];at+=1
   y=''.join(a)
  assert y==p;out.update(keys=ks,p=p,c=c,full50_reencryption_exact=True,full50_inverse_exact=True)
  if condition_align:out.update(n=s.value(n),progressive=s.value(d))
 return out
if __name__=='__main__':
 controls=json.loads((B/'equal17-control-truth.json').read_text())
 for tr in controls:
  hard=solve(tr['p'],tr['c'],5,known=tr['keys']);assert hard['status']in ['FEASIBLE','OPTIMAL'];(B/f"residue17-known-{tr['label']}.json").write_text(json.dumps(hard,indent=2)+'\n');r=solve(tr['p'],tr['c'],30);(B/f"residue17-blind-{tr['label']}.json").write_text(json.dumps(r,indent=2)+'\n');print(tr['label'],r['status'],r['seconds'],flush=True)
