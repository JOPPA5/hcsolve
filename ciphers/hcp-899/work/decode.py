#!/usr/bin/env python3
"""Decode the explicit manual shape inventory; does not extract image pixels."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
d=json.loads((root/'work/transcript.json').read_text())
for name,want in d['source_sha256'].items():
 got=hashlib.sha256((root/name).read_bytes()).hexdigest()
 assert got==want, f'Original source changed: {name}'
key=d['key']; reverse={v:k for k,v in key.items()}; assert len(reverse)==len(key)
def decode(tokens):
 out=[]
 for s in tokens.split():
  out.append('/' if s=='/' else key[s])
  if s!='/':assert reverse[key[s]]==s
 return ''.join(out).replace('/',' / ')
counts={'upper_confirmed':0,'lower_confirmed':0,'lower_provisional':0,'untranscribed_spans':0}
for row in d['rows']:
 if row['region']=='upper':
  ts=row['tokens']; assert len(row['glyphs'])==len(ts.replace('/','').split())
  counts['upper_confirmed']+=len(row['glyphs'])
  print(row['label'],decode(ts))
 else:
  parts=[]
  for s in row['segments']:
   if s['status']=='untranscribed':
    counts['untranscribed_spans']+=1;parts.append('[UNTRANSCRIBED: '+s['scope']+']')
   else:
    counts['lower_'+s['status']]+=len(s['tokens'].replace('/','').split())
    text=decode(s['tokens']);parts.append(text if s['status']=='confirmed' else '[PROVISIONAL: '+text+']')
  print(row['label'],' / '.join(parts))
assert counts['upper_confirmed']==75
print(json.dumps(counts,sort_keys=True))
print('Fixed source hashes and exact shape round trips pass. Manual transcription only.')
print('PARTIAL: no exact total inventory or complete lower plaintext is claimed.')
