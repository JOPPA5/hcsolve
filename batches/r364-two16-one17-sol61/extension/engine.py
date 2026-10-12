from collections import Counter
import sys,time
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
def domains(N,w,col):
 q,r=divmod(N,w);L=q+(col<r);out=set()
 for k in range(w):
  for lo in range(max(0,k-(w-r-(col>=r))),min(k,r-(col<r))+1):
   if q*k+lo+L<=N:out.add(q*k+lo)
 return sorted(out)
def encode(p,key):return ''.join(p[i]for col in key for i in range(col,len(p),len(key)))
def solve(p,variants,widths=(16,16,17),seconds=120,rank_partition=False,rank_cap=10,blocked_keys=None,backend='native'):
 N=len(p);w0,w1,w2=widths;assert w0==w1 and N%w0==1 and all(Counter(v)==Counter(p)for v in variants)
 q0=N//w0;assert q0>=2 and N>=max(widths);t=time.monotonic();s=z3.SolverFor('QF_FD')if backend=='native'else z3.Then('simplify','card2bv','bit-blast','sat').solver();s.set(timeout=int(seconds*1000),random_seed=364161617)
 nbits=[z3.Bool(f'n{k}')for k in range(min(widths))];s.add(z3.PbEq([(v,1)for v in nbits],1))
 opts=[];prefix_count=0
 for j,w in enumerate(widths):
  q,r=divmod(N,w);cols=[];occupied=[[]for _ in range(N)]
  for col in range(w):
   values={at:z3.Bool(f'A{j}_{col}_{at}')for at in domains(N,w,col)};cols.append(values);s.add(z3.PbEq([(v,1)for v in values.values()],1))
   for at,V in values.items():
    for row in range(q+(col<r)):occupied[at+row].append(V)
  for row in occupied:s.add(z3.PbEq([(v,1)for v in row],1))
  if j<2:
   # Exact single-long packing shared by the two first stages.
   # Column0 starts q*n; shorts before it have start q*rank, shorts
   # after it q*rank+1. This removes generic packing/rank variables.
   for k,bit in enumerate(nbits):s.add(cols[0][q*k]==bit)
   for col in range(1,w):
    for at,V in cols[col].items():
     if at%q==0:support=nbits[at//q+1:]
     else:
      assert at%q==1;support=nbits[:(at-1)//q]
     s.add(z3.Implies(V,z3.Or(*support)))
  else:
   states={};offsets={}
   for k in range(w+1):
    layer=[]
    for lo in range(max(0,k-(w-r)),min(k,r)+1):
     bit=z3.Bool(f'P{k}_{lo}');states[k,lo]=bit;layer.append(bit);offsets.setdefault(q*k+lo,[]).append((k,lo))
    s.add(z3.PbEq([(v,1)for v in layer],1))
   prefix_count=len(states)
   for pairs in offsets.values():s.add(z3.PbLe([(states[k,lo],1)for k,lo in pairs],1))
   for col,values in enumerate(cols):
    long=int(col<r)
    for at,V in values.items():
     support=[z3.And(states[k,lo],states[k+1,lo+long])for k,lo in offsets[at]if(k+1,lo+long)in states]
     s.add(z3.Implies(V,z3.Or(*support)))
   for k,bit in enumerate(nbits):s.add(bit==z3.Or(*[z3.And(V,cols[0][q*k+lo])for(kk,lo),V in states.items()if kk==k and q*k+lo in cols[0]]))
  opts.append(cols)
 if blocked_keys:
  chosen=[]
  for j,(w,key)in enumerate(zip(widths,blocked_keys)):
   q,r=divmod(N,w);at=0
   for col in key:chosen.append(opts[j][col][at]);at+=q+(col<r)
  s.add(z3.Or(*[z3.Not(v)for v in chosen]))
 selectors=[z3.Bool(f'variant{k}')for k in range(len(variants))];s.add(z3.PbEq([(v,1)for v in selectors],1))
 nots={v:z3.Not(v)for stage in opts for values in stage for v in values.values()};lastcache={};firstcache={};reversecache={};forward=reverse=0
 def last(col,row,ch):
  key=col,row,ch
  if key not in lastcache:
   support=[]
   for at,V in opts[2][col].items():
    matching=[bit for bit,c in zip(selectors,variants)if c[at+row]==ch]
    if matching:support.append(V if len(matching)==len(variants)else z3.And(V,z3.Or(*matching)))
   lastcache[key]=z3.Or(*support)
  return lastcache[key]
 for i,ch in enumerate(p):
  col0,row0=i%w0,i//w0
  for a,A in opts[0][col0].items():
   x=a+row0;col1,row1=x%w1,x//w1
   for b,B in opts[1][col1].items():
    y=b+row1;s.add(z3.Or(nots[A],nots[B],last(y%w2,y//w2,ch)));forward+=1
 occurrences={ch:[i for i,x in enumerate(p)if x==ch]for ch in set(p)}
 def first(x,ch):
  key=x,ch
  if key not in firstcache:firstcache[key]=z3.Or(*[opts[0][i%w0][x-i//w0]for i in occurrences.get(ch,[])if x-i//w0 in opts[0][i%w0]])
  return firstcache[key]
 cover={y:[]for y in range(N)}
 for col,values in enumerate(opts[1]):
  length=len(range(col,N,w1))
  for b,B in values.items():
   for y in range(b,b+length):cover[y].append((B,(y-b)*w1+col))
 for col2,values in enumerate(opts[2]):
  for at,C in values.items():
   for row2 in range(len(range(col2,N,w2))):
    final=at+row2;y=row2*w2+col2
    for B,x in cover[y]:
     key=x,final
     if key not in reversecache:
      chars={v[final]for v in variants};reversecache[key]=first(x,next(iter(chars)))if len(chars)==1 else z3.Or(*[z3.And(bit,first(x,c[final]))for bit,c in zip(selectors,variants)])
     s.add(z3.Or(nots[C],nots[B],reversecache[key]));reverse+=1
 built=time.monotonic()-t;t=time.monotonic();checks=[]
 if rank_partition:
  for k,V in enumerate(nbits):
   s.set(timeout=int(rank_cap*1000));at=time.monotonic();status=s.check(V);checks.append(dict(n=k+1,status=str(status),seconds=time.monotonic()-at));print('rank',k+1,str(status),round(checks[-1]['seconds'],2),flush=True)
   if status==z3.sat:break
  if status!=z3.sat and any(r['status']=='unknown'for r in checks):status=z3.unknown
 else:status=s.check()
 out=dict(status=str(status),seconds=time.monotonic()-t,build_seconds=built,widths=list(widths),unknown_common_alignment=True,n_hints=False,key_hints=False,backend=backend,rank_partition_checks=checks,rank_cap=rank_cap if rank_partition else None,timeout=seconds,selected_start_variables=sum(len(v)for stage in opts for v in stage),third_stage_prefix_states=prefix_count,first_two_stages_explicit_singlelong_packing=True,forward_clauses=forward,reverse_clauses=reverse)
 if status==z3.sat:
  m=s.model();keys=[sorted(range(w),key=lambda col:next(at for at,V in stage[col].items()if z3.is_true(m.eval(V))))for w,stage in zip(widths,opts)];n=next(k+1 for k,V in enumerate(nbits)if z3.is_true(m.eval(V)));selected=next(c for bit,c in zip(selectors,variants)if z3.is_true(m.eval(bit)));pred=p
  for key in keys:pred=encode(pred,key)
  assert pred==selected and all(key.index(0)+1==n for key in keys)
  out.update(keys=keys,recovered_n=n,selected_ciphertext=selected,conditional_plaintext=p,full_reencryption=True)
 else:out['reason']=('some ranks timed out'if rank_partition else s.reason_unknown())if status==z3.unknown else'UNSAT under fixed conditions'
 return out
