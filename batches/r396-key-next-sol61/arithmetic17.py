from pathlib import Path
import json,sys,time
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model
B=Path(__file__).resolve().parent

def enc(p,k):return ''.join(p[i]for col in k for i in range(col,len(p),17))
def solve(p,c,seconds=30,known=None):
 assert len(p)==len(c)==50;m=cp_model.CpModel();n=m.new_int_var(1,17,'n');d=m.new_bool_var('progressive');m.add(n+2*d<=17);ranksets=[];keys=[];afters=[]
 for stage in range(3):
  ranks=[m.new_int_var(0,16,f'rank{stage}_{j}')for j in range(17)];key=[m.new_int_var(0,16,f'key{stage}_{j}')for j in range(17)];m.add_inverse(key,ranks);ranksets.append(ranks);keys.append(key);offset=[]
  for col in range(17):
   af=m.new_bool_var(f'after{stage}_{col}');m.add(ranks[col]>ranks[16]).only_enforce_if(af);m.add(ranks[col]<=ranks[16]).only_enforce_if(af.Not());offset.append(af)
  afters.append(offset);m.add(ranks[0]==n-1+stage*d)
  if known:
   for rank,col in enumerate(known[stage]):m.add(key[rank]==col)
 positions=[[i for i in range(50)]];rows=[]
 for stage in range(3):
  dsts=[];rrows=[];cut=3*ranksets[stage][16]+2
  for i,ch in enumerate(p):
   src=positions[stage][i]
   if stage==0:col=i%17;row=i//17;rank=ranksets[stage][col];aft=afters[stage][col]
   else:
    col=m.new_int_var(0,16,f'col{stage}_{i}');row=m.new_int_var(0,2,f'row{stage}_{i}');rank=m.new_int_var(0,16,f'exrank{stage}_{i}');aft=m.new_bool_var(f'exaft{stage}_{i}');m.add_modulo_equality(col,src,17);m.add_division_equality(row,src,17);m.add_element(col,ranksets[stage],rank);m.add_element(col,afters[stage],aft)
   dst=m.new_int_var_from_domain(cp_model.Domain.from_values([j for j,x in enumerate(c)if x==ch]),f'dst{stage}_{i}')if stage==2 else m.new_int_var(0,49,f'dst{stage}_{i}');m.add(dst==3*rank+row-aft)
   m.add(dst>=cut).only_enforce_if(aft);m.add(dst<cut).only_enforce_if(aft.Not());m.add_modulo_equality(row,dst+aft,3);m.add_division_equality(rank,dst+aft,3);dsts.append(dst);rrows.append(row)
  m.add_all_different(dsts);positions.append(dsts);rows.append(rrows)
 for ch in sorted(set(p)):
  inds=[i for i,x in enumerate(p)if x==ch]
  for row in range(3):
   bs=[]
   for i in inds:
    b=m.new_bool_var(f'cnt{ch}{row}_{i}');m.add(rows[2][i]==row).only_enforce_if(b);m.add(rows[2][i]!=row).only_enforce_if(b.Not());bs.append(b)
   cnt=m.new_int_var(0,len(inds),f'count{ch}{row}');m.add_element(ranksets[2][16],[sum(x==ch and(j+int(j>=3*s+2))%3==row for j,x in enumerate(c))for s in range(17)],cnt);m.add(sum(bs)==cnt)
 assert not m.validate(),m.validate();s=cp_model.CpSolver();s.parameters.num_search_workers=4;s.parameters.max_time_in_seconds=seconds;s.parameters.random_seed=396171713;t=time.monotonic();status=s.solve(m);out=dict(status=s.status_name(status),seconds=time.monotonic()-t,widths=[17]*3,alignment_unknown_constant_or_progressive=True,known_key_check=known is not None,branches=s.num_branches,conflicts=s.num_conflicts)
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
 controls=json.loads((B/'equal17-control-truth.json').read_text())
 for tr in controls:
  hard=solve(tr['p'],tr['c'],5,known=tr['keys']);assert hard['status']in ['FEASIBLE','OPTIMAL'];(B/f"arithmetic17-known-{tr['label']}.json").write_text(json.dumps(hard,indent=2)+'\n');r=solve(tr['p'],tr['c'],30);(B/f"arithmetic17-blind-{tr['label']}.json").write_text(json.dumps(r,indent=2)+'\n');print(tr['label'],r['status'],r['seconds'],flush=True)
