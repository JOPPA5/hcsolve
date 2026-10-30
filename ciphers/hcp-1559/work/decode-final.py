#!/usr/bin/env python3
"""HCP1559 final decode: fixed Anna Ticha family key + family G, applied to the
manual transcription in transcription-final.txt. Brackets are carried through:
[..] restored from context, (..) low-confidence trace. Read-only."""
from pathlib import Path
import json
W=Path(__file__).resolve().parent;R=W.parents[2]
key=json.loads((W/'key-final.json').read_text())
base=json.loads((R/'ciphers/hcp-1520/work/key.json').read_text())
assert {k:v for k,v in key.items() if k!='G'}==base and key['G']=='g','key differs from family key + G'
read=restored=low=0;out=[]
for line in (W/'transcription-final.txt').read_text().splitlines():
    if not line or line.startswith('#'):continue
    rid,cip=line.split(' ',1);mode=None;lit=''
    for c in cip:
        if c in '[(' :mode=c;lit+=c;continue
        if c in '])':mode=None;lit+=c;continue
        if c in key:
            lit+=key[c]
            if mode=='[':restored+=1
            elif mode=='(':low+=1
            else:read+=1
        else:
            assert c in ' ,.-',('unmapped sign',rid,c);lit+=c
    out.append(rid+' '+lit)
sol=(W.parent/'SOLUTION.md').read_text().split('<!--final-begin-->')[1].split('<!--final-end-->')[0].strip()
assert sol=='```plaintext\n'+'\n'.join(out)+'\n```','SOLUTION final block differs'
print('\n'.join(out))
print(f'\nCHECK: {len(out)} rows; {read+restored+low} cipher units = {read} read + {low} low-confidence (..) + {restored} restored [..]; unknown spans: 0')
