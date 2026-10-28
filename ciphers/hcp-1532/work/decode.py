"""Read-only, standard-library audit of manual transcription; not OCR."""
import collections,csv,hashlib,io,json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];W=BASE/'work'
manifest=json.loads((W/'manifest.json').read_text())
for group in ['source_files','record_files']:
 for relative,expected in manifest[group].items():
  assert hashlib.sha256((BASE/relative).read_bytes()).hexdigest()==expected,'Hash mismatch: '+relative
key=json.loads((W/'key.json').read_text());data=json.loads((W/'transcription.json').read_text())
inverse={v:k for k,v in key.items()};assert len(inverse)==len(key)
index=list(csv.DictReader(io.StringIO((W/'index.csv').read_text())))
count=letters=ch=0;outputs=[];ambiguities=[];counts=collections.Counter()
for row in data['rows']:
 units=[c for c in row['cipher'] if c in key];selected={u['row_ordinal']:u for u in row.get('uncertainties',[])}
 assert len(units)==row['active_units']
 plain=''.join(key.get(c,c) for c in row['cipher'])
 assert all(c in key or c in ' .,-?;' for c in row['cipher'])
 assert plain==row['plaintext'],'Plaintext mismatch '+row['id'];outputs.append(plain)
 # Independent whole-row inverse of printed plaintext; CH is longest first.
 recovered=[];i=0
 while i<len(plain):
  if not plain[i].isalpha():recovered.append(plain[i]);i+=1;continue
  for token in sorted(inverse,key=len,reverse=True):
   if plain.startswith(token,i):recovered.append(inverse[token]);i+=len(token);break
  else:raise AssertionError(('unencodable plaintext',row['id'],i))
 assert ''.join(recovered)==row['cipher'],'Whole-row inverse mismatch '+row['id']
 for ordinal,c in enumerate(units,1):
  rec=index[count];count+=1;letters+=len(key[c]);ch+=c=='ř';counts[c]+=1
  assert (rec['row'],int(rec['row_ordinal']),int(rec['global_ordinal']),rec['cipher_label'],rec['plaintext_unit'],rec['row_source_xyxy'])==(row['id'],ordinal,count,c,key[c],','.join(map(str,row['box_source_xyxy'])))
  u=selected.get(ordinal)
  if u:
   assert u['selected_label']==c and len(u['candidate_labels'])>1 and c in u['candidate_labels']
   assert all(v in key for v in u['candidate_labels'])
   assert rec['status']=='ambiguous' and rec['candidate_cipher_labels']=='|'.join(u['candidate_labels']) and rec['candidate_plaintext_units']=='|'.join(key[v] for v in u['candidate_labels']) and rec['observation']==u['observation']
   assert rec['selected_reading_basis']==u['selected_reading_basis'];ambiguities.append((row['id'],ordinal,count,u))
  else:assert rec['status']=='read' and rec['candidate_cipher_labels']==c and rec['candidate_plaintext_units']==key[c] and not rec['observation'] and not rec['selected_reading_basis']
 print(plain)
assert count==len(index)==manifest['active_units'] and letters==manifest['base_letters'] and ch==manifest['CH_units']
assert '\n'.join(outputs)+'\n'==(W/'literal-cz.txt').read_text()
inventory=json.loads((W/'inventory.json').read_text());assert inventory['selected_label_counts']==dict(sorted(counts.items()))
assert len(ambiguities)==inventory['ambiguous_units']==manifest['ambiguous_units']==1
assert inventory['unambiguous_units']==count-len(ambiguities)
for row,ordinal,global_ordinal,u in ambiguities:
 print(f'\nAMBIGUOUS {row} unit {ordinal} / global {global_ordinal}: {u["observation"]}; candidates '+', '.join(v+'→'+key[v] for v in u['candidate_labels'])+f'; selected {u["selected_label"]}→{key[u["selected_label"]]}. '+u['selected_reading_basis'])
print(f'\nVerified: {count} cipher units ({count-len(ambiguities)} unambiguous, {len(ambiguities)} ambiguous with selected reading); {ch} CH units; {letters} selected base letters; {len(manifest["source_files"])} source hashes and {len(manifest["record_files"])} record hashes; exact whole-row fixed-key inverse. Manual image reading is not proved by these checks.')
