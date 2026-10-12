from itertools import product,islice
import time
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0,str(Path('batches/kryha373-unemitted-spaces-sol61').resolve()))
from model import z3
from z3.z3util import get_vars

def enumerate_observed(e2,v2,e13,v13,observed,limit=913952):
 start=time.monotonic();active=[]
 for ee,vv in [(e2,v2),(e13,v13)]:
  used=set()
  for i in observed:
   if isinstance(ee[i],z3.ExprRef):used.update(str(x)for x in get_vars(ee[i]))
  active.append([x for x in vv if str(x)in used])
 d2,d13=map(len,active);total=2**d2*13**d13
 if d2>5 or d13>4 or total>limit:return dict(status='bounded-out',active2=d2,active13=d13,total=total)
 def coeff(ee,vv,aa,q):
  def ev(mapping):
   ss=[(x,z3.IntVal(mapping.get(str(x),0)))for x in vv]
   return np.array([z3.simplify(z3.substitute(e,*ss)).as_long()%q if isinstance(e,z3.ExprRef)else e%q for e in ee],dtype=np.int64)
  base=ev({});cc=np.array([(ev({str(x):1})-base)%q for x in aa],dtype=np.int64).reshape(len(aa),len(ee));return base,cc
 b2,c2=coeff(e2,v2,active[0],2);b13,c13=coeff(e13,v13,active[1],13)
 a2=np.array(list(product(range(2),repeat=d2)),dtype=np.int64).reshape(2**d2,d2);r2=(b2[observed]+a2@c2[:,observed])%2
 left=[j for j,i in enumerate(observed)if i<26];right=[j for j,i in enumerate(observed)if 26<=i<52];tested=0;stream=iter(product(range(13),repeat=d13))
 while True:
  chunk=list(islice(stream,512))
  if not chunk:break
  a13=np.array(chunk,dtype=np.int64).reshape(len(chunk),d13);r13=(b13[observed]+a13@c13[:,observed])%13
  vals=r13[:,None,:]+13*((r2[None,:,:]-r13[:,None,:])%2)
  good=np.ones((len(chunk),len(a2)),dtype=bool)
  for side in [left,right]:
   ordered=np.sort(vals[:,:,side],axis=2);good &= np.all(np.diff(ordered,axis=2)!=0,axis=2)
  hits=np.argwhere(good)
  if len(hits):
   h,k=map(int,hits[0]);aa13=a13[h];aa2=a2[k];all13=(b13+aa13@c13)%13;all2=(b2+aa2@c2)%2;values=all13+13*((all2-all13)%2)
   return dict(status='sat',values=values.tolist(),enumerated=tested+h*len(a2)+k+1,total=total,active2=d2,active13=d13,seconds=time.monotonic()-start,integer_dtype='int64')
  tested+=len(chunk)*len(a2)
 assert tested==total
 return dict(status='unsat',enumerated=tested,total=total,active2=d2,active13=d13,seconds=time.monotonic()-start,integer_dtype='int64')
