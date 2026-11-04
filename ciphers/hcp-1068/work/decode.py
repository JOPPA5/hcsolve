"""Decode hcp-1068: python3 -I ciphers/hcp-1068/work/decode.py  (run from repo root)"""
import hashlib, json, os, re, sys
D=os.path.dirname(os.path.abspath(__file__)); C=os.path.dirname(D)
HASH={'source/address-large.jpg':'047d2ed28c42f43048cc0cfb81684ce4bf22ab377e74160effd458857b949646',
      'source/picture-large.jpg':'17d77c6fce4dce1b535232420697d0caa4e1a7a590ded704911ab9a77d88736b',
      'work/hires/cpc_1965-04-06_DE_Munchen_DE_Bremen_barbelhoffmann-02_adr.jpg':'d1f6156fffb9aacb1377d5cb3260a7ed3651d3fe5e3a2eecba1257565f4c3d7b'}
for p,h in HASH.items():
    got=hashlib.sha256(open(os.path.join(C,p),'rb').read()).hexdigest()
    if got!=h: sys.exit('hash mismatch '+p)
key=json.load(open(os.path.join(D,'key.json'),encoding='utf-8'))
out=[]
for line in open(os.path.join(D,'transcription.txt'),encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    line=line.rstrip('\n')
    line=re.sub(r'.\[([^\]]*)\]',r'\1',line)   # insertion replaces the sign before the caret
    if 'Eva' in line: line,tail=line.split('Eva'); tail='Eva'+tail
    else: tail=''
    out.append(''.join(key.get(c,c) for c in line)+tail)
print('hashes ok'); print('\n'.join(out))
