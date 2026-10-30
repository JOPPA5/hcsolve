#!/usr/bin/env python3
"""Caesar -1 on frozen MANUAL transcript; no image OCR."""
import hashlib,json,string
from pathlib import Path
r=Path(__file__).resolve().parents[1]
for name,h in json.loads((r/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((r/'source'/name).read_bytes()).hexdigest()==h,name
k={c:chr((ord(c)-ord('A')-1)%26+ord('A')) for c in string.ascii_uppercase}
def dec(s):return ''.join(k.get(c.upper(),c) for c in s)
t=json.loads((r/'work/transcription.json').read_text())
count=0
for line in t['frozen_cipher_lines']:
 parts=line.split('[',1)
 print(dec(parts[0])+('['+parts[1] if len(parts)>1 else ''))
 count+=sum(c.isalpha() for c in parts[0])
print(f'{count} frozen alphabetic positions. Full message NOT established.')
for c in t['closing']:
 if 'decoded' in c:
  assert dec(c['raw'])==c['decoded']
  print('PROVISIONAL ONLY:',c['raw'],'->',dec(c['raw']))
print('Abbreviation not expanded:',t['closing'][0]['raw'])
print('Source hashes pass; manual transcription is not independently validated by this script.')
