import sys,time
from collections import Counter
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
def starts(N,w,col):
 q,r=divmod(N,w);L=q+(col<r);out=set()
 for k in range(w):
  for lo in range(max(0,k-(w-r-(col>=r))),min(k,r-(col<r))+1):out.add(q*k+lo)
 return sorted(at for at in out if at+L<=N)
def enc(p,k):return ''.join(p[c::len(k)]for c in k)
def dec(c,k):
 out=['']*len(c);at=0
 for col in k:
  for i in range(col,len(c),len(k)):out[i]=c[at];at+=1
 return ''.join(out)
def build(p,c,widths=(21,19,20),progressive=False,known_keys=None,blocked_keys=None,verbose=False):
 assert len(p)==len(c) and Counter(p)-Counter(c)==Counter(f=1) and Counter(c)-Counter(p)==Counter(p=1)
 N=len(p);begin=time.monotonic();s=z3.SolverFor('QF_FD');s.set(random_seed=3966122120)
 opts=[];prefix=[];literals=0;statebits=0
 for j,w in enumerate(widths):
  q,r=divmod(N,w);cols=[];occupy=[[]for _ in range(N)]
  fixed={};at=0
  if known_keys:
   for col in known_keys[j]:fixed[col]=at;at+=q+(col<r)
  for col in range(w):
   domain=starts(N,w,col)
   if known_keys:assert fixed[col]in domain;domain=[fixed[col]]
   values={a:z3.Bool(f'A{j}_{col}_{a}')for a in domain};cols.append(values);literals+=len(values);s.add(z3.PbEq([(v,1)for v in values.values()],1))
   for a,v in values.items():
    for row in range(len(range(col,N,w))):occupy[a+row].append(v)
  for row in occupy:s.add(z3.PbEq([(v,1)for v in row],1))
  # Prefix path: after k chunks, lo of them are long. Domains are exact,
  # only (r+1)*(w-r+1) states instead of arbitrary rank values at every offset.
  states={};byoffset={}
  for k in range(w+1):
   layer=[]
   for lo in range(max(0,k-(w-r)),min(k,r)+1):
    bit=z3.Bool(f'P{j}_{k}_{lo}');states[k,lo]=bit;layer.append(bit);byoffset.setdefault(q*k+lo,[]).append((k,lo))
   s.add(z3.PbEq([(v,1)for v in layer],1))
  statebits+=len(states)
  for pairs in byoffset.values():s.add(z3.PbLe([(states[k,lo],1)for k,lo in pairs],1))
  for col,values in enumerate(cols):
   islong=int(col<r)
   for a,A in values.items():
    supports=[z3.And(states[k,lo],states[k+1,lo+islong])for k,lo in byoffset.get(a,[])if(k+1,lo+islong)in states]
    s.add(z3.Implies(A,z3.Or(*supports)))
  if known_keys:
   at=0
   for col in known_keys[j]:s.add(cols[col][at]);at+=q+(col<r)
  opts.append(cols);prefix.append((states,byoffset))
 maxn=min(w-j if progressive else w for j,w in enumerate(widths));nvars=[z3.Bool(f'n{k}')for k in range(maxn)];s.add(z3.PbEq([(v,1)for v in nvars],1))
 for k,nbit in enumerate(nvars):
  for j,w in enumerate(widths):
   q,r=divmod(N,w);rank=k+j if progressive else k;states,_=prefix[j]
   supports=[z3.And(bit,opts[j][0][q*rank+lo])for(kk,lo),bit in states.items()if kk==rank and q*rank+lo in opts[j][0]]
   s.add(nbit==z3.Or(*supports))
 if blocked_keys:
  chosen=[]
  for j,(w,key)in enumerate(zip(widths,blocked_keys)):
   q,r=divmod(N,w);at=0
   for col in key:chosen.append(opts[j][col][at]);at+=q+(col<r)
  s.add(z3.Or(*[z3.Not(v)for v in chosen]))
 E={i:z3.Bool(f'E{i}')for i,ch in enumerate(c)if ch=='p'};s.add(z3.PbEq([(v,1)for v in E.values()],1))
 nots={v:z3.Not(v)for cols in opts for values in cols for v in values.values()}
 w0,w1,w2=widths;lastcache={};firstcache={};forward=reverse=0
 def final_support(col,row,ch):
  key=col,row,ch
  if key not in lastcache:
   bits=[]
   for at,V in opts[2][col].items():
    pos=at+row
    if c[pos]==ch:bits.append(z3.And(V,z3.Not(E[pos]))if pos in E else V)
    elif ch=='f'and c[pos]=='p':bits.append(z3.And(V,E[pos]))
   lastcache[key]=z3.Or(*bits)
  return lastcache[key]
 for i,ch in enumerate(p):
  col0,row0=i%w0,i//w0
  for a,A in opts[0][col0].items():
   x=a+row0;col1,row1=x%w1,x//w1
   for b,B in opts[1][col1].items():
    y=b+row1;col2,row2=y%w2,y//w2;s.add(z3.Or(nots[A],nots[B],final_support(col2,row2,ch)));forward+=1
  if verbose and i%25==0:print('forward',i,forward,flush=True)
 occurrences={ch:[i for i,x in enumerate(p)if x==ch]for ch in set(p)}
 def initial_support(x,ch):
  key=x,ch
  if key not in firstcache:
   firstcache[key]=z3.Or(*[opts[0][i%w0][x-i//w0]for i in occurrences.get(ch,[])if x-i//w0 in opts[0][i%w0]])
  return firstcache[key]
 middlecovers={y:[]for y in range(N)}
 for col,values in enumerate(opts[1]):
  length=len(range(col,N,w1))
  for b,B in values.items():
   for y in range(b,b+length):middlecovers[y].append((B,(y-b)*w1+col))
 for col2,values in enumerate(opts[2]):
  for at,C in values.items():
   for row2 in range(len(range(col2,N,w2))):
    final=at+row2;y=row2*w2+col2;ch=c[final]
    for B,x in middlecovers[y]:
     support=initial_support(x,ch)
     if final in E:support=z3.Or(z3.And(z3.Not(E[final]),support),z3.And(E[final],initial_support(x,'f')))
     s.add(z3.Or(nots[C],nots[B],support));reverse+=1
  if verbose and col2%5==0:print('reverse',col2,reverse,flush=True)
 return s,opts,nvars,dict(build_seconds=time.monotonic()-begin,widths=list(widths),selected_start_variables=literals,prefix_path_state_variables=statebits,forward_endpoint_clauses=forward,reverse_endpoint_clauses=reverse,progressive=progressive)
