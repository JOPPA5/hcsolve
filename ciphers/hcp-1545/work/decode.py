#!/usr/bin/env python3
"""Read-only verification of linked manual transcription and fixed-key decode."""
from pathlib import Path
from collections import Counter
import hashlib,json,csv,io,re
from PIL import Image,ImageChops
R=Path(__file__).resolve().parents[1];W=R/'work';BASE=R.parents[1]
for manifest,base in [('source-sha256.json',R),('record-sha256.json',R),('reference-sha256.json',BASE)]:
 for filename,wanted in json.loads((W/manifest).read_text()).items():
  assert hashlib.sha256((base/filename).read_bytes()).hexdigest()==wanted, f'Hash mismatch: {filename}'
key=json.loads((W/'key.json').read_text());prior=json.loads((BASE/'ciphers/hcp-1527/work/key.json').read_text())
assert key==prior, 'Key changed from pre-target family key'
assert len(set(key.values()))==len(key);inverse={v:k for k,v in key.items()}
rec=json.loads((W/'transcription.json').read_text());positions=[];texts=[];known=0;unknown=0;ch=0;total=0;counts=Counter()
orig=Image.open(R/'source/picture.jpg');imgs={'ROTATE_270':orig.transpose(Image.Transpose.ROTATE_270),'ROTATE_180':orig.transpose(Image.Transpose.ROTATE_180)}
def encode_actual(text):
 # Fixed inverse over the whole decoded stream, greedily treating CH as one unit.
 # No per-position plaintext-to-glyph associations are learned from this card.
 out=[];i=0
 while i<len(text):
  if text[i]=='[':
   end=text.index(']',i);out.append('{'+text[i+1:end]+'}');i=end+1;continue
  if text[i:i+2]=='CH':out.append(inverse['CH']);i+=2;continue
  c=text[i];out.append(inverse.get(c,c));i+=1
 return ''.join(out)
for row in rec['rows']:
 idx=0;out=[]
 for token in re.findall(r'\{U\d+\}|.',row['cipher']):
  if token in key:
   idx+=1;total+=1;known+=1;ch+=token=='ř';counts[token]+=1;plain=key[token];status='mapped'
  elif token.startswith('{U'):
   uid=token[1:-1];assert uid in rec['unknown_regions'];idx+=1;total+=1;unknown+=1;plain='['+uid+']';status='unknown_region_1-2_units'
  else:
   assert token in ' .,;?-"';out.append(token);continue
  positions.append([str(total),row['id'],str(idx),token,plain,status]);out.append(plain)
 text=''.join(out);assert text==row['plaintext'];assert idx==row['indexed_items'];assert encode_actual(text)==row['cipher']
 crop=imgs[row['orientation']].crop(row['box']);crop=crop.resize((crop.width*4,crop.height*4));assert ImageChops.difference(crop,Image.open(W/(row['id']+'.png'))).getbbox() is None
 texts.append(text);print(text)
assert len(rec['rows'])==15
assert (W/'plaintext.txt').read_text()=='\n'.join(texts)+'\n'
assert list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:]==positions
print(f'\nVerified: 3 immutable source files; 4 pre-target references; fixed unchanged key; all 15 row crops, all {total} indexed items; {known} mapped cipher units + {unknown} unidentified non-key mark (U01: one small dotted oval after PRIJEDE, probably not a letter; legacy status label in positions.csv); {ch} CH units; saved plaintext and index equality; whole-stream inverse-key reconstruction (no aliases).')
print('This checks transcription consistency, not automatic image reading or independent review. R07 KOLUBENKU and R09 ANUNKO remain source-literal; R08 U01 is an unidentified non-key mark, kept visible as [U01]. Complete reading of all key letters. Diacritic interpretation is editorial.')
print('Key inventory:',' '.join(f'{k}:{counts[k]}' for k in key))
