from pathlib import Path
import json,random,subprocess,concurrent.futures,time
import sys
base=Path(__file__).resolve().parent;b=Path(sys.argv[1]).resolve();r=base.parents[1];geometry=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=geometry['adjacent_distances'];ctfile=b/'ciphertexts.txt';small=r/'batches/kryha-mask-sol61';large=r/'ciphers/hcp-350/work'
def schedule(holes):
 jumps=[]
 for j,h in enumerate(holes):
  x=h;d=0
  while True:
   d+=a[x];x=(x+1)%52
   if x==holes[(j+1)%26]:break
  jumps.append(d)
 assert sum(jumps)==179;return jumps
def parse(lines):
 key=list(map(int,lines[1].split()));assert len(key)==52;return {'score':float(lines[0]),'input_slots':key[:26],'output_positions':key[26:],'plaintexts':lines[2:4]}
def command(binary,args,path):
 if not path.exists():
  with path.with_suffix('.partial').open('w') as out:subprocess.run([str(base/binary)]+list(map(str,args)),stdout=out,check=True)
  path.with_suffix('.partial').rename(path)
 return path.read_text().splitlines()

command('pair-cycle',[ctfile,26,2,32,20000],b/'pair-cycle.tsv')
command('pair-mask-profile',[ctfile,base/'coordinates.txt',large/'ring-unigrams.tsv',b/'pair-cycle.tsv'],b/'mask-profiles.tsv')
lines=command('pair-bridge-masc',[ctfile,base/'guess0/initial-schedule.txt',small,large,b/'mask-profiles.tsv',base/'coordinates.txt'],b/'bridge-masc.txt');profiles=(b/'mask-profiles.tsv').read_text().splitlines();assert len(lines)==5*len(profiles);rows=[]
for i,line in enumerate(profiles):
 ix,restart,prof,h,key=line.split('\t');z=parse(lines[5*i+1:5*i+5]);z.update(holes=list(map(int,h.rstrip(',').split(','))),profile=float(prof),cycle_index=int(ix),mask_restart=int(restart));rows.append(z)
rows.sort(key=lambda z:z['score'],reverse=True);(b/'bridge-ranked.json').write_text(json.dumps(rows,indent=2)+'\n');print('bridge top MASC',rows[0]['score'],flush=True)
# Four seeds selected solely by complete language score, with no planted-key access.
results=[]
for i,current in enumerate(rows[:4]):
 folder=b/f'bridge-seed{i}';folder.mkdir(exist_ok=True);(folder/'initial.json').write_text(json.dumps(current,indent=2)+'\n')
 for iteration in range(4):
  stage=folder/f'iteration{iteration}';stage.mkdir(exist_ok=True);ringfile=stage/'rings-before.txt';ringfile.write_text(' '.join(map(str,current['input_slots']+current['output_positions']))+'\n');candidates=[]
  for line in command('pair-mask',[ctfile,64,ringfile,base/'coordinates.txt',small,large],stage/'beam.tsv'):
   anchor,rank,score,key,p0,p1=line.split('\t');candidates.append(dict(score=float(score),holes=list(map(int,key.split(','))),plaintexts=[p0,p1]))
  top=max(candidates,key=lambda z:z['score'])
  if current['score']>top['score']:top=current
  sf=stage/'schedule.txt';sf.write_text(' '.join(map(str,schedule(top['holes'])))+'\n');z=parse(command('pair-joint',[ctfile,sf,small,large,ringfile,30000],stage/'joint.txt'));z.update(holes=top['holes'],seed_rank=i,iteration=iteration);current=z;(stage/'result.json').write_text(json.dumps(z,indent=2)+'\n');print('bridge',i,iteration,z['score'],flush=True)
 results.append(current)
(b/'bridge-results.json').write_text(json.dumps(results,indent=2)+'\n')
