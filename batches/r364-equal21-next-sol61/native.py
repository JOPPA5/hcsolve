from collections import Counter
import sys,time
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3

def solve(plain,variants,width=21,progressive=False,seconds=60):
 n=len(plain);q,r=divmod(n,width);assert r==2 and all(Counter(c)==Counter(plain)for c in variants);build=time.monotonic();s=z3.Then('simplify','card2bv','bit-blast','sat').solver();s.set(timeout=int(seconds*1000),random_seed=3642112)
 arrays=[[z3.BitVecVal(ord(c)-97,5)for c in plain]]
 for j in range(2):
  chars=[z3.BitVec(f'char{j}_{i}',5)for i in range(n)];arrays.append(chars)
  for ch,count in Counter(plain).items():s.add(z3.PbEq([(v==ord(ch)-97,1)for v in chars],count))
 output=[z3.BitVecVal(ord(c)-97,5)if len({v[i]for v in variants})==1 else z3.BitVec(f'out{i}',5)for i,c in enumerate(variants[0])];s.add(z3.Or(*[z3.And(*[output[i]==ord(c)-97 for i,c in enumerate(v)])for v in variants]));arrays.append(output)
 shared=[z3.Bool(f'alignment{a}')for a in range(width-2 if progressive else width)];s.add(z3.PbEq([(v,1)for v in shared],1));perms=[]
 for j in range(3):
  A=[[z3.Bool(f'perm{j}_{col}_{rank}')for rank in range(width)]for col in range(width)];perms.append(A)
  for col in range(width):s.add(z3.PbEq([(v,1)for v in A[col]],1))
  for rank in range(width):s.add(z3.PbEq([(A[col][rank],1)for col in range(width)],1))
  for rank in range(width):
   off=rank-(j if progressive else 0);s.add(A[0][rank]==(shared[off]if 0<=off<len(shared)else z3.BoolVal(False)))
  before=[[z3.Bool(f'before{j}_{long}_{rank}')for rank in range(width)]for long in [0,1]]
  for long in [0,1]:
   for rank in range(width):s.add(before[long][rank]==z3.Or(*A[long][:rank]))
  for col in range(width):
   for rank in range(width):
    if col<2:conditions=[z3.Not(before[1-col][rank]),before[1-col][rank]]
    else:conditions=[z3.And(z3.Not(before[0][rank]),z3.Not(before[1][rank])),z3.Xor(before[0][rank],before[1][rank]),z3.And(before[0][rank],before[1][rank])]
    for offset,condition in enumerate(conditions):
     for row in range(q+(col<2)):s.add(z3.Implies(z3.And(A[col][rank],condition),arrays[j][row*width+col]==arrays[j+1][q*rank+offset+row]))
 built=time.monotonic()-build;at=time.monotonic();status=s.check();out=dict(status=str(status),seconds=time.monotonic()-at,build_seconds=built,widths=[width]*3,progressive=progressive,unknown_alignment=True,truth_key_seed=False,Boolean_permutations=True,variable_elements=0)
 if status==z3.sat:
  m=s.model();keys=[[next(col for col in range(width)if z3.is_true(m.eval(A[col][rank])))for rank in range(width)]for A in perms];pred=plain
  for k in keys:pred=''.join(pred[i]for col in k for i in range(col,len(pred),width))
  assert pred in variants;x=pred
  for k in keys[::-1]:
   arr=['']*n;pos=0
   for col in k:
    for i in range(col,n,width):arr[i]=x[pos];pos+=1
   x=''.join(arr)
  assert x==plain;out.update(keys=keys,full_encoder_inverse=True,plaintext=plain,selected_ciphertext=pred,alignment=next(i+1 for i,v in enumerate(shared)if z3.is_true(m.eval(v))))
 else:out['reason']=s.reason_unknown()if status==z3.unknown else 'exactUNSAT'
 return out
