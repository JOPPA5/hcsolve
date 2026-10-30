#!/usr/bin/env python3
"""Read-only fixed-family-key reproduction of manual source transcription; not OCR."""
from pathlib import Path
from collections import Counter
import csv,hashlib,io,json,re
W=Path(__file__).resolve().parent;B=W.parent;ROOT=W.parents[2]
h=json.loads((W/'sha256.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for p,d in h['inputs'].items():assert sha(ROOT/p)==d,'Input changed: '+p
for p,d in h['records'].items():assert sha(W/p)==d,'Record changed: '+p
guard=json.loads((ROOT/'batches/easy-2026-10-28/cz246-251-252-source-sha256.json').read_text());assert len(guard)==9
for p,d in guard.items():assert sha(ROOT/p)==d,'Frozen batch source changed: '+p
key=json.loads((W/'key.json').read_text());assert key==json.loads((ROOT/'ciphers/hcp-1520/work/key.json').read_text());inv={v:k for k,v in key.items()};assert len(inv)==len(key)==22
record=json.loads((W/'transcription.json').read_text());assert record['manual'] is True
positions=[];counts=Counter();idx=mapped=ch=letters=0;out=[];unknown_positions=[]
for row in record['rows']:
 b=row['box_oriented_xyxy'];assert row['rotation_counterclockwise']==90 and row['box_original_xyxy']==[1024-b[3],b[0],1024-b[1],b[2]]
 n=kn=0
 for wi,word in enumerate(row['cipher'].split(),1):
  for c in re.findall(r'\{U1\}|.',word):
   if c in key or c=='{U1}':
    idx+=1;n+=1;unknown=c=='{U1}';plain=c if unknown else key[c]
    if unknown:unknown_positions.append((idx,row['row'],n,wi))
    else:mapped+=1;kn+=1;ch+=c=='H';letters+=len(key[c]);counts[c]+=1
    positions.append([str(idx),row['row'],str(n),str(wi),c,plain,'unknown-class-single-glyph' if unknown else 'mapped',','.join(map(str,b)),','.join(map(str,row['box_original_xyxy']))])
   else:assert c in ',.!?'
 literal=''.join(c if c=='{U1}' else key.get(c,c) for c in re.findall(r'\{U1\}|.',row['cipher']))
 assert literal==row['literal'] and (n,kn)==(row['source_units'],row['mapped_units']);out.append(literal);print(literal)
 # Actual inverse of complete printed plaintext, with the opaque unknown passed
 # through without assigning it any guessed plaintext or fixed-key glyph.
 encoded=[];i=0
 while i<len(literal):
  if literal.startswith('{U1}',i):encoded.append('{U1}');i+=4;continue
  if not literal[i].isalpha():encoded.append(literal[i]);i+=1;continue
  for unit in sorted(inv,key=len,reverse=True):
   if literal.startswith(unit,i):encoded.append(inv[unit]);i+=len(unit);break
  else:raise AssertionError(('unencodable literal',row['row'],i))
 assert ''.join(encoded)==row['cipher'],'Whole-plaintext inverse mismatch '+row['row']
assert [r['row'] for r in record['rows']]==[f'R{i:02}' for i in range(1,16)]
assert positions==list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:]
text='\n'.join(out)+'\n';assert text==(W/'literal-cz.txt').read_text()
assert '\n'.join(r['cipher'] for r in record['rows'])+'\n'==(W/'transcription.txt').read_text()
assert '```text\n'+text+'```' in (B/'SOLUTION.md').read_text(),'SOLUTION literal differs'
j=json.loads((W/'inventory.json').read_text());assert (idx,mapped,ch,letters)==(j['source_units'],j['mapped_units'],j['CH_units'],j['known_base_letters'])==(523,522,6,528)
assert counts==Counter(j['class_counts']) and {r['row']:r['source_units'] for r in record['rows']}==j['row_counts'] and {r['row']:r['mapped_units'] for r in record['rows']}==j['row_mapped_counts']
assert unknown_positions==[(364,'R11',5,1)] and j['unknown_single_glyphs']==1 and j['unknown_length_runs']==0
u=record['unknowns']['U1'];assert u['observed_source_units']==1 and u['plaintext_length'] is None and u['row']=='R11' and u['word']==1
print(f'\nCHECKED: 15 rows; {idx} source-glyph slots = {mapped} mapped + one unmapped single glyph; {ch} CH units expand mapped text to {letters} known base letters. Original plaintext length remains unknown for U1. {len(h["inputs"])} input/reference/guard hashes, all9 frozen batch sources, {len(h["records"])} local record hashes; all indices/coordinates, literal/SOLUTION equality and actual whole-plaintext fixed inverse pass. U1 is opaque, not an assigned G or R; no OCR/glyph-truth/acceptance claim.')
