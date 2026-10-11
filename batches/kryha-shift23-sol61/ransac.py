from pathlib import Path
import json,random,time,collections,sys
b=Path(__file__).resolve().parent;a,c=json.load(open(Path(sys.argv[1]) if len(sys.argv)>1 else b/'preferred-pair.json'));pairs=[(i%23,ord(a[i])-97,ord(c[i+1])-97,i) for i in range(21,375)];n=49;rows=[]
for r,x,y,i in pairs:
 v=[0]*n;v[y]+=1;v[x]-=1;v[26+r]-=1;rows.append(v)
gauge=[0]*n;gauge[0]=1
# Independent randomized rank48 bases; same noisy rows for GF2/GF13. True cycle never used.
def nullone(indices,q):
 piv={}
 for k in [-1]+indices:
  v=[z%q for z in(gauge if k<0 else rows[k])]
  for p,w in sorted(piv.items()):
   if v[p]:d=v[p];v=[(x-d*y)%q for x,y in zip(v,w)]
  p=next((j for j,x in enumerate(v) if x),None)
  if p is None:continue
  s=pow(v[p],-1,q);v=[x*s%q for x in v];piv[p]=v
  if len(piv)==48:break
 if len(piv)!=48:return None
 free=next(j for j in range(n) if j not in piv);v=[0]*n;v[free]=1
 for p,w in sorted(piv.items(),reverse=True):v[p]=-sum(w[j]*v[j] for j in range(p+1,n))%q
 return v
rng=random.Random(35035123);best=0;found={};start=time.monotonic()
for trial in range(10000):
 ix=list(range(len(rows)));rng.shuffle(ix);v13=nullone(ix,13)
 if v13 is None or any(v13[:26].count(t)!=2 for t in range(13)):continue
 v2=nullone(ix,2)
 if v2 is None or v2[:26].count(0)!=13:continue
 for m in range(1,13):
  O=[(m*v13[j]+13*((v2[j]-m*v13[j])%2))%26 for j in range(26)]
  if len(set(O))!=26:continue
  hist=[collections.Counter() for _ in range(23)]
  for r,x,y,i in pairs:hist[r][(O[y]-O[x])%26]+=1
  shifts=[h.most_common(1)[0][0] for h in hist];score=sum(h[s] for h,s in zip(hist,shifts));key=tuple(O)
  if key not in found:found[key]=dict(output_positions=O,shifts_by_absolute_residue=shifts,matched_cells=score,trial=trial)
  if score>best:best=score;print('best',best,'trial',trial,'seconds',round(time.monotonic()-start,1),flush=True)
 if best>=325 and trial>=100:break
 if trial%1000==0:print('trial',trial,flush=True)
result=sorted(found.values(),key=lambda z:z['matched_cells'],reverse=True);(Path(sys.argv[2]) if len(sys.argv)>2 else b/'ransac-results.json').write_text(json.dumps(dict(seed=35035123,trials=trial+1,seconds=time.monotonic()-start,rows=result),indent=2)+'\n');print('done',best,len(result))
