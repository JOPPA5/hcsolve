from pathlib import Path
import sys,json,random,itertools,time,hashlib
import numpy as np
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'batches/kryha-knownpair373-sol61'))
from crt import expressions,z3
edges=json.loads((root/'ciphers/hcp-350/work/kryha-decipherment/key.json').read_text())['adjacent_distances'];assert len(edges)==52 and sum(edges)==179
coords=np.array([sum(edges[:i])for i in range(52)],dtype=np.int64)
profiles=[];disps=[]
for omit in itertools.combinations(range(52),2):
 selected=[h for h in range(52)if h not in omit];xy=coords[selected]
 for sr in range(50):
  js=sr+np.arange(92);d=xy[js%50]-xy[sr]+179*(js//50)
  profiles.append((omit,sr,selected[sr]));disps.append(d)
D=np.array(disps,dtype=np.int64);assert D.shape==(66300,92)
RHS=np.column_stack([D,np.zeros((66300,2),dtype=np.int64)])
def matrix(p,c):
 a=np.zeros((94,53),dtype=np.int64)
 for i,(x,y)in enumerate(zip(p,c)):a[i,ord(x)-97]-=1;a[i,26+ord(y)-97]+=1;a[i,52]-=1
 a[92,0]=1;a[93,26]=1;return a

def null_constraints(a,q):
 # Retain exact row-operation transform; its zero-coefficient rows test every RHS.
 n=a.shape[1];v=np.column_stack([a%q,np.eye(len(a),dtype=np.int64)]);at=0
 for col in range(n):
  ids=np.flatnonzero(v[at:,col]%q)
  if not len(ids):continue
  k=at+ids[0];v[[at,k]]=v[[k,at]];v[at]=(v[at]*pow(int(v[at,col]),-1,q))%q
  for j in range(len(v)):
   if j!=at and v[j,col]:v[j]=(v[j]-v[j,col]*v[at])%q
  at+=1
 return v[at:,n:],at

def solve(p,c,idx,block=None):
 a=matrix(p,c);ds=D[idx];rows=np.column_stack([a,np.append(ds,[0,0])]).tolist();es=[];vs=[]
 for q in [2,13]:
  e,v=expressions(rows,53,q)
  if e is None:return {'status':'unsat','reason':'linear inconsistency'}
  es.append(e);vs.append(v)
 s=z3.Solver();s.set(timeout=5000);values=[x+13*((y-x)%2)for x,y in zip(es[1],es[0])]
 for q,v in zip([2,13],vs):
  for x in v:s.add(x>=0,x<q)
 s.add(z3.Distinct(values[:26]),z3.Distinct(values[26:52]))
 if block:s.add(z3.Or([v!=b for v,b in zip(values,block)]))
 t=time.monotonic();r=s.check();res={'status':str(r),'seconds':time.monotonic()-t,'profile_index':idx,'omitted':profiles[idx][0],'start':profiles[idx][2]}
 if r==z3.sat:
  md=s.model();v=[md.eval(x).as_long()if isinstance(x,z3.ExprRef)else x for x in values];res.update(P=v[:26],O=v[26:52],beta=v[52],witness=v)
 if r==z3.unknown:res['reason']=s.reason_unknown()
 return res

def verify(p,c,r):
 # Walk actual adjacent edges, skipping the omitted holes, independent of coordinate RHS.
 omitted=set(r['omitted']);hole=r['start'];d=r['beta'];P=r['P'];O=r['O'];oi={v:chr(97+i)for i,v in enumerate(O)};pi={v:chr(97+i)for i,v in enumerate(P)};enc='';dec=''
 for x,y in zip(p,c):
  enc+=oi[(P[ord(x)-97]+d)%26];dec+=pi[(O[ord(y)-97]-d)%26]
  while True:
   d+=edges[hole];hole=(hole+1)%52
   if hole not in omitted:break
 return dict(reencryption_exact=enc==c,inverse_exact=dec==p,encoded=enc,decoded=dec)

def search(p,c,name):
 a=matrix(p,c);keep=np.ones(66300,dtype=bool);diag=[]
 for q in [2,13]:
  null,rank=null_constraints(a,q);consistent=np.all((RHS@null.T)%q==0,axis=1);keep&=consistent;diag.append(dict(q=q,rank=rank,left_nullity=len(null),linear_survivors=int(consistent.sum())))
 survivors=np.flatnonzero(keep).tolist();audits=[]
 rng=random.Random(5037392)
 for idx in rng.sample(range(66300),80)+survivors[:20]:
  rows=np.column_stack([a,RHS[idx]]).tolist();consistent=all(expressions(rows,53,q)[0]is not None for q in [2,13]);assert consistent==bool(keep[idx]);audits.append(dict(index=idx,linear_consistent=consistent))
 results=[]
 for idx in survivors:
  r=solve(p,c,idx)
  if r['status']=='sat':
   r['independent_verification']=verify(p,c,r);assert r['independent_verification']['reencryption_exact']and r['independent_verification']['inverse_exact'];r['second_witness']=solve(p,c,idx,r['witness'])
  results.append(r)
 output=dict(p=p,c=c,profiles=66300,linear_diagnostics=diag,combined_linear_survivors=len(survivors),audit=audits,ring_results=results)
 (out/(name+'.json')).write_text(json.dumps(output,indent=2)+'\n');print(name,'linear survivors',len(survivors),'ring counts',{s:sum(r['status']==s for r in results)for s in ['sat','unsat','unknown']},flush=True);return output
cases=[x for x in json.loads((root/'batches/kryha374-prefix-offset-main/unknown-cases.json').read_text())if x['m']==50]
p=cases[0]['p'];assert len(p)==92;rng=random.Random(3735020261012);omitted=tuple(sorted(rng.sample(range(52),2)));selected=[h for h in range(52)if h not in omitted];start=rng.choice(selected);beta=rng.randrange(26);P=rng.sample(range(26),26);O=rng.sample(range(26),26);oi={v:chr(97+i)for i,v in enumerate(O)};d=beta;hole=start;c=''
for x in p:
 c+=oi[(P[ord(x)-97]+d)%26]
 while True:
  d+=edges[hole];hole=(hole+1)%52
  if hole not in omitted:break
(out/'control-truth.json').write_text(json.dumps(dict(p=p,c=c,omitted=omitted,start=start,beta=beta,P=P,O=O),indent=2)+'\n')
control=search(p,c,'control-results');assert any(r['status']=='sat'for r in control['ring_results']),'control failed, actual forbidden'
ct=(root/'batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower();summary=[]
for k,case in enumerate(cases):
 cc=list(ct);cc[52]=case['glyph53'];cc[89]=case['glyph90'];cc=''.join(cc)[case['offset']:case['offset']+92];r=search(case['p'],cc,'actual-'+str(k));summary.append(dict(offset=case['offset'],glyph53=case['glyph53'],glyph90=case['glyph90'],linear_survivors=r['combined_linear_survivors'],ring_counts={s:sum(x['status']==s for x in r['ring_results'])for s in ['sat','unsat','unknown']}))
(out/'summary.json').write_text(json.dumps(dict(cases=summary,geometry=edges,geometry_total=sum(edges),complete_profiles_per_case=66300),indent=2)+'\n')
