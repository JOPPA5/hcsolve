from pathlib import Path
import json,random
b=Path(__file__).resolve().parent;base=json.loads(Path('batches/r364-review-collation-sol61/variants.json').read_text())['four_sentence_X_template64']
for j,at in enumerate([0,37,64]):
 rng=random.Random(617364161901+j);n=rng.randrange(1,15);p=base[:at]+'x'+base[at:];keys=[];c=p
 for stage in range(3):
  k=rng.sample(range(1,16),15);k.insert(n+stage-1,0);keys.append(k);c=''.join(c[i]for col in k for i in range(col,len(c),16))
 alt=list(c);u=c.index('u');v=c.index('v');alt[u],alt[v]=alt[v],alt[u];alt=''.join(alt);variants=[alt,c]if j%2 else[c,alt]
 (b/f'control{j}-input.json').write_text(json.dumps(dict(template=base,cipher_variants=variants,widths=[16]*3,alignment_hypothesis='unknown progressive n,n+1,n+2; no wrap; n1..14'),indent=2)+'\n');(b/f'control{j}-truth.json').write_text(json.dumps(dict(keys=keys,plaintext=p,ciphertext=c,alignment=n,insertion=at),indent=2)+'\n')
print('3 fresh blind progressive fixtures; n/keys/insertions quarantined separately.')
