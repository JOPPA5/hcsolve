import json,sys
c=[d for d in json.load(open('work/comps150.json')) if d['n']>=2 and d['mn']<135 and d['x1']-d['x0']<45 and d['y1']-d['y0']<11 and d['cx']<615 and d['cx']>35]
S=float(sys.argv[1]) if len(sys.argv)>1 else 0.0
for d in c: d['k']=d['cy']-S*d['cx']
c.sort(key=lambda d:d['k'])
groups=[];cur=[c[0]]
for d in c[1:]:
  if d['k']-cur[-1]['k']>4: groups.append(cur);cur=[d]
  else: cur.append(d)
groups.append(cur)
for g in groups:
  ks=[d['k'] for d in g]
  print(round(min(ks)),round(max(ks)),len(g),round(min(d['cx'] for d in g)),round(max(d['cx'] for d in g)))
