from pathlib import Path
from collections import Counter
import sys,json,time,random
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
b=Path(__file__).resolve().parent

def enc(p,k):return ''.join(p[i]for col in k for i in range(col,len(p),17))
def inv(c,k):
 a=['']*50;at=0
 for col in k:
  for i in range(col,50,17):a[i]=c[at];at+=1
 return ''.join(a)
def build(p,c,w=17,progressive=False,errorPF=False):
 N=3*w-1
 assert len(p)==len(c)==N
 if not errorPF:assert Counter(p)==Counter(c)
 else:assert Counter(p)-Counter(c)==Counter(f=1)and Counter(c)-Counter(p)==Counter(p=1)
 s=z3.SolverFor('QF_FD');s.set(random_seed=396171762)
 ranks=[[[z3.Bool(f'r{stage}_{col}_{r}')for r in range(w)]for col in range(w)]for stage in range(3)]
 for layer in ranks:
  for bits in layer:s.add(z3.PbEq([(x,1)for x in bits],1))
  for r in range(w):s.add(z3.PbEq([(layer[col][r],1)for col in range(w)],1))
 if not progressive:
  for r in range(w):s.add(ranks[0][0][r]==ranks[1][0][r],ranks[0][0][r]==ranks[2][0][r])
 else:
  for r in range(w-2):s.add(ranks[0][0][r]==ranks[1][0][r+1],ranks[0][0][r]==ranks[2][0][r+2])
  for st,invalid in [(0,[w-2,w-1]),(1,[0,w-1]),(2,[0,1])]:
   for r in invalid:s.add(z3.Not(ranks[st][0][r]))
 errors={i:z3.Bool(f'errorPF{i}')for i,ch in enumerate(c)if ch=='p'}if errorPF else{}
 if errorPF:s.add(z3.PbEq([(e,1)for e in errors.values()],1))
 def match(ch,dst,bit):
  if dst in errors:
   if ch=='f':return z3.And(bit,errors[dst])
   if ch=='p':return z3.And(bit,z3.Not(errors[dst]))
   return None
  return bit if c[dst]==ch else None
 route=[];forward=[];backward=[]
 for st in range(3):
  cuts=[z3.Bool(f'cut{st}_{r}')for r in range(w)]
  for r in range(w):s.add(cuts[r]==z3.Or(ranks[st][w-1][:r]))
  fw=[[]for _ in range(N)];bw=[[]for _ in range(N)]
  for i in range(N):
   col,row=i%w,i//w
   for r in range(w):
    shifts=[0]if col==w-1 else([0]if r==0 else[1]if r==w-1 else[0,1])
    for sh in shifts:
     dst=3*r-sh+row
     if not 0<=dst<N:continue
     bit=z3.Bool(f'map{st}_{i}_{r}_{sh}');s.add(bit==z3.And(ranks[st][col][r],cuts[r]if sh else z3.Not(cuts[r])))
     fw[i].append((dst,bit));bw[dst].append((i,bit))
  for opts in fw+bw:s.add(z3.Or([bit for _,bit in opts]))
  forward.append(fw);backward.append(bw)
 clauses=0
 # Complete endpoint support in both directions, no intermediate character guesses.
 for i,ch in enumerate(p):
  for pos1,b0 in forward[0][i]:
   for pos2,b1 in forward[1][pos1]:
    support=[a for dst,bit in forward[2][pos2]if(a:=match(ch,dst,bit))is not None];s.add(z3.Or(z3.Not(b0),z3.Not(b1),*support));clauses+=1
 for dst,ch in enumerate(c):
  for pos2,b2 in backward[2][dst]:
   for pos1,b1 in backward[1][pos2]:
    support=[a for src,bit in backward[0][pos1]if(a:=match(p[src],dst,bit))is not None];s.add(z3.Or(z3.Not(b2),z3.Not(b1),*support));clauses+=1
 return s,ranks,clauses
