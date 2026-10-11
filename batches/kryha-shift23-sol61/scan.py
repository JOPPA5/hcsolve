from pathlib import Path
import json,collections,hashlib
b=Path(__file__).resolve().parent;r=b.parents[1];cases=[]
for reading in ('original','preferred'):
 paths=[r/f'ciphers/hcp-{n}/work/transcription.txt' if reading=='original' else r/f'batches/source-variants-350-351/{n}-source-preferred.txt' for n in (350,351)];a,c=[''.join(p.read_text().lower().split()) for p in paths];assert len(a)==len(c)==385
 rows=[]
 for off in range(-1,3):
  for p in range(2,60):
   cells=[(i,a[i],c[i+off]) for i in range(21,375)];maps=collections.defaultdict(list)
   for i,x,y in cells:maps[(i%p,x)].append(y)
   denominator=sum(len(v)-1 for v in maps.values());first=sum(sum(y==v[0] for y in v[1:]) for v in maps.values());majority=sum(max(collections.Counter(v).values())-1 for v in maps.values());rows.append(dict(offset=off,period=p,repeated_denominator=denominator,first_match=first,majority_match=majority,fraction=first/denominator if denominator else 0))
 cases.append(dict(reading=reading,source_paths=[str(p.relative_to(r)) for p in paths],source_sha256=[hashlib.sha256(p.read_bytes()).hexdigest() for p in paths],indices='zero-based21..374 inclusive, 354cells',rows=rows));(b/f'{reading}-pair.json').write_text(json.dumps([a,c])+'\n')
(b/'scan.json').write_text(json.dumps(cases,indent=2)+'\n')
for case in cases:
 print(case['reading']);print([z for z in case['rows'] if z['period'] in(17,23,26,46)]);print('best',sorted(case['rows'],key=lambda z:z['fraction'],reverse=True)[:6])
