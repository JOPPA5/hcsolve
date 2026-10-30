#!/usr/bin/env python3
"""Literal standard-Morse decoding of manual groups, preserving nonstandard signs."""
from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parents[1]
for name,digest in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()==digest,name
codes='.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
key=dict(zip(codes,'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
total=0;unknown=0
for row in json.loads((p/'work/transcription.json').read_text())['rows']:
 out=[]
 for group in row['groups']:
  total+=1
  if group in key:out.append(key[group])
  else:out.append('{'+group+'}');unknown+=1
 print(row['id']+': '+''.join(out))
print(f'{total} manual Morse groups: {total-unknown} standard A-Z letters, {unknown} preserved nonstandard group.')
print('Source hashes verified; manual transcription, not OCR or independent pixel proof.')
