#!/usr/bin/env python3
"""Caesar -1 on a frozen MANUAL transcript; not pixel OCR."""
import hashlib,json,string,re
from pathlib import Path
r=Path(__file__).resolve().parents[1]
for name,h in json.loads((r/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((r/'source'/name).read_bytes()).hexdigest()==h,name
abc=string.ascii_uppercase
key=dict(zip(abc,abc[-1]+abc[:-1]));inv={v:k for k,v in key.items()}
def dec(s):return ''.join(key.get(c.upper(),c) for c in s)
t=json.loads((r/'work/transcript.json').read_text())
count=0
outputs=[]
for line in t['cipher_lines']:
 p=dec(line);print(p);outputs.append(p)
 assert ''.join(inv.get(c,c) for c in p)==line.upper()
 count+=sum(c in abc for c in line.upper())
assert count==48,count
joined=' '.join(outputs).replace('SCOT CH','SCOTCH').replace('.','')
print('Joined reading: '+re.sub(r'\s+',' ',joined).strip()+'.')
print('Ordinary date:',t['ordinary_date'])
print('Ordinary circled signature:',t['ordinary_signature'])
print(f'{count} encrypted letters; source hashes and exact alphabetic round trips pass.')
print('Manual transcription; script does not independently validate image pixels.')
