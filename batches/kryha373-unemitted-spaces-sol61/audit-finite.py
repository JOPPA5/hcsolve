from pathlib import Path
from itertools import product
import json,random
from model import z3
from finite import enumerate_observed
b=Path(__file__).resolve().parent;rng=random.Random(3732676);rows=[]
for case in range(20):
 observed=list(range(8))+list(range(26,34));coeff={};planted=[rng.randrange(26),rng.randrange(26)];positions={}
 for start in [0,26]:
  vals=[0]+rng.sample(range(1,26),7)
  for i in range(8):
   index=start+i;u,v=(0,0)if i==0 else(rng.randrange(26),rng.randrange(26))
   if case%3==0:v=0
   if case%3==1:v=2*(v%13)
   coeff[index]=((vals[i]-u*planted[0]-v*planted[1])%26,u,v)
 if case%2:coeff[2]=coeff[1] # independently constructed impossible injective ring
 exprs=[];variables=[]
 for q in [2,13]:
  core=[z3.Int(f'audit{case}q{q}k{j}')for j in range(2)];ee=[];vv=core[:]
  for index in range(54):
   if index in coeff:
    a,u,v=coeff[index];ee.append((a+u*core[0]+v*core[1])%q)
   elif index==52:ee.append(core[0])
   elif index==53:ee.append(core[1])
   else:
    x=z3.Int(f'audit{case}q{q}unused{index}');vv.append(x);ee.append(x)
  exprs.append(ee);variables.append(vv)
 r=enumerate_observed(exprs[0],variables[0],exprs[1],variables[1],observed);assert r is not None
 # Independent brute force over all676 mod26 parameter pairs, no Z3 expressions.
 witness=None
 for a,c in product(range(26),repeat=2):
  pos={i:(base+u*a+v*c)%26 for i,(base,u,v)in coeff.items()}
  if len({pos[i]for i in range(8)})==8 and len({pos[i]for i in range(26,34)})==8:witness=(a,c);break
 assert (r['status']=='sat')==(witness is not None)
 if r['status']=='sat':
  vals=r['values'];assert len({vals[i]for i in range(8)})==8 and len({vals[i]for i in range(26,34)})==8
  for start in [0,26]:
   known=vals[start:start+8];full=known+sorted(set(range(26))-set(known));assert sorted(full)==list(range(26))
 rows.append(dict(case=case,independent_status='sat'if witness else'unsat',finite={k:v for k,v in r.items()if k!='values'},observed_values=[r['values'][i]for i in observed]if r['status']=='sat'else None))
(b/'finite-independent-audit.json').write_text(json.dumps(dict(cases=rows,independent_assignment_domain='all676 integer mod26 parameter pairs percase; dimensions may reduce when coefficients even/zero',status_agreement=True,unused_permutation_extension_checked=True),indent=2)+'\n');print('20 finite-algebra cases agree with independent676-pair enumeration (10SAT/10UNSAT).')
