from pathlib import Path
import json,random,unicodedata,subprocess
b=Path(__file__).resolve().parent;r=b.parents[1];key=json.load(open(b/'transferred-key.json'));baseP=key['P'];baseO=key['O'];edges=key['adjacent_distances'];coord=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'))['unwrapped_effective_coordinates'];ns={'digits':['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'],'unicodedata':unicodedata};s=(r/'batches/kryha-mask-sol61/prepare.py').read_text();exec(s[s.index('def prep('):s.index('train=r/')],ns);prep=ns['prep'];exc={prep(z)for z in (r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().strip().split('\n\n')};stream=''.join(prep(z)for z in (r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().strip().split('\n\n')if prep(z)not in exc)
def run(cfg,inp,out):
 subprocess.run([str(b/'beam-direction'),str(cfg),str(inp),'23','128',str(r),str(out)],check=True);return sorted((x.split()for x in out.read_text().splitlines()),key=lambda x:float(x[0]),reverse=True)
def verify(ct,row,P,O,S):
 score,a,d,hs,pt=row;h=[int(x)for x in hs.split(',')if x];d=int(d);assert len(set(h))==23 and sum((h[(i+1)%23]-h[i])%52 for i in range(23))==52;invP={x:i for i,x in enumerate(P)};invO={x:i for i,x in enumerate(O)};dec=''
 for i,c in enumerate(ct):
  j=i%23;D=coord[h[j]]-coord[h[0]]+179*(h[j]<h[0])+179*(i//23);dec+=chr(97+P[(O[ord(c)-97]-d-S*D)%26])
 assert dec==pt;back='';cur=d
 for i,c in enumerate(pt):
  back+=chr(97+invO[(invP[ord(c)-97]+cur)%26]);x=h[i%23];y=h[(i+1)%23]
  while x!=y:cur+=S*edges[x];x=(x+1)%52
 assert back==ct
 return dict(score=float(score),P=P,O=O,displacement_sign=S,holes=h,initial_displacement=d,plaintext=pt,independent_inverse_and_reencryption=True)
records=[]
for idx,(swap,S)in enumerate([(False,1),(False,-1),(True,1),(True,-1)]):
 label=f'direction-swap{int(swap)}-sign{S}';P=baseP;O=baseO
 if swap:
  P=[baseO.index(i)for i in range(26)];O=[baseP.index(i)for i in range(26)]
 cfg=b/(label+'-cfg.txt');cfg.write_text(' '.join(map(str,P+O+coord+[S]))+'\n');rng=random.Random(37485230+idx);h=sorted(rng.sample(range(52),23));phase=rng.randrange(23);h=h[phase:]+h[:phase];d0=rng.randrange(26);d=d0;off=58000+idx*200;pt=stream[off:off+85].replace('j','i').replace('x','j');assert len(pt)==85;invP={x:i for i,x in enumerate(P)};invO={x:i for i,x in enumerate(O)};ct=''
 for i,c in enumerate(pt):
  ct+=chr(97+invO[(invP[ord(c)-97]+d)%26]);x=h[i%23];y=h[(i+1)%23]
  while x!=y:d+=S*edges[x];x=(x+1)%52
 verify(ct,['0',str(h[0]),str(d0),','.join(map(str,h))+',',pt],P,O,S);inp=b/(label+'-control.txt');inp.write_text(ct+'\n');qs=run(cfg,inp,b/(label+'-control-beam.txt'));best=verify(ct,qs[0],P,O,S);rec=dict(label=label,seed=37485230+idx,TEST_offset=off,control=dict(plaintext=pt,ciphertext=ct,holes=h,initial_displacement=d0),blind_best=best,whole_exact=best['plaintext']==pt,correct_letters=sum(x==y for x,y in zip(best['plaintext'],pt)),exact_coverage_ranks=[i for i,x in enumerate(qs)if x[-1]==pt]);print(label,rec['whole_exact'],rec['correct_letters'],flush=True)
 if rec['whole_exact']:
  inp=b/'target-G1-Q1-V1.txt';qs=run(cfg,inp,b/(label+'-target-beam.txt'));rec['target_candidates']=[verify(inp.read_text().strip(),q,P,O,S)for q in qs[:20]];print('target',rec['target_candidates'][0]['plaintext'],flush=True)
 records.append(rec)
(b/'direction-results.json').write_text(json.dumps(records,indent=2)+'\n')
