from pathlib import Path
import subprocess,json
p=Path(__file__).resolve().parent;root=p.parents[3]
controls=json.loads((p/'control-checks.json').read_text())
assert all(c['first_key_exact'] for c in controls.values())
summary={}
for glyph in ['x','a']:
 dest=p/f'target400-{glyph}-results.txt'
 with dest.open('w') as out,(p/f'target400-{glyph}-progress.txt').open('w') as err:
  subprocess.run([str(p/'search-lex'),str(root/'batches/scoring-sol61'),str(p.parent/'segmented/bigrams.tsv'),str(p.parent/f'cipher-{glyph}.txt')],stdout=out,stderr=err,check=True)
 parts=dest.read_text().split();k1=[int(x) for x in parts[1].split('=')[1].split(',') if x];k2=[int(x) for x in parts[2].split('=')[1].split(',') if x];plain=parts[3];ct=plain
 for key in [k1,k2]:ct=''.join(ct[j::20] for j in key)
 assert ct==(p.parent/f'cipher-{glyph}.txt').read_text().strip()
 # Each ciphertext20chunk is an unknown plaintext row; undo only recovered first-key hypothesis.
 inverse=[k1.index(i) for i in range(20)];cipher=ct
 rows=[''.join(cipher[r*20+c] for c in inverse) for r in range(20)]
 (p/f'target400-{glyph}-rows.txt').write_text('\n'.join(f'{i:02d} {s}' for i,s in enumerate(rows))+'\n')
 summary[glyph]={'result':dest.read_text().strip(),'full_reencryption':True,'full_control_failed':True,'negative_family_exclusion':False}
 print(glyph,summary[glyph]['result'],flush=True)
(p/'target-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
