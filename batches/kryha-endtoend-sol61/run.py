from pathlib import Path
import json,subprocess,math
b=Path(__file__).resolve().parent;r=b.parents[1]
ct=json.loads((b/'pilot-pair.json').read_text());rows=json.loads((b/'pilot-ransac.json').read_text())['rows'];geo=json.loads((r/'batches/kryha-wheel-sol61/wheel52.json').read_text());edges=geo['adjacent_distances'];coords=geo['unwrapped_effective_coordinates'];lp=[0.]*26
for line in (r/'ciphers/hcp-350/work/ring-unigrams.tsv').read_text().splitlines():
 ch,v=line.split();lp[ord(ch)-97]=float(v)
(b/'dummy.txt').write_text('a\na\n');(b/'zero.txt').write_text(' '.join(['0']*26))
summary=[]
for rid,row in enumerate(rows):
 O=row['output_positions'];K=row['shifts_by_absolute_residue'];delta=[(K[(j+1)%23]-K[j])%26 for j in range(23)];d=b/f'pilot-gauge{rid}';d.mkdir(exist_ok=True)
 inp=' '.join(map(str,[23]+edges+delta));res=subprocess.check_output([str(b/'fit_dp')],input=inp,text=True);(d/'feasibility.txt').write_text(res);summary.append(dict(gauge=rid,feasible=res.startswith('YES')))
 if not res.startswith('YES'):continue
 H=[[0]*26 for _ in range(23)]
 for i in range(384):
  H[i%23][(O[ord(ct[0][i])-97]-23*(i//23))%26]+=1
  H[i%23][(O[ord(ct[1][i+1])-97]-23*(i//23)-K[i%23])%26]+=1
 values=edges+delta+lp+[x for h in H for x in h];data=' '.join(map(str,values));(d/'profile-input.txt').write_text(data)
 with open(d/'profile.txt','w') as out:subprocess.run([str(b/'enumerate-profile'),'-1'],input=data,text=True,stdout=out,check=True)
 lines=(d/'profile.txt').read_text().splitlines();summary[-1]['paths']=int(lines[0].split()[1]);print(rid,lines[0],flush=True)
 paths=[];projected=[]
 for line in lines[1:]:
  nums=list(map(int,line.split()[1:]));h=[nums[::2],nums[1::2]];paths.append(h);messages=[]
  for side in range(2):
   text=''
   for i,ch in enumerate(ct[side]):
    t=i-side;j=t%23;D=coords[h[side][j]]-coords[h[side][0]]+179*(h[side][j]<h[side][0])+179*(t//23)+(K[0] if side else 0);text+=chr(97+(O[ord(ch)-97]-D)%26)
   messages.append(text)
  projected.append(' '.join(messages))
 (d/'paths.json').write_text(json.dumps(paths));(d/'derived-row.json').write_text(json.dumps(row));(d/'projected.txt').write_text('\n'.join(projected)+'\n')
 with open(d/'masc.txt','w') as out:subprocess.run([str(b/'masc'),str(b/'dummy.txt'),str(b/'zero.txt'),str(r/'batches/kryha-mask-sol61'),str(r/'ciphers/hcp-350/work'),str(d/'projected.txt')],stdout=out,check=True)
 with open(d/'reranked.txt','w') as out:subprocess.run([str(b/'rerank'),str(r/'batches/kryha-two-mask-refine-sol61'),str(d/'projected.txt'),str(d/'masc.txt')],stdout=out,check=True)
 print('gauge completed',rid,flush=True)
(b/'pilot-feasibility-summary.json').write_text(json.dumps(summary,indent=2))
