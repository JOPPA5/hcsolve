"""HCP 1565 reproduction (revised after review 1). Standard library only, read-only.
Decodes work/transcription.txt with work/key.json and checks the saved records."""
from pathlib import Path
from collections import Counter
import csv, hashlib, io, json
W=Path(__file__).resolve().parent; C=W.parent; R=C.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rec=json.loads((W/'transcription.json').read_text())
for rel,digest in rec['source_sha256'].items():
    assert sha(R/rel)==digest, ('source hash mismatch',rel)
key=json.loads((W/'key.json').read_text())
fam=R/'ciphers/hcp-1520/work/key.json'
if fam.exists(): assert fam.read_bytes()==(W/'key.json').read_bytes(), 'key differs from family key'
assert len(key)==len(set(key.values()))==22
NONCIPHER=' ,.-?:♡'
inverse={v:k for k,v in key.items()}; longest=sorted(inverse,key=len,reverse=True)
def encode(text):
    out='';i=0
    while i<len(text):
        m=next((v for v in longest if text.startswith(v,i)),None)
        if m: out+=inverse[m]; i+=len(m)
        else: assert text[i] in NONCIPHER; out+=text[i]; i+=1
    return out
counts=Counter(); lines=[]; positions=[]
for line in (W/'transcription.txt').read_text().splitlines():
    rid,ct=line.split(' ',1); lit=''; rk=0
    for off,ch in enumerate(ct,1):
        if ch in key:
            counts[ch]+=1; rk+=1; lit+=key[ch]
            positions.append([str(len(positions)+1),rid,str(rk),'1',str(off),ch,key[ch]])
        else:
            assert ch in NONCIPHER, ('unmapped sign',rid,ch); lit+=ch
    assert encode(lit)==ct, ('inverse',rid)
    row=next(r for r in rec['rows'] if r['id']==rid)
    assert row['cipher_with_unknown_markers']==ct and row['literal']==lit and row['mapped_units']==rk
    lines.append(rid+' '+lit)
text='\n'.join(lines)+'\n'
assert (W/'literal-czech.txt').read_text()==text
sol=(C/'SOLUTION.md').read_text()
block=sol.split('<!-- literal-start -->\n```text\n',1)[1].split('```\n<!-- literal-end -->',1)[0]
assert block==text, 'SOLUTION.md literal block differs'
assert list(csv.reader(io.StringIO((W/'glyph-index.csv').read_text())))[1:]==positions
assert rec['counts']['mapped_units']==sum(counts.values()) and len(counts)==22
print(text,end='')
print(f'PASS: 9 rows; {sum(counts.values())} cipher signs ({counts["H"]} CH, {sum(counts[k]*len(key[k]) for k in counts)} letters); 22/22 classes; 0 unknown; 1 non-cipher heart; whole-text inverse OK.')
