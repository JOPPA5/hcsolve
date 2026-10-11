from pathlib import Path
import json,itertools
b=Path(__file__).resolve().parent;r=b.parents[2];models={}
for n in (4,5):models[n]={s:float(v) for s,v in (line.split() for line in (r/f'ciphers/hcp-350/work/ring-{n}grams.tsv').read_text().splitlines())}
ns={'__file__':str(b/'run.py')};source=(b/'run.py').read_text();exec(source[:source.index('with concurrent.futures')],ns)
records=[];controls={c['label']:c for c in json.load(open(b/'controls.json'))};folders=[b/label for label in controls]
if (b/'targets.json').exists():folders+=[b/x['label'] for x in json.load(open(b/'targets.json')) if (b/x['label']/'result5.json').exists()]
for folder in folders:
 ct=(folder/'cipher.txt').read_text().strip();steps=list(map(int,(folder/'schedule.txt').read_text().split()));offsets=[];d=0
 for i in range(len(ct)):offsets.append(d);d=(d+steps[i%len(steps)])%26
 for stage in ('result4','result5'):
  if not (folder/(stage+'.json')).exists():continue
  winner=json.load(open(folder/(stage+'.json')));P=winner['input_slots'];O=winner['output_positions'];rows=[]
  for pair in [None,*itertools.combinations(range(26),2)]:
   key=P[:]
   if pair:key[pair[0]],key[pair[1]]=key[pair[1]],key[pair[0]]
   plain=''.join(chr(97+key[(O[ord(c)-97]-offsets[i])%26]) for i,c in enumerate(ct));rec={'swap':pair,'input_slots':key,'output_positions':O,'plaintext':plain,'score4':sum(models[4].get(plain[i:i+4],-4) for i in range(len(plain)-3)),'score5':sum(models[5].get(plain[i:i+5],-5) for i in range(len(plain)-4))};ns['verify'](rec,ct,list(map(int,(folder/'schedule.txt').read_text().split())));rows.append(rec)
  rows.sort(key=lambda z:z['score5'],reverse=True);(folder/(stage+'-coverage.json')).write_text(json.dumps(rows,indent=2)+'\n');summary={'label':folder.name,'stage':stage,'candidates':len(rows),'all_reencryptions_passed':True,'selection':'all325input swaps and unchanged key, output fixed; generic5gram rank'}
  if folder.name in controls:summary['exact_plaintext_ranks5']=[i for i,x in enumerate(rows) if x['plaintext']==controls[folder.name]['plaintext']]
  records.append(summary)
(b/'coverage-summary.json').write_text(json.dumps(records,indent=2)+'\n');print(json.dumps(records,indent=2))
