#!/usr/bin/env python3
"""Decode a manually frozen image transcript, not image pixels."""
import hashlib,json
from pathlib import Path
r=Path(__file__).resolve().parents[1]
for name,h in json.loads((r/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((r/'source'/name).read_bytes()).hexdigest()==h, name
key=json.loads((r/'work/key.json').read_text())
assert len(set(key.values()))==len(key)
punctuation={'{question}':'?', '{punct}':'[punctuation]', '{comma}':',', '{stop}':'.'}
known=unknown=0
for line in (r/'work/transcript.txt').read_text().splitlines():
 words=[]
 for word in line.strip().split(' / '):
  out=''
  for token in word.split():
   if token=='?': out+='□';unknown+=1
   elif token in punctuation: out+=punctuation[token]
   else: out+=key[token];known+=1
  words.append(out)
 print(' '.join(words))
print(f'{known} mapped positions, {unknown} unresolved positions; {len(key)} glyph classes.')
print('Source hashes pass. Manual transcription, not pixel-to-text validation.')
print('Context suggests SATURDAY (8 slots) and HER (3 slots), not inserted into literal output.')
