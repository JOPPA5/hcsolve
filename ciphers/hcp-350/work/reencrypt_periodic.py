from pathlib import Path
import random,json,time,sys,collections
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
p=Path(__file__).resolve().parent
a=''.join((p/'transcription.txt').read_text().split()).lower()[20:375]
b=''.join((p.parents[1]/'hcp-351/work/transcription.txt').read_text().split()).lower()[20:375]
assert len(a)==len(b)==355
def shifts(n,steps):
 d=0;out=[]
 for i in range(n):out.append(d);d=(d+steps[i%len(steps)])%26
 return out
def solve(inp,out,T,budget=0,timeout=30000):
 # Periodic increments imply d_i=R[i mod T]+floor(i/T)*S mod26.
 # R[0]=0; S=sum(period increments). Every R/S assignment induces a valid periodic step array.
 s=z3.Solver();s.set(timeout=timeout)
 I=[z3.Int(f'I{i}')for i in range(26)];O=[z3.Int(f'O{i}')for i in range(26)];R=[z3.Int(f'R{i}')for i in range(T)];S=z3.Int('S')
 s.add(*[z3.And(x>=0,x<26)for x in I+O+R+[S]],z3.Distinct(I),z3.Distinct(O),I[0]==0,R[0]==0)
 errors=[z3.Bool(f'err{i}')for i in range(len(inp))]
 s.add(z3.PbLe([(x,1)for x in errors],budget))
 for i,(x,y)in enumerate(zip(inp,out)):
  s.add(z3.Or(errors[i],(O[ord(y)-97]-I[ord(x)-97]-R[i%T]-(i//T)*S)%26==0))
 at=time.monotonic();status=s.check();rec=dict(period=T,budget=budget,status=str(status),seconds=time.monotonic()-at)
 if status==z3.sat:
  m=s.model();iv=[m[x].as_long()for x in I];ov=[m[x].as_long()for x in O];rs=[m[x].as_long()for x in R];cycle=m[S].as_long();steps=[(rs[i+1]-rs[i])%26 for i in range(T-1)]+[(cycle-rs[-1])%26];d=shifts(len(inp),steps);ringout={v:chr(97+j)for j,v in enumerate(ov)};reproduced=''.join(ringout[(iv[ord(x)-97]+v)%26]for x,v in zip(inp,d));bad=[i for i,x in enumerate(errors)if z3.is_true(m[x])];actualbad=[i for i,(x,y)in enumerate(zip(reproduced,out))if x!=y]
  assert set(actualbad)<=set(bad) and len(actualbad)<=budget
  rec.update(ring_in_positions=iv,ring_out_positions=ov,steps=steps,error_positions=bad,actual_mismatch_positions=actualbad,reproduced=reproduced)
 else:
  if status==z3.unknown:rec['reason_unknown']=s.reason_unknown()
 return rec
if __name__=='__main__':
 rng=random.Random(35035152);controls=[]
 for T in (17,26,52):
  iv=list(range(26));ov=list(range(26));rng.shuffle(iv);rng.shuffle(ov);steps=[rng.randrange(26)for _ in range(T)];d=shifts(len(a),steps);ringout={v:chr(97+j)for j,v in enumerate(ov)};out=''.join(ringout[(iv[ord(x)-97]+r)%26]for x,r in zip(a,d));rec=solve(a,out,T,0,60000);rec['exact_reproduction']=rec.get('reproduced')==out;controls.append(dict(input=a,output=out,planted_ring_in=iv,planted_ring_out=ov,planted_steps=steps,result=rec));print('CONTROL',T,rec['status'],rec['seconds'],rec['exact_reproduction'],flush=True);(p/'reencrypt-periodic-controls.json').write_text(json.dumps(controls,indent=2))
  if not rec['exact_reproduction']:raise SystemExit('CONTROL GATE FAILED/INCONCLUSIVE: no target search')
 results=[]
 for T in range(1,53):
  rec=solve(a,b,T,0,30000);results.append(rec);print('TARGET',T,rec['status'],rec['seconds'],flush=True);(p/'reencrypt-periodic-target.json').write_text(json.dumps(results,indent=2))
