from pathlib import Path
import json,subprocess,time
# Reuse independently verified codecs; no search or generation is triggered.
exec((Path(__file__).parent/'run.py').read_text().split("digits=['nula'")[0])
out=[]
for label in ['fresh385-sign1','fresh365-sign-1']:
 src=next(json.loads(x) for x in (P/'results.jsonl').read_text().splitlines() if json.loads(x)['label']==label);folder=P/'fivegram-from4'/label;folder.mkdir(parents=True,exist_ok=True);seed=folder/'seed.txt';seed.write_text(' '.join(map(str,src['input_slots']+src['output_positions']))+'\n');cipher=folder/'cipher.txt';ct=src['planted']['ciphertext'];cipher.write_text(ct+'\n');start=time.monotonic()
 with (folder/'refine.txt').open('w') as f:subprocess.run([str(R/'batches/kryha-framing-sol61/ring_ic_refine5'),str(M),str(cipher),str(src['phase']),'1',str(seed)],stdout=f,check=True)
 r=parse((folder/'refine.txt').read_text());verify(r,ct,src['phase']);r.update(label=label,seconds=time.monotonic()-start,seed_selection='unchanged operative4gram final language winner; no truth/key-based choice',phase=src['phase'],exact_plaintext=r['plaintext']==src['planted']['plaintext'],matching_letters=sum(a==b for a,b in zip(r['plaintext'],src['planted']['plaintext'])),length=src['length'],marker_scan=markers(),objective='standalone frozen5gram',truth_used_for_selection=False);(folder/'result.json').write_text(json.dumps(r,indent=2)+'\n');out.append(r);(P/'results5-from4.json').write_text(json.dumps(out,indent=2)+'\n');print(label,r['matching_letters'],r['length'],r['language_score'],r['seconds'],flush=True)
