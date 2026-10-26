#!/usr/bin/env python3
"""Decode manually read values, retain separately recorded source punctuation."""
from pathlib import Path
import hashlib,json,re
p=Path(__file__).resolve().parents[1]
key={n:chr(64+n) for n in range(1,27)}
for name,h in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()==h,name
lines=(p/'work/transcription.txt').read_text().splitlines()
diplomatic=(p/'work/transcription-diplomatic.txt').read_text().splitlines()
punctuation=json.loads((p/'work/punctuation.json').read_text())['rows']
assert len(lines)==len(diplomatic)==len(punctuation)==5
count=0
for i,line in enumerate(lines):
 words=[];rownums=[]
 for j,word in enumerate(line.split(' / ')):
  nums=list(map(int,word.split()));rownums.extend(nums)
  assert all(1<=n<=26 for n in nums)
  plain=''.join(key[n] for n in nums)+punctuation[i].get(str(j),'')
  count+=len(nums);words.append(plain)
 assert rownums==list(map(int,re.findall(r'\d+',diplomatic[i]))),(i,rownums)
 print(' '.join(words))
assert count==40
print('Encrypted numeric positions:',count)
print('Source hashes and diplomatic/normalised value agreement passed.')
print('Manual transcription rechecked after review 1; no OCR or pixel proof from this command.')
