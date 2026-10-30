#!/usr/bin/env python3
"""Read-only verification of a MANUAL transcription. Never OCR or visual proof."""
import hashlib,json,re
from pathlib import Path
W=Path(__file__).resolve().parent;R=W.parent.parent.parent

def main():
 hashes=json.loads((W/'audit-sha256.json').read_text())
 for name,digest in hashes.items():
  assert hashlib.sha256((R/name).read_bytes()).hexdigest()==digest, 'Hash mismatch: '+name
 key=json.loads((W/'key.json').read_text())
 inv=json.loads((W/'inventory.json').read_text())
 assert len(set(key.values()))==len(key),'Key must be injective'
 assert (W/'transcription.txt').read_text()=='\n'.join(r['transcription'] for r in inv['rows'])+'\n'
 flat=[];literals=[]
 for row in inv['rows']:
  assert len(row['upright_bbox'])==4
  tokenized=re.findall(r'\{[^}]+\}|.',row['transcription'])
  assert tokenized==[t['cipher'] for t in row['tokens']]
  cursor=0;glyphs=[];literal=[];roundtrip=[]
  for token in row['tokens']:
   c=token['cipher'];p=token['plaintext']
   assert token['index']==len(roundtrip)+1
   assert token['raw_start']==cursor and token['raw_end']==cursor+len(c)
   assert row['transcription'][cursor:cursor+len(c)]==c
   cursor+=len(c)
   if c.startswith('{'):
    options=c[1:-1].split('|');assert all(x in key for x in options)
    assert p=='{'+'|'.join(key[x] for x in options)+'}'
   elif c in key: assert p==key[c]
   else: assert c in ' .,!?-' and p==c
   if token['glyph_index'] is not None:
    g=row['glyphs'][len(glyphs)]
    assert g['index']==len(flat)+len(glyphs)+1==token['glyph_index']
    assert g['row']==row['id'] and g['row_glyph']==len(glyphs)+1
    assert g['token_index']==token['index'] and g['raw_char_offset']==token['raw_start']
    assert g['cipher']==c and g['plaintext']==p
    glyphs.append(g)
   else: assert c not in key and not c.startswith('{')
   # Token-preserving re-encoding: a CH token cannot split into unrelated c,h;
   # alternatives stay alternatives. This does not prove the visual reading.
   inverse={v:k for k,v in key.items()}
   if c.startswith('{'): back='{'+ '|'.join(inverse[x] for x in p[1:-1].split('|'))+'}'
   else: back=inverse.get(p,p)
   assert back==c
   roundtrip.append(back);literal.append(p)
  assert ''.join(roundtrip)==row['transcription'] and cursor==len(row['transcription'])
  assert ''.join(literal)==row['literal']
  assert glyphs==row['glyphs'] and glyphs[0]['index']==row['first_glyph'] and glyphs[-1]['index']==row['last_glyph']
  flat.extend(glyphs);literals.append(row['literal'])
 assert flat==inv['glyphs']
 assert '\n'.join(literals)+'\n'==(W/'literal-czech.txt').read_text()
 assert inv['canceled_ink']==[] and inv['unknown_length_spans']==[]
 print(f'{len(hashes)} source, key, reference and manual-record hashes verified.')
 print(f'{len(inv["rows"])} rows; {len(flat)} indexed glyphs; '+str(sum(g['status']=='bounded_alternative' for g in flat))+' bounded alternatives; no unknown-length spans identified.')
 print('Indexed positions, key application and exact token round trip verified. These checks are not OCR or visual proof.\n')
 print('\n'.join(literals))
if __name__=='__main__':main()
