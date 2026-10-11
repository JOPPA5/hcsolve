from pathlib import Path
import random,json,time,sys,collections
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
p=Path(__file__).resolve().parent
steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9]
a=''.join((p/'transcription.txt').read_text().split()).lower()[20:375]
b=''.join((p.parents[1]/'hcp-351/work/transcription.txt').read_text().split()).lower()[20:375]
assert len(a)==len(b)==355
def shifts(n,phase,direction):
 d=0;out=[]
 for i in range(n):
  out.append(d);d=(d+direction*steps[(phase+i)%17])%26
 return out
def lowerbound(inp,out,d):
 pairs=collections.defaultdict(collections.Counter)
 for x,y,s in zip(inp,out,d):pairs[(x,y)][s]+=1
 return sum(sum(c.values())-max(c.values())for c in pairs.values())
def solve(inp,out,phase,direction,budget=0,timeout=30000):
 d=shifts(len(inp),phase,direction);s=z3.Solver();s.set(timeout=timeout)
 I=[z3.Int(f'I{i}')for i in range(26)];O=[z3.Int(f'O{i}')for i in range(26)]
 s.add(*[z3.And(x>=0,x<26)for x in I+O],z3.Distinct(I),z3.Distinct(O),I[0]==0)
 errors=[z3.Bool(f'err{i}')for i in range(len(inp))]
 if budget:s.add(z3.PbLe([(x,1)for x in errors],budget))
 else:s.add(*[z3.Not(x)for x in errors])
 for i,(x,y,r)in enumerate(zip(inp,out,d)):
  diff=O[ord(y)-97]-I[ord(x)-97];s.add(z3.Or(errors[i],diff==r,diff==r-26))
 t=time.monotonic();status=s.check();record=dict(phase=phase,direction=direction,budget=budget,pair_conflict_lower_bound=lowerbound(inp,out,d),status=str(status),seconds=time.monotonic()-t)
 if status==z3.sat:
  m=s.model();iv=[m[x].as_long()for x in I];ov=[m[x].as_long()for x in O];bad=[i for i,x in enumerate(errors)if z3.is_true(m[x])];ringout={v:chr(97+j)for j,v in enumerate(ov)}
  reproduced=''.join(ringout[(iv[ord(x)-97]+r)%26]for x,r in zip(inp,d));record.update(ring_in_positions=iv,ring_out_positions=ov,error_positions=bad,reproduced=reproduced)
 return record
rng=random.Random(350351);iv=list(range(26));ov=list(range(26));rng.shuffle(iv);rng.shuffle(ov);phase=6;direction=-1;d=shifts(len(a),phase,direction);ringout={v:chr(97+j)for j,v in enumerate(ov)};control=''.join(ringout[(iv[ord(x)-97]+r)%26]for x,r in zip(a,d))
rec=solve(a,control,phase,direction);offset=iv[0];expected_i=[(x-offset)%26 for x in iv];expected_o=[(x-offset)%26 for x in ov];rec['exact_reproduction']=rec.get('reproduced')==control;rec['exact_key_up_to_rotation']=rec.get('ring_in_positions')==expected_i and rec.get('ring_out_positions')==expected_o
assert rec['status']=='sat' and rec['exact_reproduction'] and rec['exact_key_up_to_rotation'],rec
# Three independent planted output typos, explicit exact error budget.
typo=list(control)
for i in (31,167,302):typo[i]=chr((ord(typo[i])-97+11)%26+97)
typo=''.join(typo);rec3=solve(a,typo,phase,direction,3);rec3['exact_underlying_key_up_to_rotation']=rec3.get('ring_in_positions')==expected_i and rec3.get('ring_out_positions')==expected_o
assert rec3['status']=='sat' and rec3['error_positions']==[31,167,302] and rec3['exact_underlying_key_up_to_rotation'],rec3
(p/'reencrypt-control.json').write_text(json.dumps(dict(input=a,output=control,typo_output=typo,planted_ring_in=iv,planted_ring_out=ov,control=rec,three_typo_control=rec3),indent=2))
print('Control exact355/key, 3typos exact key/errorpositions PASS',flush=True)
results=[]
for phase in range(17):
 for direction in (-1,1):
  for budget in (0,3):
   r=solve(a,b,phase,direction,budget);results.append(r);print(phase,direction,budget,r['status'],r['pair_conflict_lower_bound'],flush=True)
(p/'reencrypt-target-results.json').write_text(json.dumps(results,indent=2))
