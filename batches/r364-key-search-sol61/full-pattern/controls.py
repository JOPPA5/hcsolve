from pathlib import Path
import random,json,subprocess,time,hashlib
P=Path(__file__).resolve().parent;R=P.parents[2];quote='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';widths=[21,19,20];assert len(quote)==64
# Independent index-map codec, not the C++ slicing implementation.
def mapping(key,n):return [row*len(key)+col for col in key for row in range((n-col+len(key)-1)//len(key))]
def enc(plain,key):return ''.join(plain[i] for i in mapping(key,len(plain)))
def dec(cipher,key):
 out=['']*len(cipher)
 for c,i in zip(cipher,mapping(key,len(cipher))):out[i]=c
 return ''.join(out)
results=[]
for seed,filler in [(364219201,'r'),(364219204,'c')]:
 rng=random.Random(seed);plain=quote+filler;keys=[rng.sample(range(w),w) for w in widths];ct=plain
 for key in keys:ct=enc(ct,key)
 folder=P/f'control-{seed}';folder.mkdir(exist_ok=True);fixture=dict(plaintext=plain,ciphertext=ct,planted_keys=keys,widths=widths,seed=seed);(folder/'planted.json').write_text(json.dumps(fixture,indent=2)+'\n');inp=folder/'input.txt';inp.write_text(plain+'\n'+ct+'\n');truthfile=folder/'known-check-keys.txt';truthfile.write_text(' '.join(map(str,sum(keys,[])))+'\n')
 known=subprocess.check_output([str(P/'search'),str(inp),'1','1','77119',str(truthfile)],text=True).strip();assert known=='65 65 65 65';(folder/'known-key-check.txt').write_text(known+'\n')
 output=folder/'search.txt'
 if not output.exists():
  with output.open('w') as f,(folder/'progress.txt').open('w') as err:subprocess.run([str(P/'search'),str(inp),'60','1000',str(seed+6000)],stdout=f,stderr=err,check=True)
 lines=output.read_text().splitlines();score,proposals,seconds=lines[0].split();recovered_keys=[[int(x) for x in line.split(',') if x] for line in lines[1:4]];predicted=plain
 for key,w in zip(recovered_keys,widths):assert sorted(key)==list(range(w));predicted=enc(predicted,key)
 recovered=ct
 for key in reversed(recovered_keys):recovered=dec(recovered,key)
 assert predicted==lines[4] and recovered==lines[5];assert int(score)==sum(a==b for a,b in zip(predicted,ct));recovered_plain_score=sum(a==b for a,b in zip(recovered,plain));assert recovered_plain_score==int(score)
 r=dict(**fixture,recovered_keys=recovered_keys,predicted_ciphertext=predicted,inverted_ciphertext=recovered,matching_positions=int(score),exact_wholetext=int(score)==65,exact_planted_keys=recovered_keys==keys,proposals=int(proposals),seconds=float(seconds),blind_seed=seed+6000,truth_used_for_search=False,known_key_check=known,independent_encoder_matches=True,independent_inverse_matches=True,mismatch_positions=[i for i,(a,b) in enumerate(zip(predicted,ct)) if a!=b]);results.append(r);(folder/'result.json').write_text(json.dumps(r,indent=2)+'\n');(P/'results.json').write_text(json.dumps(results,indent=2)+'\n');print(seed,r['matching_positions'],r['seconds'],r['exact_planted_keys'],flush=True)
(P/'manifest.json').write_text(json.dumps(dict(widths=widths,known_plaintext_hypothesis=quote+'{one fully known filler per control}',restarts=60,proposals_per_restart=1000,coordinate='stage21 enumerate all210height patterns + exact Hungarian; other stages conditional-height Hungarian/random pattern flips;10% ordinary key swaps',temperature='.15+1.4*(1-(iteration mod1000)/1000)',key_orientation='physical column readout order, zero-based',known_key_check_not_recovery=True,source_hashes={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in [R/'ciphers/hcp-364/source/cryptogram.jpg',R/'ciphers/hcp-364/source/metadata.md',R/'ciphers/hcp-364/work/transcription.txt']}),indent=2)+'\n')
