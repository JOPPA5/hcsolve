from pathlib import Path
import json,subprocess,time,concurrent.futures
b=Path(__file__).resolve().parent;r=b.parents[1];model=r/'ciphers/hcp-350/work'
def parse(lines):return {'language_score':float(lines[0].split()[0]),'plaintext':lines[0].split()[1],'input_slots':[int(x) for x in lines[1].split(',') if x],'output_positions':[int(x) for x in lines[2].split(',') if x]}
def verify(rec,ct):
 P=rec['input_slots'];O=rec['output_positions'];assert sorted(P)==sorted(O)==list(range(26));assert ''.join(chr(97+P[(O[ord(c)-97]-i)%26]) for i,c in enumerate(ct))==rec['plaintext'];I={c:i for i,c in enumerate(P)};oi={v:c for c,v in enumerate(O)};assert ''.join(chr(97+oi[(I[ord(c)-97]+i)%26]) for i,c in enumerate(rec['plaintext']))==ct
 rec['independent_full_inverse_and_reencryption_passed']=True
 return rec
def work(control):
 folder=b/control['label'];ct=control['ciphertext'];file=folder/'cipher.txt';start=time.monotonic()
 def command(binary,args,name):
  path=folder/name
  if not path.exists():
   with path.with_suffix('.partial').open('w') as f:subprocess.run([str(b/binary)]+list(map(str,args)),stdout=f,stderr=open(folder/(name+'.log'),'w'),check=True)
   path.with_suffix('.partial').rename(path)
  return path.read_text().splitlines()
 profile=command('profile',[file,0,1,3000,model/'ring-unigrams.tsv'],'profile.txt');lines=command('masc',[model,file,0,1,folder/'profile.txt'],'masc.txt');assert len(lines)==len(profile)*4;rows=[]
 for j in range(len(profile)):
  assert int(lines[4*j].split()[0])==j;rec=verify(parse(lines[4*j+1:4*j+4]),ct);rec.update(candidate_index=j,profile_score=float(profile[j].split()[0]));rows.append(rec)
 rows.sort(key=lambda x:x['language_score'],reverse=True);(folder/'ranked.json').write_text(json.dumps(rows,indent=2)+'\n');top=rows[0];(folder/'seed.txt').write_text(' '.join(map(str,top['input_slots']+top['output_positions']))+'\n');final=verify(parse(command('joint',[model,file,0,1,folder/'seed.txt'],'joint.txt')),ct);final.update(label=control['label'],length=len(ct),candidate_count=len(rows),seed_selection='highest generic frozen TRAIN4gram score; no key/plaintext evaluation used',seconds=time.monotonic()-start,exact_plaintext=final['plaintext']==control.get('plaintext',''),matching_letters=sum(a==z for a,z in zip(final['plaintext'],control.get('plaintext',''))),planted_keys_not_passed_to_optimizer=True,masc_top_score=top['language_score']);
 if 'plaintext' not in control:
  final.pop('exact_plaintext');final.pop('matching_letters')
 (folder/'result.json').write_text(json.dumps(final,indent=2)+'\n');print(control['label'],final.get('matching_letters','unjudged'),final['length'],final['language_score'],flush=True);return final
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(work,json.load(open(b/'controls.json'))))
(b/'results.json').write_text(json.dumps(results,indent=2)+'\n')
