from pathlib import Path
import json,math
b=Path(__file__).resolve().parent;ns={'__file__':str(b/'run.py')};source=(b/'run.py').read_text();exec(source[:source.index('with concurrent.futures')],ns);manifest=json.load(open(b/'manifest.json'));logs=sorted(float(line.split()[1]) for line in Path(manifest['model_files']['ring-unigrams.tsv']).read_text().splitlines());counts={'profile_independent_rescores':0,'MASC_full_reencryptions':0,'joint_full_reencryptions':0,'neighbor_full_reencryptions':0};inspection=[]
for control in json.load(open(b/'controls.json'))+json.load(open(b/'targets.json')):
 folder=b/control['label'];ct=control['ciphertext']
 for line in (folder/'profile.txt').read_text().splitlines():
  sc,key=line.split();O=list(map(int,key.rstrip(',').split(',')));assert sorted(O)==list(range(26));N=[0]*26
  for i,c in enumerate(ct):N[(O[ord(c)-97]-i)%26]+=1
  score=sum(n*p-math.lgamma(n+1) for n,p in zip(sorted(N),logs));assert abs(score-float(sc))<.02;counts['profile_independent_rescores']+=1
 for rec in json.load(open(folder/'ranked.json')):ns['verify'](rec,ct);counts['MASC_full_reencryptions']+=1
 for stage in ('result','result5'):
  rec=json.load(open(folder/(stage+'.json')));ns['verify'](rec,ct);counts['joint_full_reencryptions']+=1;inspection.append(control['label']+' '+stage+'\n'+rec['plaintext']+'\n')
  coverage=json.load(open(folder/(stage+'-coverage.json')));assert len(coverage)==326
  for rec in coverage:ns['verify'](rec,ct);counts['neighbor_full_reencryptions']+=1
  inspection.append(control['label']+' '+stage+' top5gram neighbors\n'+'\n'.join(x['plaintext'] for x in coverage[:4])+'\n')
counts['total_independent_full_reencryptions']=sum(v for k,v in counts.items() if k!='profile_independent_rescores');counts['cipher_marker_scan']={str(n):[p.name for p in (b.parents[1]/f'ciphers/hcp-{n}').iterdir() if p.name=='FINAL' or p.name.startswith(('DONE','REVIEWED'))] for n in (350,351,369)};(b/'checks.json').write_text(json.dumps(counts,indent=2)+'\n');(b/'inspection.txt').write_text('\n'.join(inspection));print(counts)
