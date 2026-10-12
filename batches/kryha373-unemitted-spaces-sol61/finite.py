"""Exact finite enumeration of parameters affecting observed ring slots only."""
from itertools import product
import time
from model import z3
from z3.z3util import get_vars

def enumerate_observed(e2,v2,e13,v13,observed,limit=50000):
 start=time.monotonic();active=[]
 for exprs,variables in [(e2,v2),(e13,v13)]:
  used=set()
  for i in observed:
   if isinstance(exprs[i],z3.ExprRef):used.update(str(x)for x in get_vars(exprs[i]))
  active.append([x for x in variables if str(x)in used])
 total=(2**len(active[0]))*(13**len(active[1]))
 if total>limit:return None
 def numeric(exprs,variables,act,q):
  def evaluate(replacement):
   sub=[(x,z3.IntVal(replacement.get(str(x),0)))for x in variables];return [z3.simplify(z3.substitute(e,*sub)).as_long()%q if isinstance(e,z3.ExprRef)else e%q for e in exprs]
  base=evaluate({});coeff=[]
  for x in act:
   value=evaluate({str(x):1});coeff.append([(a-b)%q for a,b in zip(value,base)])
  return base,coeff
 b2,c2=numeric(e2,v2,active[0],2);b13,c13=numeric(e13,v13,active[1],13);left=[i for i in observed if i<26];right=[i for i in observed if 26<=i<52];tested=0
 for vals13 in product(range(13),repeat=len(active[1])):
  a13=[(b+sum(v*cc[i]for v,cc in zip(vals13,c13)))%13 for i,b in enumerate(b13)]
  for vals2 in product(range(2),repeat=len(active[0])):
   a2=[(b+sum(v*cc[i]for v,cc in zip(vals2,c2)))%2 for i,b in enumerate(b2)];values=[a+13*((bb-a)%2)for a,bb in zip(a13,a2)];tested+=1
   if len({values[i]for i in left})==len(left)and len({values[i]for i in right})==len(right):return dict(status='sat',values=values,seconds=time.monotonic()-start,enumerated=tested,total=total,active2=len(active[0]),active13=len(active[1]))
 return dict(status='unsat',seconds=time.monotonic()-start,enumerated=tested,total=total,active2=len(active[0]),active13=len(active[1]))
