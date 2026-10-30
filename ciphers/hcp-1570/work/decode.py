#!/usr/bin/env python3
"""HCP1570 v2: read-only reproduction. Decodes the manual transcription with the
Anna Tichá family key (+ k-shaped G, as on hcp-1541/1553/1554). Standard library only.
v1 (with opaque {U1}) is kept in work/v1/ for audit."""
from pathlib import Path
from collections import Counter
import csv,hashlib,io,json
W=Path(__file__).resolve().parent;B=W.parent;ROOT=W.parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
h=json.loads((W/'sha256.json').read_text())
for p,d in h['inputs'].items():assert sha(ROOT/p)==d,'Input changed: '+p
for p,d in h['records'].items():assert sha(W/p)==d,'Record changed: '+p
key=json.loads((W/'key.json').read_text())
base=json.loads((ROOT/'ciphers/hcp-1520/work/key.json').read_text())
assert {k:v for k,v in key.items() if k!='G'}==base and key['G']=='g','key must be family key + G'
inv={v:k for k,v in key.items()};assert len(inv)==len(key)==23
rec=json.loads((W/'transcription.json').read_text());assert rec['manual'] is True
assert [r['row'] for r in rec['rows']]==[f'R{i:02}' for i in range(1,16)]
src=(W/'transcription.txt').read_text();assert src=='\n'.join(r['cipher'] for r in rec['rows'])+'\n'
out=[];pos=[];cnt=Counter();idx=letters=0
for row in rec['rows']:
    b=row['box_oriented_xyxy'];assert row['rotation_counterclockwise']==90 and row['box_original_xyxy']==[1024-b[3],b[0],1024-b[1],b[2]]
    n=0
    for wi,word in enumerate(row['cipher'].split(),1):
        for c in word:
            if c in key:
                idx+=1;n+=1;cnt[c]+=1;letters+=len(key[c])
                pos.append([str(idx),row['row'],str(n),str(wi),c,key[c],'mapped',','.join(map(str,b)),','.join(map(str,row['box_original_xyxy']))])
            else:assert c in ',.!?',('unmapped sign',row['row'],c)
    lit=''.join(key.get(c,c) for c in row['cipher']);assert lit==row['literal'] and n==row['source_units']
    enc=[];i=0  # full inverse of the printed plaintext, CH before C
    while i<len(lit):
        if not lit[i].isalpha():enc.append(lit[i]);i+=1;continue
        u=next(u for u in sorted(inv,key=len,reverse=True) if lit.startswith(u,i));enc.append(inv[u]);i+=len(u)
    assert ''.join(enc)==row['cipher'],'inverse mismatch '+row['row']
    out.append(lit);print(lit)
text='\n'.join(out)+'\n';assert text==(W/'literal-cz.txt').read_text()
assert '```text\n'+text+'```' in (B/'SOLUTION.md').read_text(),'SOLUTION literal differs'
assert pos==list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:]
j=json.loads((W/'inventory.json').read_text())
assert (idx,letters,cnt['H'],dict(cnt))==(j['source_units'],j['known_base_letters'],j['CH_units'],j['class_counts'])==(523,529,6,j['class_counts'])
print(f'\nCHECKED v2: 15 rows; {idx} cipher signs, all mapped (0 unknown); {cnt["H"]} CH, {cnt["G"]} G (k-shaped); {letters} plaintext letters; source/input and {len(h["records"])} record hashes, row boxes, positions, inventory, SOLUTION literal and whole-plaintext inverse pass.')
