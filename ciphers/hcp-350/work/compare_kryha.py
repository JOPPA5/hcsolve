from pathlib import Path
from collections import Counter,defaultdict
import random,math
p=Path(__file__).parent
x=p.joinpath('cipher.txt').read_text();y=''.join((p.parents[1]/'hcp-351/work/transcription.txt').read_text().lower().split())
print('Lengths',len(x),len(y))
for lo,hi in [(0,20),(20,375),(375,385)]:print('half-open range',lo,hi,'equal',sum(a==b for a,b in zip(x[lo:hi],y[lo:hi])))
print('Matching groups >=2letters,1based')
for i in range(0,len(x),5):
 n=sum(a==b for a,b in zip(x[i:i+5],y[i:i+5]))
 if n>=2:print(i//5+1,x[i:i+5],y[i:i+5],n)
x=x[20:375];y=y[20:375]
expected=len(x)*sum(Counter(x)[c]*Counter(y)[c] for c in set(x))/(len(x)*len(y))
print('Interior independent marginal expected matches',expected)
# Under same plaintext, same mixed alphabets, repeating stepping schedule of lengthT,
# but distinct wheel phase/start positions, each residue has a fixed bijection C1->C2.
# Count paired occurrences of same C1 in same residue: true model requires same C2.
def consistency(a,b,T):
 inp=Counter();out=Counter();joint=Counter()
 for i,(c,d) in enumerate(zip(a,b)):
  inp[i%T,c]+=1;out[i%T,d]+=1;joint[i%T,c,d]+=1
 choose=lambda n:n*(n-1)//2
 hits=sum(choose(v) for v in joint.values())
 return hits,sum(choose(v) for v in inp.values()),sum(choose(v) for v in out.values())
print('Kryha same-plaintext/shared-alphabets phase-bijection test:period matched/repeated-input/repeated-output pairs')
for T in range(1,41):print(T,*consistency(x,y,T))
rng=random.Random(350351);observed=consistency(x,y,17)[0];null=[];equal_null=[]
for _ in range(5000):
 z=list(y);rng.shuffle(z);null.append(consistency(x,z,17)[0]);equal_null.append(sum(a==b for a,b in zip(x,z)))
print('17phase observed',observed,'shuffle mean',sum(null)/len(null),'right-tail',(1+sum(v>=observed for v in null))/(1+len(null)))
equals=sum(a==b for a,b in zip(x,y))
print('Equality deficit observed',equals,'shuffle mean',sum(equal_null)/len(equal_null),'left-tail',(1+sum(v<=equals for v in equal_null))/(1+len(equal_null)))
print('This rejects or supports ONLY stated shared-alphabet/same-plaintext model, not Kryha in general.')
steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9]
def schedule(n,phase):
 z=0;out=[]
 for i in range(n):out.append(z);z=(z+steps[(phase+i)%17])%26
 return out
# Identical cumulative wheel position implies the same mixed substitution alphabet;
# pooling equality counts therefore tests Kryha's historical schedule without either ring key.
def pooled_ic(t,sch):
 d=Counter(zip(sch,t));n=Counter(sch)
 return sum(v*(v-1) for v in d.values())/sum(v*(v-1) for v in n.values())
for label,t in [('350interior',x),('351interior',y)]:
 schedules=[schedule(len(t),phase) for phase in range(17)]
 scores=[pooled_ic(t,sch) for sch in schedules]
 print(label,'historical17step ring-position pooledIC',scores,'best',max(scores),'phase',scores.index(max(scores)))
 null=[]
 for _ in range(1000):
  z=list(t);rng.shuffle(z);null.append(max(pooled_ic(z,sch) for sch in schedules))
 print(label,'maxphase shuffle mean',sum(null)/len(null),'right-tail',(1+sum(v>=max(scores) for v in null))/(1+len(null)))
