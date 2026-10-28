#!/usr/bin/env python3
"""Read-only check of manual source-image transcription. Does not perform OCR."""
from pathlib import Path
import csv,hashlib,json
from collections import Counter
p=Path(__file__).resolve().parent; root=p.parent
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
meta=json.loads((p/'transcription.json').read_text());key=json.loads((p/'key.json').read_text())
assert sha(p/'key.json')=='83f6adf2789edbd6311e9d16394db0ba4a0a34c0745bb1dfc7e7f20e29dfc973','fixed transferred key changed'
for name,want in meta['source_sha256'].items():
 assert sha(root/'source'/name)==want,'source hash changed: '+name
for name,want in json.loads((p/'record-hashes.json').read_text()).items():
 assert sha(p/name)==want,'manual record/crop changed: '+name
for name,want in json.loads((p/'reference-sha256.json').read_text()).items():
 assert sha(root.parent.parent/name)==want,'reference hash changed: '+name
assert len(set(key.values()))==len(key)
inverse={v:k for k,v in key.items()};units=list(csv.DictReader((p/'indexed-units.csv').open()));i=0;ch=0;letters=0;used=set();counts=Counter();output=[]
for row in meta['rows']:
 j=0;parts=[]
 for token in row['cipher']:
  if token in key:
   plain=key[token];j+=1;i+=1;used.add(token);counts[token]+=1;ch+=token=='H';letters+=len(plain)
   assert inverse[plain]==token
   expected={'ordinal':str(i),'row':row['id'],'row_unit':str(j),'glyph_label':token,'plain':plain,'frame':row['frame'],'row_box':','.join(map(str,row['box']))}
   assert units[i-1]==expected,(row['id'],j)
   parts.append(plain)
  else:
   assert token in ' .,!-;:',(row['id'],token)
   parts.append(token)
 plain=''.join(parts);assert plain==row['literal'];assert j==row['assigned_units']
 # Check the actual inverse of each full literal row, using longest match for CH.
 back='';offset=0
 while offset<len(plain):
  value='CH' if plain.startswith('CH',offset) else plain[offset]
  back+=inverse.get(value,value);offset+=len(value)
 assert back==row['cipher'],('full-row inverse differs',row['id'])
 output.append(row['id']+' '+plain)
 print(row['id']+' '+plain)
assert len(units)==i
assert meta['counts']=={'active_rows':len(meta['rows']),'active_units':i,'base_letters':letters,'CH_units':ch,'unknown_active_units':0,'observed_assigned_classes':len(used),'class_counts':dict(sorted(counts.items()))}
assert (p/'transcription.txt').read_text()==''.join(row['id']+' '+row['cipher']+'\n' for row in meta['rows'])
assert (p/'literal.txt').read_text()=='\n'.join(output)+'\n'
solution=(root/'SOLUTION.md').read_text();literal_block=solution.split('```text\n',1)[1].split('\n```',1)[0]
assert literal_block=='\n'.join(output),'SOLUTION literal differs'
print(f'\nCHECK: source, manual-record/crop and reference hashes OK. {len(meta["rows"])} active rows; {i} active indexed units, all assigned; {letters} base letters; {ch} CH units; {len(used)} observed assigned classes; unknown active units=0. Tokenwise and full-row inverse, indexed/text/SOLUTION literal equality OK.')
print(f'Class counts: 4/I={counts["4"]}; 1/Y={counts["1"]}.')
print('One canceled B09 span is excluded: at least three apparent positions, middle f/V visible, exact original count and whole word unknown. The distinct M03 u-like mark is excluded with unknown meaning. No total-original-unit denominator is claimed.')
print('This checks a manual transcription and key transfer. It is not OCR, automatic pixel proof, independent review, or proof of exact intended accents.')
