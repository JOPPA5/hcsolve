from pathlib import Path
import sys,json,random,time,hashlib
root=Path(__file__).resolve().parents[2]; out=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'batches/kryha-knownpair373-sol61'))
from crt import expressions,z3
# Only this geometry field is used; no historical recovered rings are imported.
keypath=root/'ciphers/hcp-350/work/kryha-decipherment/key.json'
edges=json.loads(keypath.read_text())['adjacent_distances'];assert len(edges)==52 and sum(edges)==179
cases=[x for x in json.loads((root/'batches/kryha374-prefix-offset-main/unknown-cases.json').read_text())if x['m']==52]
def displacements(start,n):
 d=0;v=[]
 for i in range(n):v.append(d);d+=edges[(start+i)%52]
 return v

def solve(p,c,start,blocked=None):
 ds=displacements(start,len(p));rows=[]
 for a,b,d in zip(p,c,ds):
  r=[0]*54;r[ord(a)-97]-=1;r[26+ord(b)-97]+=1;r[52]-=1;r[53]=d;rows.append(r)
 for j in [0,26]:r=[0]*54;r[j]=1;rows.append(r)
 es=[];vs=[]
 for q in [2,13]:
  e,v=expressions(rows,53,q)
  if e is None:return {'status':'unsat','reason':'linear inconsistency','start':start}
  es.append(e);vs.append(v)
 s=z3.Solver();s.set(timeout=3000)
 for q,v in zip([2,13],vs):
  for x in v:s.add(x>=0,x<q)
 values=[a+13*((b-a)%2)for a,b in zip(es[1],es[0])]
 s.add(z3.Distinct(values[:26]),z3.Distinct(values[26:52]))
 if blocked:s.add(z3.Or([x!=v for x,v in zip(values,blocked)]))
 t=time.monotonic();r=s.check();res={'status':str(r),'start':start,'seconds':time.monotonic()-t,'nullity2':len(vs[0]),'nullity13':len(vs[1])}
 if r==z3.sat:
  md=s.model();vals=[md.eval(x).as_long()if isinstance(x,z3.ExprRef)else x for x in values]
  res.update(P=vals[:26],O=vals[26:52],beta=vals[52]);res['witness']=vals
 return res

def independently_verify(p,c,r):
 # Adjacent walk at absolute physical hole indices, independently of solver ds.
 P,O,beta=r['P'],r['O'],r['beta'];oi={v:chr(97+i)for i,v in enumerate(O)};pi={v:chr(97+i)for i,v in enumerate(P)}
 encoded=[];decoded=[];d=beta;hole=r['start']
 for a,b in zip(p,c):
  encoded.append(oi[(P[ord(a)-97]+d)%26]);decoded.append(pi[(O[ord(b)-97]-d)%26]);d+=edges[hole];hole=(hole+1)%52
 return {'reencryption_exact':''.join(encoded)==c,'inverse_exact':''.join(decoded)==p,'encoded':''.join(encoded),'decoded':''.join(decoded)}
rng=random.Random(37352621012);p=cases[0]['p'];assert len(p)==92
P=rng.sample(range(26),26);O=rng.sample(range(26),26);start=rng.randrange(52);beta=rng.randrange(26)
oi={v:chr(97+i)for i,v in enumerate(O)};d=beta;hole=start;c=''
for a in p:c+=oi[(P[ord(a)-97]+d)%26];d+=edges[hole];hole=(hole+1)%52
(out/'control-truth.json').write_text(json.dumps(dict(p=p,c=c,P=P,O=O,start=start,beta=beta),indent=2)+'\n')
control=[solve(p,c,h)for h in range(52)]
for r in control:
 if r['status']=='sat':r['independent_verification']=independently_verify(p,c,r);assert all(r['independent_verification'][k]for k in ['reencryption_exact','inverse_exact'])
(out/'control-results.json').write_text(json.dumps(control,indent=2)+'\n')
assert any(r['status']=='sat'for r in control),'no positive control: actual forbidden'
print('full92 control recovery passed; starts',[r['start']for r in control if r['status']=='sat'],flush=True)
ct=(root/'batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower();actual=[]
for case in cases:
 cc=list(ct);cc[52]=case['glyph53'];cc[89]=case['glyph90'];cc=''.join(cc)[case['offset']:case['offset']+len(case['p'])]
 results=[solve(case['p'],cc,h)for h in range(52)]
 for r in results:
  if r['status']=='sat':r['independent_verification']=independently_verify(case['p'],cc,r)
 actual.append(dict(p=case['p'],c=cc,offset=case['offset'],glyph53=case['glyph53'],glyph90=case['glyph90'],results=results))
 print('actual',case['offset'],case['glyph53'],case['glyph90'],{s:sum(r['status']==s for r in results)for s in ['sat','unsat','unknown']},flush=True)
(out/'actual-results.json').write_text(json.dumps(actual,indent=2)+'\n')
(out/'summary.json').write_text(json.dumps({'control_counts':{s:sum(r['status']==s for r in control)for s in ['sat','unsat','unknown']},'actual_counts':{s:sum(r['status']==s for case in actual for r in case['results'])for s in ['sat','unsat','unknown']},'geometry':edges,'geometry_total':sum(edges),'source_key_sha256':hashlib.sha256(keypath.read_bytes()).hexdigest()},indent=2)+'\n')
