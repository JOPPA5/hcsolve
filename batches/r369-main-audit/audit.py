"""Read-only independent full column-grid audit of regular22 control/target.

Does not import the optimizer or its encoder. Target audit only runs on SAT.
"""
from pathlib import Path
import json,sys,hashlib
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
def encrypt_grid(text,order):
    w=len(order);rows=[list(text[i:i+w])for i in range(0,len(text),w)]
    return ''.join(row[col]for col in order for row in rows if col<len(row))
def inverse_grid(text,order):
    w=len(order);n=len(text);grid=[['']*min(w,n-i)for i in range(0,n,w)];at=0
    for col in order:
        for row in grid:
            if col<len(row):row[col]=text[at];at+=1
    assert at==n
    return ''.join(''.join(row)for row in grid)
def verify(p,c,result):
    keys=result['keys'];assert len(keys)==3 and all(sorted(k)==list(range(22))for k in keys)
    ranks=[k.index(0)+1 for k in keys];assert len(set(ranks))==1
    enc=p
    stages=[]
    for key in keys:enc=encrypt_grid(enc,key);stages.append(enc)
    mismatches=[dict(position1=i+1,predicted=a,literal=b)for i,(a,b)in enumerate(zip(enc,c))if a!=b]
    assert len(mismatches)==1 and mismatches[0]['predicted']=='n'and mismatches[0]['literal']=='u'
    assert enc==result['predicted_ciphertext']
    plain=enc;raw=c
    for key in keys[::-1]:plain=inverse_grid(plain,key);raw=inverse_grid(raw,key)
    assert plain==p
    pd=[dict(position1=i+1,prepared=a,raw=b)for i,(a,b)in enumerate(zip(p,raw))if a!=b]
    assert len(pd)==1 and pd[0]['prepared']=='n'and pd[0]['raw']=='u'
    return dict(independent_ciphertext=enc,raw_literal_plaintext=raw,prepared_plaintext=p,stage_outputs=stages,common_alignment=ranks[0],cipher_differences=mismatches,plaintext_differences=pd,full110_raw_inverse=True,full110_encoder_after_declared_error=True)
case=sys.argv[1]if len(sys.argv)>1 else'control0'
base=root/'batches/r369-regular22-next-sol61'
if case.startswith('control'):
    result=json.loads((base/(case+'-eager.json')).read_text())
    assert result['status']=='sat'
    data=json.loads((base/(case+'-truth.json')).read_text())
    # Only the independently supplied P/CT pair is needed; planted key ignored.
    p=data['plaintext'];c=data['observed_ciphertext']
elif case=='target':
    result=json.loads((base/'target.json').read_text());assert result['status']=='sat'
    data=result['conditional_preparation'];p=data['plaintext'];c=data['ciphertext']
else:raise ValueError(case)
audit=verify(p,c,result)
audit['result_sha256']=hashlib.sha256(json.dumps(result,sort_keys=True).encode()).hexdigest()
(out/(case+'.json')).write_text(json.dumps(audit,indent=2)+'\n')
print(case,'independent110encoder/inverse verified; one declared N→U',audit['cipher_differences'])
