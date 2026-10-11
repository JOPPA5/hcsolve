from codec import *
import sys,time,subprocess
folder=Path(sys.argv[1]).resolve();m=int(sys.argv[2]);assert 20<=m<=30 and m!=26;ctfile=folder/'ciphertexts.txt';start=time.monotonic()
def command(binary,args,path):
 if not path.exists():
  with path.with_suffix('.partial').open('w')as out:subprocess.run([str(B/binary)]+list(map(str,args)),stdout=out,check=True)
  path.with_suffix('.partial').rename(path)
 return path.read_text().splitlines()
def parse(lines):
 key=list(map(int,lines[1].split()));assert len(key)==52;return dict(score=float(lines[0]),input_slots=key[:26],output_positions=key[26:],plaintexts=lines[2:4])
# This optimizer never opens plant.json or uses any control key/text.
dummyholes=[(52*i)//m for i in range(m)];dummy=folder/'dummy-schedule.txt';dummy.write_text(' '.join(map(str,schedule(dummyholes)))+'\n')
command('pair-cycle',[ctfile,m,2,32,20000],folder/'pair-cycle.tsv');print('cycle complete',m,flush=True)
command('pair-mask-profile',[ctfile,B/'coordinates.txt',LARGE/'ring-unigrams.tsv',folder/'pair-cycle.tsv',m],folder/'mask-profiles.tsv');print('physical profiles complete',m,flush=True)
lines=command('pair-bridge-masc',[ctfile,dummy,SMALL,LARGE,folder/'mask-profiles.tsv',B/'coordinates.txt',m],folder/'bridge-masc.txt');profiles=(folder/'mask-profiles.tsv').read_text().splitlines();assert len(profiles)==256 and len(lines)==5*len(profiles);rows=[]
for i,line in enumerate(profiles):
 ix,restart,prof,h,key=line.split('\t');z=parse(lines[5*i+1:5*i+5]);z.update(holes=list(map(int,h.rstrip(',').split(','))),profile=float(prof),cycle_index=int(ix),mask_restart=int(restart),count=m);rows.append(z)
rows.sort(key=lambda z:z['score'],reverse=True);(folder/'bridge-ranked.json').write_text(json.dumps(rows,indent=2));print('MASC top',m,rows[0]['score'],flush=True);results=[]
for seed,current in enumerate(rows[:4]):
 sfolder=folder/f'bridge-seed{seed}';sfolder.mkdir(exist_ok=True);(sfolder/'initial.json').write_text(json.dumps(current,indent=2))
 for iteration in range(4):
  stage=sfolder/f'iteration{iteration}';stage.mkdir(exist_ok=True);ringfile=stage/'rings-before.txt';ringfile.write_text(' '.join(map(str,current['input_slots']+current['output_positions']))+'\n');candidates=[]
  for line in command('pair-mask',[ctfile,64,ringfile,B/'coordinates.txt',SMALL,LARGE,m],stage/'beam.tsv'):
   anchor,rank,sc,key,p0,p1=line.split('\t');candidates.append(dict(score=float(sc),holes=list(map(int,key.split(','))),plaintexts=[p0,p1]))
  top=max(candidates,key=lambda z:z['score'])
  if current['score']>top['score']:top=current
  schedulefile=stage/'schedule.txt';schedulefile.write_text(' '.join(map(str,schedule(top['holes'])))+'\n');z=parse(command('pair-joint',[ctfile,schedulefile,SMALL,LARGE,ringfile,30000],stage/'joint.txt'));z.update(holes=top['holes'],seed_rank=seed,iteration=iteration,count=m,selection='complete boundary-separated frozen TRAIN2/3/4/5gram sum only',mask_rings_start_unknown=True);current=z;(stage/'result.json').write_text(json.dumps(z,indent=2));print('bridge',m,seed,iteration,z['score'],flush=True)
 results.append(current)
(folder/'bridge-results.json').write_text(json.dumps(results,indent=2));(folder/'run-completion.json').write_text(json.dumps(dict(complete=True,count=m,seconds=time.monotonic()-start,planted_keys_read=False),indent=2))
