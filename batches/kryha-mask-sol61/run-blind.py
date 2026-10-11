from pathlib import Path
import json,subprocess,random,concurrent.futures
b=Path(__file__).resolve().parent;r=b.parents[1];ct=(b/'control-m26/cipher.txt').read_text().strip();m=26
# No controls.json/true rings/plaintext/mask read. Count26 is explicitly supplied.
def run(start):
 folder=b/f'blind26-start{start}';folder.mkdir(exist_ok=True);rng=random.Random(52619900+start);P=rng.sample(range(26),26);O=rng.sample(range(26),26);current=None;steps=[]
 for iteration in range(4):
  stage=folder/f'iteration{iteration}';stage.mkdir(exist_ok=True);rings=stage/'rings-before.txt';rings.write_text(' '.join(map(str,P+O))+'\n')
  with (stage/'beam.tsv').open('w') as out,(stage/'beam.log').open('w') as err:subprocess.run([str(b/'maskbeam'),str(b/'control-m26/cipher.txt'),str(m),'64',str(rings),str(b/'coordinates.txt'),str(b),str(r/'ciphers/hcp-350/work')],stdout=out,stderr=err,check=True)
  rows=[]
  for line in (stage/'beam.tsv').read_text().splitlines():anchor,rank,score,key,plain=line.split('\t');rows.append({'score':float(score),'holes':list(map(int,key.split(','))),'plaintext':plain})
  top=max(rows,key=lambda z:z['score'])
  if current and current['score']>top['score']:top=current
  holes=stage/'chosen-holes.txt';holes.write_text(' '.join(map(str,top['holes']))+'\n')
  with (stage/'joint.txt').open('w') as out:subprocess.run([str(b/'ringjoint'),str(b/'control-m26/cipher.txt'),str(rings),str(holes),str(b/'coordinates.txt'),str(b),str(r/'ciphers/hcp-350/work'),'30000'],stdout=out,check=True)
  lines=(stage/'joint.txt').read_text().splitlines();key=list(map(int,lines[1].split()));P=key[:26];O=key[26:];current={'score':float(lines[0]),'holes':top['holes'],'plaintext':lines[2],'input_slots':P,'output_positions':O};current.update(start=start,iteration=iteration,chosen_by='whole frozen2/3/4/5gram score only',m_supplied=26,mask_and_rings_unknown=True);steps.append(current);(stage/'result.json').write_text(json.dumps(current,indent=2)+'\n');print(start,iteration,current['score'],flush=True)
 (folder/'steps.json').write_text(json.dumps(steps,indent=2)+'\n');return current
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(run,range(8)))
(b/'blind-results.json').write_text(json.dumps(results,indent=2)+'\n')
