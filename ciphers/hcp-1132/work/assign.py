# Assign each ink mark to the nearest column polyline; print sequences with gaps.
import json,sys
sys.path.insert(0,'work')
from cols21 import COLS,xat
c=json.load(open('work/comps.json'))
cols={k:[] for k in COLS}
far=[]
for o in c:
    o['h']=o['y1']-o['y0']+1; o['w']=o['x1']-o['x0']+1
    if o['area']<40 or o['h']>200: continue
    d=sorted((abs(o['x']-xat(k,o['y'])),k) for k in COLS)
    o['dist']=round(d[0][0],1)
    if d[0][0]>26: far.append(o); continue
    cols[d[0][1]].append(o)
out={}
for k in sorted(cols):
    col=sorted(cols[k],key=lambda o:o['y0']); prev=None; parts=[]
    for o in col:
        sym='h' if (o['w']>o['h']*1.6 and o['w']>18) else ('.' if o['h']<25 else '-')
        o['sym']=sym; o['gap']=None if prev is None else o['y0']-prev['y1']; prev=o
        parts.append(f"{'' if o['gap'] is None else '['+str(o['gap'])+']'}{sym}{o['h']}@{o['y0']}" + (f"~{o['dist']}" if o['dist']>14 else ''))
    print(f"C{k}: "+' '.join(parts))
    out[k]=col
print('unassigned:',[(o['x'],o['y0'],o['h'],o['w']) for o in far])
json.dump(out,open('work/assigned.json','w'))
