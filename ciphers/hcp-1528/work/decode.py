#!/usr/bin/env python3
"""HCP 1528: verify source/record hashes and decode the round-2 manual transcription
with the Anna Tichá family key. Read-only. Run: python3 -I ciphers/hcp-1528/work/decode.py"""
from pathlib import Path
import hashlib,json,csv,io,re
R=Path(__file__).resolve().parents[1];W=R/'work'
for m in ('source-sha256.json','record-sha256.json'):
 for fn,h in json.loads((W/m).read_text()).items():
  assert hashlib.sha256((R/fn).read_bytes()).hexdigest()==h,f'hash mismatch {fn}'
key=json.loads((W/'key.json').read_text());inv={v:k for k,v in key.items()};assert len(inv)==len(key)
rec=json.loads((W/'transcription.json').read_text());pos=[];total=letters=0;seen=[];rows=[]
for row in rec['rows']:
 out=[];idx=0
 for t in re.findall(r'\{[HQ]\d+\}|.',row['cipher']):
  if t in key:
   total+=1;idx+=1;letters+=len(key[t]);assert inv[key[t]]==t
   pos.append([str(total),row['id'],str(idx),t,key[t]]);out.append(key[t])
  elif t.startswith('{'): seen.append(t[1:-1]);out.append('['+t[1:-1]+']')
  else: assert t in ' .,-',t;out.append(t)
 s=''.join(out);assert s==row['plaintext'] and idx==row['units'];rows.append(s);print(s)
assert len(rows)==18 and sorted(seen)==sorted(rec['gaps'])
assert pos==list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:]
assert '\n'.join(rows)+'\n'==(W/'plaintext.txt').read_text()
print(f'\n{total} cipher signs decoded -> {letters} base letters; {len(seen)} marked gaps: '+'; '.join(f'{g}: {rec["gaps"][g]}' for g in seen))
