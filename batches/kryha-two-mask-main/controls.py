from solve import fit,arcs
from pathlib import Path
import random,json
P=Path(__file__).parent;rng=random.Random(350351232);rows=[]
for n in [5,23]:
    masks=[]
    for _ in range(2):
        h=sorted(rng.sample(range(52),n));k=rng.randrange(n);h=h[k:]+h[:k];masks.append(h)
    a,b=map(arcs,masks);delta=[(y-x)%26 for x,y in zip(a,b)]
    row=fit(delta,seconds=30);row.update(planted_masks=masks,count=n)
    if 'masks'in row:row['same_masks_as_planted']=row['masks']==masks
    rows.append(row);(P/'controls.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(n,row['status'],row['seconds'],flush=True)
