from pathlib import Path
import json,subprocess,sys
b=Path(__file__).resolve().parent;r=b.parents[1];model=r/'ciphers/hcp-350/work';results=[]
# Import codec helpers only; do not trigger previous search.
ns={'__file__':str(b/'run.py')};source=(b/'run.py').read_text();exec(source[:source.index('with concurrent.futures')],ns)
for c in json.load(open(b/('targets.json' if len(sys.argv)>1 else 'controls.json'))):
 folder=b/c['label'];old=json.load(open(folder/'result.json'));seed=folder/'seed5.txt';seed.write_text(' '.join(map(str,old['input_slots']+old['output_positions']))+'\n')
 with (folder/'joint5.txt').open('w') as f:subprocess.run([str(b/'joint5'),str(model),str(folder/'cipher.txt'),'0','1',str(seed)],stdout=f,check=True)
 z=ns['verify'](ns['parse']((folder/'joint5.txt').read_text().splitlines()),c['ciphertext']);z.update(label=c['label'],length=c['length'],seed_selection='unchanged operative4gram final winner for EVERY control; no truth/key-based choice',objective='frozen TRAIN5gram',exact_plaintext=z['plaintext']==c.get('plaintext',''),matching_letters=sum(a==v for a,v in zip(z['plaintext'],c.get('plaintext',''))));
 if 'plaintext' not in c:
  z.pop('exact_plaintext');z.pop('matching_letters')
 results.append(z);(folder/'result5.json').write_text(json.dumps(z,indent=2)+'\n');print(c['label'],z.get('matching_letters','unjudged'),z['length'],flush=True)
(b/('target-results5.json' if len(sys.argv)>1 else 'results5.json')).write_text(json.dumps(results,indent=2)+'\n')
