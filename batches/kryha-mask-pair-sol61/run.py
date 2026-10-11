from pathlib import Path
import json,random,subprocess,concurrent.futures,time
b=Path(__file__).resolve().parent;r=b.parents[1];geometry=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=geometry['adjacent_distances'];ctfile=b/'ciphertexts.txt';small=r/'batches/kryha-mask-sol61';large=r/'ciphers/hcp-350/work'
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
  with path.with_suffix('.partial').open('w') as out:subprocess.run([str(b/binary)]+list(map(str,args)),stdout=out,check=True)
  path.with_suffix('.partial').rename(path)
 return path.read_text().splitlines()
def work(number):
 folder=b/f'guess{number}';folder.mkdir(exist_ok=True);start=time.monotonic();rng=random.Random(52770900+number)
 if number<2:holes=list(range(number,52,2))
 else:holes=sorted(rng.sample(range(52),26));phase=rng.randrange(26);holes=holes[phase:]+holes[:phase]
 sf=folder/'initial-schedule.txt';sf.write_text(' '.join(map(str,schedule(holes)))+'\n');(folder/'initial-mask.json').write_text(json.dumps({'ordered_holes':holes,'seed':52770900+number,'method':'regular even/odd or independent random selected holes; no control key access'},indent=2)+'\n')
 profiles=command('pair-profile',[ctfile,0,1,1000,large/'ring-unigrams.tsv',sf],folder/'profiles.txt');lines=command('pair-masc',[ctfile,sf,small,large,folder/'profiles.txt'],folder/'masc.txt');assert len(lines)==len(profiles)*5;rows=[]
 for j in range(len(profiles)):
  assert int(lines[j*5].split()[0])==j;z=parse(lines[j*5+1:j*5+5]);z.update(profile_index=j,profile_score=float(profiles[j].split()[0]),holes=holes);rows.append(z)
 rows.sort(key=lambda z:z['score'],reverse=True);(folder/'ranked.json').write_text(json.dumps(rows,indent=2)+'\n');current=rows[0];(folder/'language-selected-seed.json').write_text(json.dumps(current,indent=2)+'\n');print('guess',number,'MASCseed',current['score'],flush=True);steps=[]
 for iteration in range(4):
  stage=folder/f'iteration{iteration}';stage.mkdir(exist_ok=True);ringfile=stage/'rings-before.txt';ringfile.write_text(' '.join(map(str,current['input_slots']+current['output_positions']))+'\n');lines=command('pair-mask',[ctfile,64,ringfile,b/'coordinates.txt',small,large],stage/'beam.tsv');candidates=[]
  for line in lines:anchor,rank,score,key,p0,p1=line.split('\t');candidates.append({'score':float(score),'holes':list(map(int,key.split(','))),'plaintexts':[p0,p1]})
  top=max(candidates,key=lambda z:z['score'])
  if current['score']>top['score']:top=current
  sf=stage/'schedule.txt';sf.write_text(' '.join(map(str,schedule(top['holes'])))+'\n');(stage/'chosen-mask.json').write_text(json.dumps(top['holes'])+'\n');z=parse(command('pair-joint',[ctfile,sf,small,large,ringfile,30000],stage/'joint.txt'));z.update(holes=top['holes'],guess=number,iteration=iteration,m_supplied=26,selection='whole TRAIN2/3/4/5gram language sum only; no boundary ngrams',mask_and_rings_unknown=True);current=z;steps.append(z);(stage/'result.json').write_text(json.dumps(z,indent=2)+'\n');print('guess',number,'iteration',iteration,z['score'],flush=True)
 (folder/'steps.json').write_text(json.dumps(steps,indent=2)+'\n');current.update(seconds=time.monotonic()-start);return current
# Reads ciphertext/geometry/models only. True pair data are not opened by this optimizer.
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(work,range(6)))
(b/'blind-results.json').write_text(json.dumps(results,indent=2)+'\n')
