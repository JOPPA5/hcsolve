from pathlib import Path
import json, subprocess,time,random
from solve import arcs,dist
root=Path('batches/kryha-two-mask-main')
rng=random.Random(350351233)
rows=[]
for n in (5,23):
 for trial in range(4):
  masks=[]
  for _ in range(2):
   m=sorted(rng.sample(range(52),n));p=rng.randrange(n);m=m[p:]+m[:p];masks.append(m)
  aa,bb=map(arcs,masks);delta=[(b-a)%26 for a,b in zip(aa,bb)]
  data=' '.join(map(str,[n]+dist+delta))+'\n'
  t=time.monotonic();out=subprocess.check_output([str(root/'fit_dp')],input=data,text=True)
  lines=out.splitlines();assert lines[0].startswith('YES ')
  got=list(zip(*[map(int,l.split()) for l in lines[1:]]));ga,gb=map(lambda h:arcs(list(h)),got)
  assert all((b-a)%26==d for a,b,d in zip(ga,gb,delta))
  assert sum(ga)==sum(gb)==179 and all(len(set(h))==n for h in got)
  rows.append(dict(n=n,trial=trial,seconds=time.monotonic()-t,anchor_pairs=int(lines[0].split()[1]),
    independent_arc_check=True,truth_masks_used=False,planted_masks=masks,recovered_masks=got,delta=delta))
(root/'dp-controls.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps([dict(n=r['n'],trial=r['trial'],seconds=r['seconds'],anchor_pairs=r['anchor_pairs']) for r in rows]))
