"""Necessary paired-message condition; NOT a general Kryha decipherment.
Same plaintext + same ring alphabets + common repeating stop schedule T implies
one fixed cipher-to-cipher bijection per residue i mod T, even if wheel phases differ.
Test all stop counts1..52, with literal transcription and explicit interior.
"""
from pathlib import Path
from collections import Counter
import json,random
P=Path(__file__).parent
x=''.join((P/'transcription.txt').read_text().lower().split())[20:375]
y=''.join((P.parents[1]/'hcp-351/work/transcription.txt').read_text().lower().split())[20:375]
assert len(x)==len(y)==355

def consistency(a,b,t):
 aa=Counter((i%t,c) for i,c in enumerate(a));bb=Counter((i%t,c) for i,c in enumerate(b));ab=Counter((i%t,c,d) for i,(c,d) in enumerate(zip(a,b)))
 pairs=lambda v:sum(n*(n-1)//2 for n in v.values())
 common=pairs(ab);ain=pairs(aa);bout=pairs(bb)
 return dict(matched_pairs=common,input_pairs=ain,output_pairs=bout,violating_input_pairs=ain-common,violating_output_pairs=bout-common)
rng=random.Random(350610);controls=[]
for t in range(1,53):
 maps=[]
 for _ in range(t):
  k=list('abcdefghijklmnopqrstuvwxyz');rng.shuffle(k);maps.append(dict(zip('abcdefghijklmnopqrstuvwxyz',k)))
 z=''.join(maps[i%t][c] for i,c in enumerate(x));r=consistency(x,z,t)
 assert not r['violating_input_pairs'] and not r['violating_output_pairs']
 controls.append(dict(period=t,**r))
rows=[dict(period=t,**consistency(x,y,t)) for t in range(1,53)]
out=dict(status='conditional_mechanism_test_not_plaintext',assumptions=['same aligned plaintext','same ring alphabets','same repeating stop sequence of periodT','no insertions/deletions'],half_open_literal_range=[20,375],controls=controls,target=rows)
(P/'adjustable-phase-results.json').write_text(json.dumps(out,indent=2)+'\n')
print('controls',len(controls),'all pass')
print('target exact-compatible periods',[r['period'] for r in rows if not r['violating_input_pairs'] and not r['violating_output_pairs']])
print('period52',rows[-1])
print('fewest violations',sorted(rows,key=lambda r:r['violating_input_pairs']+r['violating_output_pairs'])[:5])
