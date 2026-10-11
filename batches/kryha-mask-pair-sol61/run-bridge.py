from pathlib import Path
# Reuse only helper definitions, not execution of the earlier random-mask search.
b=Path(__file__).resolve().parent
exec((b/'run.py').read_text().split('# Reads ciphertext/geometry/models only.')[0])
lines=command('pair-bridge-masc',[ctfile,b/'guess0/initial-schedule.txt',small,large,b/'mask-profiles.tsv',b/'coordinates.txt'],b/'bridge-masc.txt');profiles=(b/'mask-profiles.tsv').read_text().splitlines();assert len(lines)==5*len(profiles);rows=[]
for i,line in enumerate(profiles):
 ix,restart,prof,h,key=line.split('\t');z=parse(lines[5*i+1:5*i+5]);z.update(holes=list(map(int,h.rstrip(',').split(','))),profile=float(prof),cycle_index=int(ix),mask_restart=int(restart));rows.append(z)
rows.sort(key=lambda z:z['score'],reverse=True);(b/'bridge-ranked.json').write_text(json.dumps(rows,indent=2)+'\n');print('bridge top MASC',rows[0]['score'],flush=True)
# Four seeds selected solely by complete language score, with no planted-key access.
results=[]
for i,current in enumerate(rows[:4]):
 folder=b/f'bridge-seed{i}';folder.mkdir(exist_ok=True);(folder/'initial.json').write_text(json.dumps(current,indent=2)+'\n')
 for iteration in range(4):
  stage=folder/f'iteration{iteration}';stage.mkdir(exist_ok=True);ringfile=stage/'rings-before.txt';ringfile.write_text(' '.join(map(str,current['input_slots']+current['output_positions']))+'\n');candidates=[]
  for line in command('pair-mask',[ctfile,64,ringfile,b/'coordinates.txt',small,large],stage/'beam.tsv'):
   anchor,rank,score,key,p0,p1=line.split('\t');candidates.append(dict(score=float(score),holes=list(map(int,key.split(','))),plaintexts=[p0,p1]))
  top=max(candidates,key=lambda z:z['score'])
  if current['score']>top['score']:top=current
  sf=stage/'schedule.txt';sf.write_text(' '.join(map(str,schedule(top['holes'])))+'\n');z=parse(command('pair-joint',[ctfile,sf,small,large,ringfile,30000],stage/'joint.txt'));z.update(holes=top['holes'],seed_rank=i,iteration=iteration);current=z;(stage/'result.json').write_text(json.dumps(z,indent=2)+'\n');print('bridge',i,iteration,z['score'],flush=True)
 results.append(current)
(b/'bridge-results.json').write_text(json.dumps(results,indent=2)+'\n')
