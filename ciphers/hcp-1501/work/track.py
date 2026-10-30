import json,sys,collections
SEEDS=[45,62,78,95,111,125,139,152,170,189,206,223,240,257,273,292,310,327,346,365,386,406,429,451,471,491,507,524,541,561,579,598,617]
XMAX={139:325}
c=[d for d in json.load(open('work/comps150.json')) if d['n']>=2 and d['mn']<135 and d['x1']-d['x0']<40 and d['y1']-d['y0']<11 and 35<d['cx']<620]
c.sort(key=lambda d:d['cx'])
used=set();lines=[]
for s in SEEDS:
  y=s;last=None;L=[]
  for i,d in enumerate(c):
    if i in used: continue
    if abs(d['cy']-y)<=4.5 and d['cx']<=XMAX.get(s,9999):
      if last is not None and d['x0']-last>45: break
      L.append(d);used.add(i);y=0.7*y+0.3*d['cy'];last=d['x1']
  lines.append(L)
json.dump(lines,open('work/lines.json','w'))
ws=collections.Counter();gs=collections.Counter()
for L in lines:
  for a,b in zip(L,L[1:]): gs[b['x0']-a['x1']-1]+=1
  for d in L: ws[d['x1']-d['x0']+1]+=1
print('widths',sorted(ws.items()));print('gaps',sorted(gs.items()))
for s,L in zip(SEEDS,lines): print(s,len(L),L[0]['x0'] if L else None,L[-1]['x1'] if L else None)
