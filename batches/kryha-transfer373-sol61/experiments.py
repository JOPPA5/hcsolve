from pathlib import Path
import json,random,unicodedata,subprocess,hashlib
b=Path(__file__).resolve().parent;r=b.parents[1];key=json.load(open(b/'transferred-key.json'));baseP=key['P'];baseO=key['O'];edges=key['adjacent_distances'];coord=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'))['unwrapped_effective_coordinates'];ns={'digits':['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'],'unicodedata':unicodedata};s=(r/'batches/kryha-mask-sol61/prepare.py').read_text();exec(s[s.index('def prep('):s.index('train=r/')],ns);prep=ns['prep'];exc={prep(z)for z in (r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().strip().split('\n\n')};stream=''.join(prep(z)for z in (r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().strip().split('\n\n')if prep(z)not in exc)
def run(cfg,inp,out,m):
 subprocess.run([str(b/'beam-direction'),str(cfg),str(inp),str(m),'128',str(r),str(out)],check=True);return sorted((x.split()for x in out.read_text().splitlines()),key=lambda x:float(x[0]),reverse=True)
def verify(ct,row,P,O,S,m):
 score,a,d,hs,pt=row;h=[int(x)for x in hs.split(',')if x];d=int(d);assert len(set(h))==m and sum((h[(i+1)%m]-h[i])%52 for i in range(m))==52;invP={x:i for i,x in enumerate(P)};invO={x:i for i,x in enumerate(O)};dec=''
 for i,c in enumerate(ct):
  j=i%m;D=coord[h[j]]-coord[h[0]]+179*(h[j]<h[0])+179*(i//m);dec+=chr(97+P[(O[ord(c)-97]-d-S*D)%26])
 assert dec==pt;back='';cur=d
 for i,c in enumerate(pt):
  back+=chr(97+invO[(invP[ord(c)-97]+cur)%26]);x=h[i%m];y=h[(i+1)%m]
  while x!=y:cur+=S*edges[x];x=(x+1)%52
 assert back==ct
 return dict(score=float(score),m=m,P=P,O=O,displacement_sign=S,holes=h,initial_displacement=d,plaintext=pt,independent_inverse_and_reencryption=True)
records=[]
for idx,(m,swap,S)in enumerate([(20,False,1),(21,False,1),(25,False,1),(23,False,-1),(23,True,1),(23,True,-1)]):
 label=f'm{m}-swap{int(swap)}-sign{S}';P=baseP;O=baseO
 if swap:P=[baseO.index(i)for i in range(26)];O=[baseP.index(i)for i in range(26)]
 cfg=b/(label+'-cfg.txt');cfg.write_text(' '.join(map(str,P+O+coord+[S]))+'\n');rng=random.Random(37365020+idx);h=sorted(rng.sample(range(52),m));phase=rng.randrange(m);h=h[phase:]+h[:phase];d0=rng.randrange(26);d=d0;off=65000+idx*700;pt=stream[off:off+650].replace('j','i').replace('x','j');assert len(pt)==650;invP={x:i for i,x in enumerate(P)};invO={x:i for i,x in enumerate(O)};ct=''
 for i,c in enumerate(pt):
  ct+=chr(97+invO[(invP[ord(c)-97]+d)%26]);x=h[i%m];y=h[(i+1)%m]
  while x!=y:d+=S*edges[x];x=(x+1)%52
 verify(ct,['0',str(h[0]),str(d0),','.join(map(str,h))+',',pt],P,O,S,m);inp=b/(label+'-control.txt');inp.write_text(ct+'\n');control=dict(seed=37365020+idx,TEST_offset=off,plaintext=pt,ciphertext=ct,holes=h,initial_displacement=d0);(b/(label+'-planted.json')).write_text(json.dumps(control,indent=2)+'\n');qs=run(cfg,inp,b/(label+'-control-beam.txt'),m);best=verify(ct,qs[0],P,O,S,m);rec=dict(label=label,control=control,blind_best=best,whole_exact=best['plaintext']==pt,mask_exact=best['holes']==h,offset_exact=best['initial_displacement']==d0,correct_letters=sum(x==y for x,y in zip(best['plaintext'],pt)),exact_coverage_ranks=[i for i,x in enumerate(qs)if x[-1]==pt]);print(label,rec['whole_exact'],rec['correct_letters'],flush=True)
 if rec['whole_exact']:
  inp=b/'target650.txt';qs=run(cfg,inp,b/(label+'-target-beam.txt'),m);rec['target_candidates']=[verify(inp.read_text().strip(),q,P,O,S,m)for q in qs[:20]];print('target score',rec['target_candidates'][0]['score'],rec['target_candidates'][0]['plaintext'][:100],flush=True)
 records.append(rec);(b/'experiments-results.json').write_text(json.dumps(records,indent=2)+'\n')
# Save the originally calibrated m23/+ direction target too, without rerunning it.
ct=(b/'target650.txt').read_text().strip();qs=sorted((x.split()for x in (b/'target650-beam128.txt').read_text().splitlines()),key=lambda x:float(x[0]),reverse=True);out=[verify(ct,q,baseP,baseO,1,23)for q in qs[:20]];(b/'original-target-keys.json').write_text(json.dumps(out,indent=2)+'\n')
(b/'source-provenance.json').write_text(json.dumps(dict(published_context=True,new_plaintext_claim=False,portal_status='Solved',context='batches/solved-context-main/373/SOURCES.md',ciphertext_transcription_source='batches/kryha373-collation-sol61/ciphertext650.txt',ciphertext_sha256=hashlib.sha256((b/'target650.txt').read_bytes()).hexdigest(),published_plaintext_not_used_in_optimizer=True,source_readings='Preferred provisional audit transcription; ambiguous glyphs still being collated',ring_key_frozen_sha256=hashlib.sha256((b/'transferred-key.json').read_bytes()).hexdigest()),indent=2)+'\n')
