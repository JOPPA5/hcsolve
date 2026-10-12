"""Independent row-fill / column-read and partition-fill verification."""
from pathlib import Path
import json
b=Path(__file__).resolve().parent
def forward(p,key):
    rows=[p[i:i+len(key)] for i in range(0,len(p),len(key))]
    return ''.join(row[col] for col in key for row in rows if col<len(row))
def inverse(c,key):
    width=len(key);q,r=divmod(len(c),width);cols={};at=0
    for col in key:
        length=q+(col<r);cols[col]=c[at:at+length];at+=length
    assert at==len(c)
    return ''.join(cols[col][row] for row in range(q+int(r>0)) for col in range(width) if row<len(cols[col]))
results=[]
for file in sorted(b.glob('*control.json'))+sorted(b.glob('*target*.json')):
    data=json.loads(file.read_text())
    if not isinstance(data,dict) or 'rows' not in data:continue
    for row in data['rows']:
        if row['status']!='sat':continue
        p=data['plaintext'];c=data['ciphertext'];pred=p
        for key in row['keys']:
            assert sorted(key)==list(range(len(key)))
            pred=forward(pred,key)
        mismatch=[i for i,(a,x) in enumerate(zip(pred,c)) if a!=x]
        assert len(mismatch)==1 and pred[mismatch[0]]=='n' and c[mismatch[0]]=='u'
        recovered=pred;literal=c
        for key in row['keys'][::-1]:
            recovered=inverse(recovered,key);literal=inverse(literal,key)
        assert recovered==p and all(key.index(0)==row['n']-1 for key in row['keys'])
        reencoded=literal
        for key in row['keys']:reencoded=forward(reencoded,key)
        assert reencoded==c and sum(x!=y for x,y in zip(literal,p))==1
        results.append(dict(file=file.name,n=row['n'],full110_encoder_inverse_exact=True,literal_roundtrip_exact=True,mismatch_position1=mismatch[0]+1,keys=row['keys']))
(b/'independent-verification.json').write_text(json.dumps(results,indent=2)+'\n')
print('Verified complete witnesses:',len(results))
