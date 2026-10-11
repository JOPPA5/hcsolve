from pathlib import Path
import json,random,subprocess,collections,math
b=Path(__file__).resolve().parent;base=b.parent;r=base.parents[1];logs=sorted(float(l.split()[1]) for l in (r/'ciphers/hcp-350/work/ring-unigrams.tsv').read_text().splitlines());results=[]
for control in [base,base/'framing355-control']:
 name='control385' if control==base else 'control355';t=json.load(open(control/'control.json'));rng=random.Random(52771702);keys=[('truth',t['output_positions'])]
 for i in range(32):O=list(range(26));rng.shuffle(O);keys.append((f'null{i}',O))
 for line in (control/'pair-cycle.tsv').read_text().splitlines():
  ix,sc,key=line.split('\t');keys.append((f'old{ix}',list(map(int,key.split(',')))))
 path=b/f'{name}-diagnostic-keys.txt';path.write_text(''.join(label+' '+','.join(map(str,O))+'\n' for label,O in keys));out=b/f'{name}-diagnostic.tsv'
 with out.open('w') as f:subprocess.run([str(b/'latent'),str(control/'ciphertexts.txt'),str(r/'ciphers/hcp-350/work/ring-unigrams.tsv'),str(path)],stdout=f,check=True)
 rows=[];cts=(control/'ciphertexts.txt').read_text().split()
 for line in out.read_text().splitlines():
  label,sc,key,sh=line.split('\t');O=list(map(int,key.rstrip(',').split(',')));sh=list(map(int,sh.rstrip(',').split(',')));N=collections.Counter()
  for ct in cts:
   for i,c in enumerate(ct):N[(O[ord(c)-97]-23*(i//26)-sh[i%26])%26]+=1
  counts=sorted(N[i] for i in range(26));v=sum(n*l-math.lgamma(n+1) for n,l in zip(counts,logs));assert abs(v-float(sc))<.012;rows.append(dict(label=label,score=v))
 true=rows[0]['score'];null=[z['score'] for z in rows if z['label'].startswith('null')];old=[z['score'] for z in rows if z['label'].startswith('old')];results.append(dict(control=name,true_fixed_ring_optimized_latent=true,null_min=min(null),null_max=max(null),null_mean=sum(null)/len(null),old_min=min(old),old_max=max(old),all_rows_independently_checked=len(rows),interpretation='landscape only; truth ring never a blind seed'))
(b/'diagnostic.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
