from pathlib import Path
import json,subprocess
b=Path(__file__).resolve().parent;r=b.parents[1];geo=json.loads((r/'batches/kryha-wheel-sol61/wheel52.json').read_text());edges=geo['adjacent_distances'];coords=geo['unwrapped_effective_coordinates'];ct=json.loads((b/'second-pair.json').read_text())
def ranked(file):
 lines=file.read_text().splitlines();assert lines[0].startswith('N 6 ');v=lines[1].split();return dict(score=float(v[0]),id=int(v[1]),P=list(map(int,lines[2].split())),plaintexts=lines[3:5])
def project(paths,O,K):
 out=[]
 for h in paths:
  pair=[]
  for q in range(2):
   s=''
   for i,ch in enumerate(ct[q]):
    t=i-q;j=t%23;D=coords[h[q][j]]-coords[h[q][0]]+179*(h[q][j]<h[q][0])+179*(t//23)+(K[0] if q else 0);s+=chr(97+(O[ord(ch)-97]-D)%26)
   pair.append(s)
  out.append(pair)
 return out
results=[]
for info in json.loads((b/'second-feasibility-summary.json').read_text()):
 if not info['feasible']:continue
 d=b/f"second-gauge{info['gauge']}";row=json.loads((d/'derived-row.json').read_text());O=row['output_positions'];K=row['shifts_by_absolute_residue'];delta=[(K[(j+1)%23]-K[j])%26 for j in range(23)];winner=ranked(d/'reranked.txt');winner['masks']=json.loads((d/'paths.json').read_text())[winner['id']];history=[]
 for it in range(1,11):
  f=d/f'round{it}';f.mkdir(exist_ok=True);(f/'configuration.txt').write_text(' '.join(map(str,[K[0]]+O+winner['P']))+'\n'+'\n'.join(ct)+'\n');inp=' '.join(map(str,edges+delta+[0]*26+[0]*598))
  with open(f/'paths.txt','w')as out:subprocess.run([str(b/'path-full'),'6',str(r/'batches/kryha-two-mask-refine-sol61/model6.tsv'),str(f/'configuration.txt')],input=inp,text=True,stdout=out,check=True)
  paths=[]
  for line in (f/'paths.txt').read_text().splitlines()[1:]:
   a=list(map(int,line.split()[1:]));paths.append([a[::2],a[1::2]])
  pro=project(paths,O,K);(f/'projected.txt').write_text('\n'.join(' '.join(p)for p in pro)+'\n');base=''
  for i,pair in enumerate(pro):base+=f'{i} 0\n'+' '.join(map(str,winner['P']))+'\n'+'\n'.join(''.join(chr(97+winner['P'][ord(x)-97])for x in s)for s in pair)+'\n'
  (f/'fixedP.txt').write_text(base)
  with open(f/'reranked.txt','w')as out:subprocess.run([str(b/'rerank'),str(r/'batches/kryha-two-mask-refine-sol61'),str(f/'projected.txt'),str(f/'fixedP.txt')],stdout=out,check=True)
  new=ranked(f/'reranked.txt');new['masks']=paths[new['id']];history.append(new);print(info['gauge'],it,new['score'],flush=True)
  if new['score']<=winner['score']+1e-8:break
  winner=new
 winner=dict(winner);winner.update(gauge=info['gauge'],O=O,K=K,history=history);results.append(winner)
results.sort(key=lambda x:x['score'],reverse=True);(b/'second-blind-ranked.json').write_text(json.dumps(results,indent=2)+'\n');print('Blind final ranking saved; truth not loaded.',flush=True)
