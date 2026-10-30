#!/usr/bin/env python3
"""Read-only verification and fixed-key decoding of a MANUAL transcript, not OCR."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
W=Path(__file__).resolve().parent
manifest=json.loads((W/'sha256.json').read_text())
for group,files in manifest.items():
 for p,expected in files.items():
  assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==expected, f'{group} hash differs: {p}'
assert manifest['originals']==json.loads((ROOT/'batches/easy-2026-10-28/cz230-next-source-sha256.json').read_text()),'Source guard entries differ'
key=json.loads((W/'key.json').read_text())
canonical=json.loads((ROOT/'ciphers/hcp-1520/work/key.json').read_text()); canonical['F']='f'
assert key==canonical,'Fixed family key was changed'
assert len(set(key.values()))==len(key),'Key inverse not one-to-one'
fixed_inverse={v:k for k,v in key.items()}
records=json.loads((W/'transcription.json').read_text()); inventory=json.loads((W/'inventory.json').read_text())
lines=(W/'transcription.txt').read_text().splitlines()
assert lines==[r['cipher'] for r in records['rows']]
assert [r['row'] for r in records['rows']]==list(range(1,9))
expected_inventory=[]; output=[]; mapped=ch=single=span=0
for ri,(line,row) in enumerate(zip(lines,records['rows']),1):
 position=0; lit=''
 for wi,word in enumerate(line.split(' '),1):
  for ti,t in enumerate(re.findall(r'<[^>]+>|.',word),1):
   if t in key:
    value=key[t];kind='mapped';position+=1;mapped+=1;ch+=t=='H'
   elif re.fullmatch(r'<[^>]+>',t):
    spec=records['unknowns'][t[1:-1]];kind=spec['type'];position+=1
    if kind=='unmapped_glyph':
     assert spec['length']==1;value='[unmapped:K]';single+=1
    else:
     assert kind=='obscured_span' and spec['length'] is None;value='[obscured:unknown-length]';span+=1
   else:
    assert t in ',.?-';value=t;kind='punctuation'
   expected_inventory.append({'row':ri,'word':wi,'token_index':ti,'position':position if kind!='punctuation' else None,'label':t,'kind':kind,'literal':value,'row_bbox':row['bbox']})
   lit+=value
  if wi<len(line.split(' ')):lit+=' '
 output.append(lit)
assert inventory==expected_inventory,'Indexed positions or literal records differ'
counts={'mapped_units':mapped,'CH_units':ch,'mapped_base_letters':mapped+ch,'unmapped_single_glyphs':single,'obscured_spans_unknown_length':span}
assert counts==records['counts']
assert '\n'.join(output)+'\n'==(W/'literal.txt').read_text(),'Expected literal differs'
# Invert each full literal line through the SAME fixed complete inverse, parsing CH
# as its one preknown Czech unit, rather than inventing a separate inverse per token.
for line,lit in zip(lines,output):
 spans=iter(re.findall(r'<S[^>]+>',line)); encoded='';i=0
 while i<len(lit):
  if lit.startswith('[obscured:unknown-length]',i):
   encoded+=next(spans);i+=len('[obscured:unknown-length]')
  elif lit.startswith('[unmapped:K]',i):encoded+='<K>';i+=len('[unmapped:K]')
  elif lit.startswith('ch',i):encoded+=fixed_inverse['ch'];i+=2
  elif lit[i] in fixed_inverse:encoded+=fixed_inverse[lit[i]];i+=1
  else:
   assert lit[i] in ' ,.?-';encoded+=lit[i];i+=1
 assert encoded==line, f'Whole-line fixed-key inverse differs: {encoded!r}'
print('\n'.join(output))
print('\nVERIFIED:',json.dumps(counts,sort_keys=True))
print('SHA-256 files:',{group:len(files) for group,files in manifest.items()})
print('Exact indexed-record checks and whole-line fixed-key inverse: PASS')
print('Manual transcription, not OCR; hashes and inverse do not establish handwriting truth.')
