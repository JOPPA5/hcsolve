# Independent straightforward IDP: feasible starts, then repeated greedy edge scan.
from pathlib import Path
import json,random,subprocess
w=Path(__file__).resolve().parent;big=Path('ciphers/hcp-363/work/segmented/bigrams.tsv');bi={a:float(b) for a,b in (s.split() for s in big.read_text().splitlines())}
def ref(s,width):
 h,e=divmod(len(s),width);starts=[range(h*i+max(0,e-(width-i-1)),h*i+min(i+1,e)+1) for i in range(width)]
 B={(a,b):max(sum(bi[s[p+r]+s[q+r]] for r in range(h))/h for p in starts[a] for q in starts[b]) for a in range(width) for b in range(width) if a!=b}
 left={};right={};total=0
 for step in range(width):
  choices=[]
  for (a,b),score in B.items():
   if a in right or b in left:continue
   cur=a;cyclic=False
   if step<width-1:
    while cur in left:
     cur=left[cur]
     if cur==b:cyclic=True;break
   if not cyclic:choices.append((score,-a,-b))
  value,na,nb=max(choices);a,b=-na,-nb;right[a]=b;left[b]=a;total+=value
 return total/width
rng=random.Random(399443);results=[]
for i in range(42):
 n=[240,245][i%2];width=16+i%7;s=''.join(rng.choice('aaaaaaeeeeeeiiiiioooonnnrrrsssstttvvkkmmldpuyzbcfhjxg') for _ in range(n));p=w/'reference-input.txt';p.write_text(s)
 got=float(subprocess.check_output([str(w/'idp'),str(big),str(p),str(width),'17','score'],text=True));want=ref(s,width);assert abs(got-want)<0.00006,(i,width,got,want);results.append(dict(n=n,width=width,cpp=got,python=want))
w.joinpath('reference-validation.json').write_text(json.dumps(dict(all_pass=True,cases=results),indent=2));print('42 independent IDP scorer comparisons PASS, lengths240/245 widths16..22')
