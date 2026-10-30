#!/usr/bin/env python3
"""Read-only fixed-key decode of a manual source-linked partial transcription, not OCR."""
from pathlib import Path
from collections import Counter
import csv,hashlib,json,re
W=Path(__file__).resolve().parent;C=W.parent;R=C.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((W/'sha256.json').read_text())
for group in ('sources','references','records'):
 for rel,want in manifest[group].items():assert sha(R/rel)==want,'hash mismatch: '+rel
record=json.loads((W/'transcription.json').read_text());key=json.loads((W/'key.json').read_text())
assert sha(W/'key.json')=='42c5162020506fead8605c07b8c07a94da2766128aabd42a374fe55cf084f6f7'
assert key==json.loads((R/'ciphers/hcp-1520/work/key.json').read_text()),'fixed key differs'
assert len(set(key.values()))==len(key);inv={v:k for k,v in key.items()}
guard=json.loads((R/'batches/easy-2026-10-28/cz239-241-source-sha256.json').read_text())
assert record['source_sha256']==manifest['sources']
for rel,want in manifest['sources'].items():assert guard[rel]==want,('target guard entry differs',rel)
positions=[];counts=Counter();known=0;unknown_seen=[];printed=[]
for row in record['rows']:
 literal='';cipher='';rowknown=0
 for ei,element in enumerate(row['elements'],1):
  if isinstance(element,dict):
   uid=element['unknown'];marker='<UNK:'+uid+'>';cipher+=marker;literal+=marker;unknown_seen.append((uid,row['id']))
  else:
   cipher+=element;literal+=''.join(key.get(c,c) for c in element)
   for offset,c in enumerate(element,1):
    if c in key:
     known+=1;rowknown+=1;counts[c]+=1;positions.append([str(known),row['id'],str(rowknown),str(ei),str(offset),c,key[c]])
    else:assert c in ' ,.-',('unmapped non-span symbol',row['id'],c)
 assert cipher==row['cipher_with_unknown_markers'];assert literal==row['literal'];assert rowknown==row['known_units']
 # Actual whole-row inverse. Unknown placeholders are opaque spans, not guessed glyphs.
 back=''
 for part in re.split(r'(<UNK:U\d{2}>)',literal):
  if part.startswith('<UNK:'):back+=part;continue
  i=0
  while i<len(part):
   value='ch' if part.startswith('ch',i) else part[i]
   assert value in inv or value in ' ,.-',('unmapped literal',row['id'],value)
   back+=inv.get(value,value);i+=len(value)
 assert back==cipher,('actual whole-row fixed-key inverse differs',row['id'])
 printed.append(row['id']+' '+literal)
assert sorted(unknown_seen)==sorted((u['id'],u['row']) for u in record['unknown_spans'])
assert all(u['glyph_count']=='unknown' for u in record['unknown_spans'])
actual={'physical_rows':len(record['rows']),'mapped_units':known,'CH_units':counts['H'],'mapped_base_letters':sum(counts[c]*len(key[c]) for c in counts),'observed_assigned_classes':len(counts),'unknown_spans':len(unknown_seen),'unknown_units':'unknown','all_original_units':'unknown','class_counts':dict(sorted(counts.items()))}
assert actual==record['counts'];assert (len(printed),known,counts['H'],actual['mapped_base_letters'],len(unknown_seen))==(5,214,5,219,4)
with (W/'positions.csv').open() as f:
 indexed=list(csv.reader(f));assert indexed[0]==['global_known_index','row','row_known_index','element_index','offset_in_known_element','shape_label','literal'];assert indexed[1:]==positions
assert (W/'transcription.txt').read_text()==''.join(x['id']+' '+x['cipher_with_unknown_markers']+'\n' for x in record['rows'])
assert (W/'literal.txt').read_text()=='\n'.join(printed)+'\n'
prose=(C/'SOLUTION.md').read_text();assert prose.split('```text\n',1)[1].split('\n```',1)[0]=='\n'.join(printed),'SOLUTION literal differs'
print('\n'.join(printed))
print(f'\nCHECK: {len(printed)} physical rows; {known} mapped units; CH={counts["H"]}; {actual["mapped_base_letters"]} mapped letters; {len(unknown_seen)} active unknown spans, unknown original glyph counts. Original total unknown.')
print('Source/reference/record hashes, own3 guard entries, unchanged fixed key, actual whole-row inverse with opaque unknown spans, indexed-unit and saved/SOLUTION literal equality OK.')
print('This verifies manual records; hashes/inverse are not pixel truth or OCR. Unknown ink is retained and not automatically canceled. No new G/F assignment or inferred name accents.')
