from pathlib import Path
import json,random,unicodedata,subprocess
b=Path(__file__).resolve().parent;r=b.parents[1];ns={'digits':['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'],'unicodedata':unicodedata};s=(r/'batches/kryha-mask-sol61/prepare.py').read_text();exec(s[s.index('def prep('):s.index('train=r/')],ns);prep=ns['prep'];exc={prep(z)for z in (r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().strip().split('\n\n')};text=''.join(prep(z)for z in (r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().strip().split('\n\n')if prep(z)not in exc);key=json.load(open(b/'transferred-key.json'));P=key['P'];O=key['O'];edges=key['adjacent_distances'];invP={v:i for i,v in enumerate(P)};invO={v:i for i,v in enumerate(O)};records=[]
for m in range(20,31):
 if m==23:continue
 rng=random.Random(3748500+m);h=sorted(rng.sample(range(52),m));phase=rng.randrange(m);h=h[phase:]+h[:phase];d0=rng.randrange(26);d=d0;plain=text[47000+m*100:47085+m*100];ct=''
 for i,c in enumerate(plain):
  ct+=chr(97+invO[(invP[ord(c)-97]+d)%26]);x=h[i%m];y=h[(i+1)%m]
  while x!=y:d+=edges[x];x=(x+1)%52
 label=f'control-m{m}';inp=b/(label+'.txt');out=b/(label+'-beam128.txt');inp.write_text(ct+'\n');subprocess.run([str(b/'beam'),str(b/'known-rings-coordinates.txt'),str(inp),str(m),'128',str(r),str(out)],check=True);qs=sorted((x.split()for x in out.read_text().splitlines()),key=lambda x:float(x[0]),reverse=True);best=qs[0];records.append(dict(m=m,seed=3748500+m,TEST_offset=47000+m*100,plaintext=plain,ciphertext=ct,holes=h,initial_displacement=d0,best=best,whole_exact=best[-1]==plain,correct_letters=sum(x==y for x,y in zip(best[-1],plain)),exact_coverage_ranks=[i for i,x in enumerate(qs)if x[-1]==plain]));print(m,records[-1]['whole_exact'],records[-1]['correct_letters'],flush=True)
(b/'count-controls.json').write_text(json.dumps(records,indent=2)+'\n')
