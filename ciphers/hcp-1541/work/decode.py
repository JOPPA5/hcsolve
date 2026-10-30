#!/usr/bin/env python3
"""Read-only audit of manual transcription. Not OCR or visual proof."""
import hashlib,json,re
from pathlib import Path
W=Path(__file__).resolve().parent;R=W.parent.parent.parent

def main():
 hashes=json.loads((W/'audit-sha256.json').read_text())
 for path,digest in hashes.items():
  assert hashlib.sha256((R/path).read_bytes()).hexdigest()==digest,'Hash mismatch: '+path
 key=json.loads((W/'key.json').read_text());inv=json.loads((W/'inventory.json').read_text())
 assert len(set(key.values()))==len(key)
 # This inverse comes from the actual fixed substitution key, never from a
 # token's recorded plaintext/cipher pair. No guessed G assignment is added.
 inverse={plain:cipher for cipher,plain in key.items()}
 assert 'g' not in inverse
 assert (W/'transcription.txt').read_text()=='\n'.join(r['transcription'] for r in inv['rows'])+'\n'
 flat=[];literals=[];seen_unknowns=[];span_records=[];decoded_count=0
 for row in inv['rows']:
  parsed=re.findall(r'\[U\d+\]|.',row['transcription'])
  assert parsed==[t['cipher'] for t in row['tokens']]
  cursor=0;literal=[];encoded=[];localglyphs=[]
  for ti,token in enumerate(row['tokens'],1):
   c=token['cipher'];p=token['plaintext'];kind=token['kind']
   assert token['index']==ti and token['raw_start']==cursor and token['raw_end']==cursor+len(c)
   assert row['transcription'][cursor:cursor+len(c)]==c
   cursor+=len(c)
   if c in key:
    assert kind=='read' and p==key[c]
    back=inverse[p];assert back==c;decoded_count+=1
   elif c.startswith('[U'):
    uid=c[1:-1];u=inv['unknowns'][uid]
    assert p==c and kind==u['kind'];seen_unknowns.append(uid)
    # Unknown placeholders are copied as explicit labels, NOT decrypted or
    # claimed to pass a key inverse. U02/U03 have unknown character counts.
    back=c
    if kind=='unknown_length_span':
     s=inv['unknown_length_spans'][len(span_records)]
     assert s['id']==uid and s['row']==row['id'] and s['token_index']==ti
     assert s['raw_char_offset']==token['raw_start']
     assert s['preceding_global_glyph']==len(flat)+len(localglyphs)
     span_records.append(s)
   else:
    assert kind=='separator' and c in ' .,!?-' and p==c;back=c
   if token['glyph_index'] is not None:
    g=row['glyphs'][len(localglyphs)]
    assert g['index']==len(flat)+len(localglyphs)+1==token['glyph_index']
    assert g['row']==row['id'] and g['row_glyph']==len(localglyphs)+1
    assert g['token_index']==ti and g['raw_char_offset']==token['raw_start']
    assert g['cipher']==c and g['plaintext']==p and g['status']==kind
    localglyphs.append(g)
   else:assert kind in ('separator','unknown_length_span')
   literal.append(p);encoded.append(back)
  assert cursor==len(row['transcription'])
  assert ''.join(encoded)==row['transcription'] and ''.join(literal)==row['literal']
  assert localglyphs==row['glyphs']
  assert localglyphs[0]['index']==row['first_glyph'] and localglyphs[-1]['index']==row['last_glyph']
  flat.extend(localglyphs);literals.append(row['literal'])
 assert flat==inv['glyphs'] and set(seen_unknowns)==set(inv['unknowns'])
 assert span_records==inv['unknown_length_spans'] and len(span_records)==2
 assert inv['canceled_ink']==[]
 assert (W/'literal-czech.txt').read_text()=='\n'.join(literals)+'\n'
 print(f'{len(hashes)} immutable-source, reference, key and manual-record hashes verified.')
 print(f'{len(inv["rows"])} rows; {len(flat)} indexed visible units: {decoded_count} key-decoded, 1 unassigned visible glyph.')
 print('Two additional dark spans have unknown glyph counts and are excluded from the unit count.')
 print('Known units pass actual fixed-key inverse and exact token round trip; unknown labels remain unresolved.')
 print('These checks are manual-record consistency, not OCR or visual proof.\n')
 print('\n'.join(literals))
if __name__=='__main__':main()
