from pathlib import Path
import json
b=Path(__file__).resolve().parent;results=[]
for d in sorted(b.glob('second-gauge*')):
 if not (d/'reranked.txt').exists():continue
 row=json.loads((d/'derived-row.json').read_text());candidates=[]
 for file in [d/'reranked.txt']+sorted(d.glob('round*/reranked.txt')):
  lines=file.read_text().splitlines();pfile=file.parent/'paths.txt'
  if pfile.exists():
   paths=[]
   for line in pfile.read_text().splitlines()[1:]:
    z=list(map(int,line.split()[1:]));paths.append([z[::2],z[1::2]])
  else:paths=json.loads((d/'paths.json').read_text())
  for i,line in enumerate(lines):
   if line.startswith('N '):
    n=int(line.split()[1]);v=lines[i+1].split();candidates.append(dict(n=n,score=float(v[0]),id=int(v[1]),P=list(map(int,lines[i+2].split())),plaintexts=lines[i+3:i+5],masks=paths[int(v[1])],provenance=str(file.relative_to(b))))
 for n in [6,7]:
  win=max((c for c in candidates if c['n']==n),key=lambda c:c['score']);win.update(gauge=int(d.name.split('gauge')[1]),O=row['output_positions'],K=row['shifts_by_absolute_residue']);results.append(win)
results.sort(key=lambda c:(c['n'],-c['score']));(b/'second-blind-ranked.json').write_text(json.dumps(results,indent=2)+'\n');print('Blind rankings saved, both pure6 and pure7, no truth read.')
