#!/usr/bin/env python3
"""Revised decoder (after review 1). Loads the frozen manual record.json (hash-checked),
applies the documented corrections in corrections.json, and prints the literal and the
restored plaintext. Usage: python3 -I ciphers/hcp-1540/work/decode2.py [--indexed]"""
from pathlib import Path
import hashlib,json,sys
W=Path(__file__).resolve().parent
RECORD_SHA='f4cd4bf125679411d5860d611dd6cf64f4e056230c3544253e2ce848a434fbd4'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(W/'record.json')==RECORD_SHA,'frozen record changed'
r=json.loads((W/'record.json').read_text());key=json.loads((W/'key.json').read_text());assert key==r['key']
corr=json.loads((W/'corrections.json').read_text())['replace'];used=set()
lit=[];res=[];table=['position\ttype\tglyph\tplain'];ng=nr=0
for row in r['rows']:
 if row['id'].startswith('A'):continue
 L=[];S=[];pos=0
 for t in row['tokens']:
  toks=[t]
  if t.get('id') in corr:used.add(t['id']);toks=corr[t['id']]['tokens']
  for u in toks:
   k=u['type']
   if k in('space','literal'):L.append(u['text']);S.append(u['text']);continue
   pos+=1;pid=f"{row['id']}.{pos:03d}"
   if k=='glyph':v=key[u['glyph']];ng+=1;L.append(v);S.append(v);table.append(f"{pid}\tglyph\t{u['glyph']}\t{v}")
   elif k=='restoration':nr+=1;L.append(u['literal']);S.append(u['restored']);table.append(f"{pid}\trestoration\t-\t{u['restored']} (editorial)")
   elif k=='unknown_span':raise SystemExit(f'unresolved span {pid}')
   else:L.append(u['text']);S.append(u['text']);table.append(f"{pid}\t{k}\t\t{u['text']}")
 lit.append(row['id']+' '+''.join(L));res.append(row['id']+' '+''.join(S))
assert used==set(corr),set(corr)-used
print(f'Frozen record hash OK; {len(used)} documented corrections applied; {ng} glyph units; {nr} editorial restoration(s); 0 unknown-length spans.')
print('\n== Literal (⟦blot⟧ = illegible struck-over group) ==');print('\n'.join(lit))
print('\n== With editorial restoration ==');print('\n'.join(res))
if '--indexed' in sys.argv:print('\n'+'\n'.join(table))
