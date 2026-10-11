"""Extend the conditional 355-letter key through the full literal 385 stream."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
adj=json.loads((root/'batches/kryha-wheel-sol61/wheel52.json').read_text())['adjacent_distances']
key=json.loads((root/'batches/kryha-two-mask-refine-sol61/actual-row5-pure6-r7-full.json').read_text())[0]
def arc(a,b):
    total=0
    while True:
        total+=adj[a];a=(a+1)%52
        if a==b:return total
def shifts(mask):
    jumps=[arc(a,b) for a,b in zip(mask,mask[1:]+mask[:1])]
    cumulative=[0]
    for a in jumps:cumulative.append(cumulative[-1]+a)
    assert cumulative[-1]==179
    return [cumulative[(i-20)%23]+179*((i-20)//23) for i in range(385)]
results=[]
for variant in ('pixel-strong','pixel-strong-plus-moderate'):
    cts=[(root/f'batches/kryha-shift23-sol61/{n}-{variant}.txt').read_text().strip() for n in (350,351)]
    pts=[]
    for side,ct in enumerate(cts):
        ds=[x+(key['beta'] if side else 0) for x in shifts(key['masks'][side])]
        pt=''.join(chr(97+key['P'][(key['O'][ord(c)-97]-d)%26]) for c,d in zip(ct,ds))
        invp={x:i for i,x in enumerate(key['P'])};invo={x:i for i,x in enumerate(key['O'])}
        reen=''.join(chr(97+invo[(invp[ord(p)-97]+d)%26]) for p,d in zip(pt,ds))
        assert reen==ct
        if variant=='pixel-strong':assert pt[20:375]==key['plaintexts'][side]
        pts.append(pt)
        print(variant,side,'PREFIX',pt[:20],'BODY',pt[20:375],'SUFFIX',pt[375:])
    results.append(dict(variant=variant,key_source='batches/kryha-two-mask-refine-sol61/actual-row5-pure6-r7-full.json',
      key=key,plaintexts_full385=pts,full_reencryption_exact=True,framing_is_encrypted_not_established=True))
(Path(__file__).parent/'full-extension.json').write_text(json.dumps(results,indent=2)+'\n')
