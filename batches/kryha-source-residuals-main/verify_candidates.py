"""Independent adjacent-hole walk audit of full-body candidate keys.

This checks mechanics, source coverage and paired differences, not linguistic
correctness. It does not import the solver's projection or codec.
"""
from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[2]
adj=json.loads((root/'batches/kryha-wheel-sol61/wheel52.json').read_text())['adjacent_distances']
assert len(adj)==52 and sum(adj)==179
def decode(ct,P,O,h,start):
    out=[];d=start
    for i,c in enumerate(ct):
        out.append(chr(97+P[(O[ord(c)-97]-d)%26]))
        hole=h[i%23];next_hole=h[(i+1)%23]
        while True:
            d=(d+adj[hole])%26;hole=(hole+1)%52
            if hole==next_hole:break
    return ''.join(out)
def encode(pt,P,O,h,start):
    pinv=[P.index(i) for i in range(26)];oinv=[O.index(i) for i in range(26)]
    return encode_walk(pt,pinv,oinv,h,start)
def encode_walk(pt,pinv,oinv,h,d):
    out=[]
    for i,c in enumerate(pt):
        out.append(chr(97+oinv[(pinv[ord(c)-97]+d)%26]))
        x=h[i%23];end=h[(i+1)%23]
        while True:
            d=(d+adj[x])%26;x=(x+1)%52
            if x==end:break
    return ''.join(out)
checks=[]
for variant in ('pixel-strong','pixel-strong-plus-moderate'):
    literal=[(root/f'batches/kryha-shift23-sol61/{n}-{variant}.txt').read_text().strip() for n in (350,351)]
    assert all(len(s)==385 for s in literal)
    cts=[s[20:375] for s in literal]
    for row in (5,6):
        file=root/f'batches/kryha-two-mask-language-sol61/{variant}-row{row}-full-candidates.json'
        keys=json.loads(file.read_text());pairdiff=[]
        for key in keys:
            P,O,h=key['P'],key['O'],key['masks']
            assert sorted(P)==sorted(O)==list(range(26))
            assert all(len(x)==23 and len(set(x))==23 and all(0<=z<52 for z in x) for x in h)
            assert all(sum((b-a)%52 for a,b in zip(x,x[1:]+x[:1]))==52 for x in h)
            starts=[0,key['beta']]
            pts=[decode(c,P,O,m,s) for c,m,s in zip(cts,h,starts)]
            assert pts==key['plaintexts']
            assert [encode(p,P,O,m,s) for p,m,s in zip(pts,h,starts)]==cts
            differences=[i+20 for i,(a,b) in enumerate(zip(pts[0][:-1],pts[1][1:])) if a!=b]
            pairdiff.append(differences)
        assert all(d==pairdiff[0] for d in pairdiff)
        checks.append(dict(file=str(file.relative_to(root)),sha256=hashlib.sha256(file.read_bytes()).hexdigest(),
          candidates=len(keys),body_letters_each=355,frame_letters_each_not_deciphered=30,
          direct_hole_walk_decode_encode_exact=True,paired_difference_350_zero=pairdiff[0],
          complete_historical_plaintext_verified=False))
(Path(__file__).parent/'candidate-verification.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
