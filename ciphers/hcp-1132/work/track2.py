# Seeded column tracking: 21 seeds at the top; each mark (in y order) joins the track
# whose linear prediction (fit over its last 6 marks) is nearest, if within TOL px.
import json
TOL=17
c=json.load(open('work/comps.json'))
for o in c:
    o['h']=o['y1']-o['y0']+1; o['w']=o['x1']-o['x0']+1
c=[o for o in c if 40<=o['area']<3000 and o['h']<200]
c.sort(key=lambda o:o['y0'])
SEED=[1461,1394,1312,1248,1179,1109,1041,959,900,840,785,730,652,592,512,449,376,308,233,163,92]
tracks=[[{'x':s,'y':60,'seed':1}] for s in SEED]
def pred(t,y):
    pts=[p for p in t if not p.get('seed')][-6:]
    if len(pts)<2:
        return (pts[-1]['x'] if pts else t[0]['x']), -0.03 if t[0]['x']<900 else 0.0
    n=len(pts); my=sum(p['y'] for p in pts)/n; mx=sum(p['x'] for p in pts)/n
    vy=sum((p['y']-my)**2 for p in pts)
    sl=sum((p['y']-my)*(p['x']-mx) for p in pts)/vy if vy>0 else 0
    sl=max(-0.12,min(0.06,sl))
    return mx+sl*(y-my), sl
un=[]
for o in c:
    best=None
    for i,t in enumerate(tracks):
        px,_=pred(t,o['y'])
        d=abs(o['x']-px)
        if d<TOL and (best is None or d<best[0]): best=(d,i)
    if best: tracks[best[1]].append(o)
    else: un.append(o)
for i,t in enumerate(tracks):
    t=[p for p in t if not p.get('seed')]
    tracks[i]=t
    print(f"C{i+1}: n={len(t)} x {t[0]['x']:.0f}->{t[-1]['x']:.0f} y {t[0]['y0']}->{t[-1]['y1']}")
print('unassigned:',[(round(o['x']),o['y0'],o['h'],o['w']) for o in un])
json.dump(tracks,open('work/tracks2.json','w'))
