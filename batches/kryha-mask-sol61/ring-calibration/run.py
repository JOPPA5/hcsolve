from pathlib import Path
import json,subprocess,concurrent.futures,time
b=Path(__file__).resolve().parent;r=b.parents[2];model=r/'ciphers/hcp-350/work'
def parse(lines):return {'language_score':float(lines[0].split()[0]),'plaintext':lines[0].split()[1],'input_slots':[int(v) for v in lines[1].split(',') if v],'output_positions':[int(v) for v in lines[2].split(',') if v]}
def verify(z,ct,steps):
 P=z['input_slots'];O=z['output_positions'];assert sorted(P)==sorted(O)==list(range(26));ip={v:i for i,v in enumerate(P)};op={v:c for c,v in enumerate(O)};d=0;enc='';dec=''
 for i,(pc,cc) in enumerate(zip(z['plaintext'],ct)):enc+=chr(97+op[(ip[ord(pc)-97]+d)%26]);dec+=chr(97+P[(O[ord(cc)-97]-d)%26]);d=(d+steps[i%len(steps)])%26
 assert len(z['plaintext'])==len(ct) and enc==ct and dec==z['plaintext'];z['independent_schedule_reencryption_exact']=True
 return z
def work(label):
 folder=b/label;file=folder/'cipher.txt';ct=file.read_text().strip();schedule=folder/'schedule.txt';steps=list(map(int,schedule.read_text().split()));start=time.monotonic()
 def command(binary,args,name):
  path=folder/name
  if not path.exists():
   with path.with_suffix('.partial').open('w') as out:subprocess.run([str(b/binary)]+list(map(str,args))+[str(schedule)],stdout=out,check=True)
   path.with_suffix('.partial').rename(path)
  return path.read_text().splitlines()
 profiles=command('profile',[file,0,1,3000,model/'ring-unigrams.tsv'],'profile.txt');lines=command('masc',[model,file,0,1,folder/'profile.txt'],'masc.txt');assert len(lines)==4*len(profiles);rows=[]
 for j,line in enumerate(profiles):assert int(lines[4*j].split()[0])==j;z=verify(parse(lines[4*j+1:4*j+4]),ct,steps);z.update(profile_index=j,profile_score=float(line.split()[0]));rows.append(z)
 rows.sort(key=lambda x:x['language_score'],reverse=True);(folder/'ranked.json').write_text(json.dumps(rows,indent=2)+'\n');top=rows[0];seed=folder/'seed4.txt';seed.write_text(' '.join(map(str,top['input_slots']+top['output_positions']))+'\n');final=verify(parse(command('joint',[model,file,0,1,seed],'joint4.txt')),ct,steps);final.update(label=label,stage='joint4',selection='highest TRAIN4gram MASC winner; no planted truth/key selection');(folder/'result4.json').write_text(json.dumps(final,indent=2)+'\n');seed5=folder/'seed5.txt';seed5.write_text(' '.join(map(str,final['input_slots']+final['output_positions']))+'\n');five=verify(parse(command('joint5',[model,file,0,1,seed5],'joint5.txt')),ct,steps);five.update(label=label,stage='joint5',selection='unchanged4gram winner for every case; no planted truth/key selection',seconds=time.monotonic()-start);(folder/'result5.json').write_text(json.dumps(five,indent=2)+'\n');print(label,final['language_score'],five['language_score'],flush=True);return [final,five]
# Explicit labels and cipher/schedule files only; no controls.json or true ring/word read.
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(work,('fresh-m20','fresh-m26','fresh-m30')))
(b/'results.json').write_text(json.dumps(results,indent=2)+'\n')
