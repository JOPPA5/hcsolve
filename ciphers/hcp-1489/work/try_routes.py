from pathlib import Path
import json,math
p=Path(__file__).resolve().parent
ct="".join((p/"transcription.txt").read_text().split())
grams="THE AND ING YOU OVE EAR THA HAT WIT ITH TIO HER HIS ALL ERE TER EST FOR ARE ENT ION".split()
words="DEAR YOUR WITH THAT THIS LOVE WILL HAVE FROM HOPE VERY SOON THINK LETTER PLEASE NIGHT WELL DARLING".split()
def score(s):
 return sum(s.count(g)*len(g) for g in grams)+sum(s.count(w)*len(w)**2 for w in words)
out=[]
def keep(name,s):
 out.append((score(s),name,s))
def rail(n,r,o):
 k=2*r-2
 return [min((i+o)%k,k-(i+o)%k) for i in range(n)]
def raildec(ct,r,o,rr):
 rows=rail(len(ct),r,o);cols={};at=0
 for j in (range(r-1,-1,-1) if rr else range(r)):
  k=rows.count(j);cols[j]=iter(ct[at:at+k]);at+=k
 return "".join(next(cols[j]) for j in rows)
for rev in (False,True):
 s=ct[::-1] if rev else ct;n=len(s)
 for r in range(2,26):
  for o in range(2*r-2):
   for rr in (False,True):keep(f"rail r{r} o{o} rr{rr} rev{rev}",raildec(s,r,o,rr))
 for w in range(2,n):
  if n%w:continue
  h=n//w
  row=[(y,x) for y in range(h) for x in range(w)]
  col=[(y,x) for x in range(w) for y in range(h)]
  snake=[(y,x) for y in range(h) for x in (range(w) if y%2==0 else range(w-1,-1,-1))]
  csnake=[(y,x) for x in range(w) for y in (range(h) if x%2==0 else range(h-1,-1,-1))]
  spiral=[];top=0;bottom=h-1;left=0;right=w-1
  while top<=bottom and left<=right:
   spiral.extend((top,x) for x in range(left,right+1));top+=1
   spiral.extend((y,right) for y in range(top,bottom+1));right-=1
   if top<=bottom:spiral.extend((bottom,x) for x in range(right,left-1,-1));bottom-=1
   if left<=right:spiral.extend((y,left) for y in range(bottom,top-1,-1));left+=1
  paths={"row":row,"col":col,"snake":snake,"csnake":csnake,"spiral":spiral}
  for a,path in paths.items():
   for v in (False,True):
    for z in (False,True):
     fill=[((h-1-y if v else y),(w-1-x if z else x)) for y,x in path]
     grid=dict(zip(fill,s))
     for b,rpath in paths.items():keep(f"grid {w}x{h} {a}->{b} flip{v},{z} rev{rev}","".join(grid[c] for c in rpath))
 for k in range(1,n):
  if math.gcd(k,n)==1:
   for o in range(n):keep(f"skip{k} offset{o} rev{rev}","".join(s[(o+i*k)%n] for i in range(n)))
out.sort(reverse=True)
(p/"route-results.json").write_text(json.dumps({"length":len(ct),"tested":len(out),"top":out[:30]},indent=2))
for x in out[:8]:print(x)
