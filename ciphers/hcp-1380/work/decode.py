#!/usr/bin/env python3
"""HCP 1380: Caesar -1 on the hand transcription (work/transcription.json); not OCR.
Checks source hashes, decodes every token, checks the inverse round trip."""
import hashlib,json,re,string
from pathlib import Path
r=Path(__file__).resolve().parents[1]
H={'source/picture-large.jpg':'f1e1dc534f4e6c1642295eb83465e74962c924fdafb51e464287a8b7427c7db5',
   'source/address-large.jpg':'cb7731ad7296796f6897119f91e8dcd87923d09140a446bf535d1569f557cd8b',
   'work/hires/pc_hcp_61_pic.JPG':'6780d98f3dcba165e2cb6a0c39d99590ca34d64476f37daf977d6e5cd145fa3b',
   'work/hires/pc_hcp_61_adr.JPG':'24a33c957842e5fe90034684b1ec8165f4437ef0fc3b585ed79be07b5aaa213b'}
for n,h in H.items():
    assert hashlib.sha256((r/n).read_bytes()).hexdigest()==h,n
print('source hashes OK (4 files)')
up=string.ascii_uppercase
key={c:up[(i-1)%26] for i,c in enumerate(up)}
inv={v:k for k,v in key.items()}
def dec(s):
    out=[];n=0
    for part in re.split(r'(\{[^}]*\})',s):
        if part.startswith('{'): out.append(part[1:-1]); continue
        p=''.join(key.get(c.upper(),c) for c in part)
        assert ''.join(inv.get(c,c) for c in p)==part.upper()
        n+=sum(c.isalpha() for c in part); out.append(p)
    return ''.join(out),n
t=json.loads((r/'work/transcription.json').read_text())
print('Plain heading (not enciphered):',t['plain_heading'])
tot=0;ps=[]
for s in t['lines']:
    p,n=dec(s);tot+=n;ps.append(p);print(' ',s.ljust(24),'->',p)
print(tot,'enciphered letters decoded; literal: &')
txt=' '.join(ps).replace('.','').replace('"','')
print('Reading:',' '.join(txt.split()))
