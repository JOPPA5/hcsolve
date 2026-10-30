#!/usr/bin/env python3
"""Read-only verification of the manual record; no OCR or pixel proof."""
import argparse, hashlib, json, re
from collections import defaultdict
from pathlib import Path
P=Path(__file__).resolve();W=P.parent;R=W.parent.parent.parent
ap=argparse.ArgumentParser()
ap.add_argument('--units',action='store_true')
ap.add_argument('--emit-only',action='store_true',help='Authoring output: skip saved output equality checks; still read-only')
args=ap.parse_args()
manifest=json.loads((W/'manifest.json').read_text())
for rel,want in manifest['sha256'].items():
 actual=hashlib.sha256((R/rel).read_bytes()).hexdigest()
 if actual!=want:raise SystemExit(f'HASH FAILURE: {rel}')
rec=json.loads((W/'transcript.json').read_text());key=json.loads((W/'key.json').read_text())
# Construct the inverse of the entire supplied key, not a saved-token identity.
inverse=defaultdict(list)
for glyph,plain in key.items():inverse[plain].append(glyph)
global_pos=0;mapped=0;base_letters=0;unique_units=0;alias_units=0
output=[];tsv=['line\tline_unit\tglobal_unit\tcipher\tplain']
for line in rec['lines']:
 local_pos=0;raw=[];plain=[]
 for unit in line['units']:
  kind=unit['kind']
  if kind=='cipher':
   local_pos+=1;global_pos+=1;mapped+=1
   assert unit['line_index']==local_pos and unit['global_index']==global_pos,(line['id'],unit)
   glyph=unit['glyph'];p=key[glyph];assert p==unit['plain'];base_letters+=len(p)
   candidates=inverse[p];assert glyph in candidates
   if len(candidates)==1:
    # Independent exact recovery is possible only for a singleton inverse class.
    recovered=candidates[0];assert recovered==glyph;unique_units+=1
   else:
    # j=y/7 and ch=H/ř cannot be uniquely recovered from plaintext.
    # Retain the original glyph label as explicit side information.
    recovered=glyph;alias_units+=1
   raw.append(recovered);plain.append(p)
   tsv.append(f"{line['id']}\t{local_pos}\t{global_pos}\t{glyph}\t{p}")
  elif kind=='separator':raw.append(unit['value']);plain.append(unit['value'])
  elif kind=='unknown_unit':
   local_pos+=1;global_pos+=1
   assert unit['line_index']==local_pos and unit['global_index']==global_pos
   span=rec['spans'][unit['id']];assert span['cipher_unit_count']==1
   assert [key[g] for g in span['glyph_candidates']]==span['plain_candidates']
   tsv.append(f"{line['id']}\t{local_pos}\t{global_pos}\t{'/'.join(span['glyph_candidates'])}\t{'/'.join(span['plain_candidates'])}")
   raw.append('{'+unit['id']+'}');plain.append('['+unit['id']+': '+'/'.join(span['plain_candidates'])+']')
  elif kind in ('unknown_span','overwritten_span'):
   span=rec['spans'][unit['id']];assert span['type']==kind and span['cipher_unit_count'] is None
   raw.append('{'+unit['id']+'}');plain.append('['+unit['id']+': unreadable span]' if kind=='unknown_span' else '['+unit['id']+': uncertain overink]')
  else:raise AssertionError(kind)
 assert ''.join(raw)==line['manual_cipher'],f"Recorded-label roundtrip failed {line['id']}"
 assert len(re.findall(r'\{[^}]+\}|.',line['manual_cipher']))==len(line['units'])
 output.append(line['id']+' '+''.join(plain))
assert global_pos==rec['active_visible_cipher_units']
header=f'PARTIAL; hashes OK ({len(manifest["sha256"])} files); {global_pos} visible positions indexed ({mapped} mapped, {global_pos-mapped} ambiguous); mapped output {base_letters} base letters.'
limits=f'Whole-key inverse: {unique_units} singleton units recovered exactly; {alias_units} alias units require saved glyph labels. Unknown placeholders preserved. Manual record, not automatic pixel proof or independent review.'
literal='\n'.join([header,limits,*output])+'\n';unit_text='\n'.join(tsv)+'\n'
if not args.emit_only:
 assert (W/'decoded-literal.txt').read_text()==literal,'Saved literal differs from current decoding'
 assert (W/'indexed-units.tsv').read_text()==unit_text,'Saved indexed TSV differs from current record'
print(unit_text if args.units else literal,end='')
