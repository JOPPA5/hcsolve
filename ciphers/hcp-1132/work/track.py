# Track columns: link marks top->bottom by nearest predicted x.
import json
c=json.load(open('work/comps.json'))
for o in c:
    o['h']=o['y1']-o['y0']+1; o['w']=o['x1']-o['x0']+1
c=[o for o in c if o['h']<200 and o['area']>=40]
c.sort(key=lambda o:o['y0'])
tracks=[]
for o in c:
    best=None
    for t in tracks:
        last=t[-1]
        if o['y0']-last['y1']>260: continue
        if len(t)>=3:
            a,b=t[-3],t[-1]
            sl=(b['x']-a['x'])/max(1,(b['y']-a['y']))
            px=b['x']+sl*(o['y']-b['y'])
        else: px=last['x']
        d=abs(o['x']-px)
        if d<20 and (best is None or d<best[0]): best=(d,t)
    if best: best[1].append(o)
    else: tracks.append([o])
tracks=[t for t in tracks if len(t)>=3]
tracks.sort(key=lambda t:t[0]['x'])
for i,t in enumerate(tracks):
    print(f"track {i}: n={len(t)} x {t[0]['x']:.0f}->{t[-1]['x']:.0f} y {t[0]['y0']}->{t[-1]['y1']}")
json.dump(tracks,open('work/tracks.json','w'))
