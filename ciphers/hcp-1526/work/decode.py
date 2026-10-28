#!/usr/bin/env python3
"""Read-only manual-transcription audit/decode; not OCR or glyph recognition."""
import hashlib,json,difflib
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
C=Path(__file__).resolve().parents[1];W=C/'work';R=C.parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(name):return json.loads((W/name).read_text())
def main():
 records=load('record-sha256.json')
 for name,expected in records.items():assert sha(W/name)==expected,(name,'canonical record changed')
 inputs=load('input-sha256.json')
 for name,expected in inputs.items():assert sha(R/name)==expected,(name,'immutable input changed')
 refs=load('reference-sha256.json')
 for name,expected in refs.items():assert sha(R/name)==expected,(name,'reference changed')
 exclusions=json.loads((R/'register-exclusions.json').read_text()).get('entries',{}).get('1526',{})
 assert not exclusions.get('exclude_from_register',False),'1526 is now explicitly excluded: honor current human scope'
 assert not exclusions.get('exclude_from_new_discovery_count',False),'1526 is now explicitly excluded: honor current human scope'
 source=load('source-sha256.json');frozen=json.loads((R/'batches/easy-2026-10-28/cz207-209-source-sha256.json').read_text())
 assert set(source)=={'source/picture.jpg','source/address.jpg','source/metadata.md'}
 for name,expected in source.items():assert sha(C/name)==expected==frozen[f'ciphers/hcp-1526/{name}']
 key=load('key.json');record=load('transcription.json');rows=record['rows'];positions=load('positions.json')
 assert len(key)==len(set(key.values()))==23
 assert [r['id'] for r in rows]==[f'R{i:02}' for i in range(1,17)]
 raw='\n'.join(r['cipher'] for r in rows)+'\n';assert raw==(W/'transcription.txt').read_text()
 outputs=[];seen=[];global_position=0
 for row in rows:
  text=row['cipher'];assert all(c in key or c in ' .,!' for c in text)
  output=''.join(key.get(c,c) for c in text);assert output==row['plaintext']
  row_index=0
  for column,c in enumerate(text,1):
   if c in key:
    row_index+=1;global_position+=1
    seen.append(dict(position=global_position,row=row['id'],index=row_index,column=column,label=c,base=key[c]))
  assert row_index==row['active_units'];outputs.append(output)
 assert positions==seen
 literal='\n'.join(outputs)+'\n';assert literal==(W/'transcript.txt').read_text()
 assert [r['active_units'] for r in rows]==[30,30,31,35,31,28,34,32,32,32,30,30,34,35,34,19]
 assert len(seen)==497 and sum(len(x['base']) for x in seen)==504
 assert sum(x['label']=='ř' for x in seen)==7 and sum(x['label']=='v' for x in seen)==1
 assert set(key)==set(x['label'] for x in seen)
 # The ENTIRE plaintext is inverse-encoded with the complete key, greedy CH.
 # Saved per-unit source labels are not consulted during inverse construction.
 inverse={plain:cipher for cipher,plain in key.items()};encoded=[];offset=0
 while offset<len(literal):
  if literal[offset:offset+2]=='CH':encoded.append(inverse['CH']);offset+=2
  else:
   c=literal[offset];encoded.append(inverse.get(c,c));offset+=1
 assert ''.join(encoded)==raw,'whole-plaintext fixed-key inverse failed'
 corrections=load('review1-corrections.json')['word_sites'];assert len(corrections)==10
 replacements=insertions=0
 for change in corrections:
  row=rows[int(change['row'][1:])-1]
  assert change['new_cipher'] in row['cipher'].replace(',','').replace('.','').split()
  assert ''.join(key[c] for c in change['new_cipher'])==change['new_base']
  assert ''.join(key[c] for c in change['old_cipher'])==change['old_base']
  for op,a0,a1,b0,b1 in difflib.SequenceMatcher(None,change['old_cipher'],change['new_cipher'],autojunk=False).get_opcodes():
   if op=='replace':assert a1-a0==b1-b0;replacements+=b1-b0
   elif op=='insert':insertions+=b1-b0
   else:assert op=='equal'
 assert replacements==9 and insertions==2
 im=Image.open(C/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
 assert im.size==(674,1024)
 upright=Image.open(W/'upright.png');assert upright.size==im.size and upright.tobytes()==im.tobytes()
 controls=load('review1-controls.json');assert controls['source_sha256']==source['source/picture.jpg']
 for rec in controls['controls']:
  tile=im.crop(rec['bbox']);s=rec['scale'];assert rec['resampling']=='nearest'
  tile=tile.resize((tile.width*s,tile.height*s),Image.Resampling.NEAREST);actual=Image.open(W/rec['file'])
  assert tile.size==actual.size and tile.tobytes()==actual.tobytes(),rec['file']
 font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',18)
 small=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',16)
 for k in range(0,16,4):
  expected=Image.new('RGB',(1250,700),'white');draw=ImageDraw.Draw(expected)
  for j,row in enumerate(rows[k:k+4]):
   y=j*175;draw.text((8,y+1),row['id']+' '+row['plaintext'],font=font,fill='black');draw.text((8,y+25),row['cipher'],font=small,fill='black')
   tile=im.crop(row['bbox']);tile=tile.resize((tile.width*2,tile.height*2));expected.paste(tile,(8,y+53))
  actual=Image.open(W/f'indexed-rows-{k+1:02}-{k+4:02}.png')
  assert expected.size==actual.size and expected.tobytes()==actual.tobytes(),'stale indexed row panel'
 print(f'PASS: 3 original guards; {len(inputs)} immutable inputs; {len(refs)} reference hashes; {len(records)} canonical record hashes')
 print('PASS: current register-exclusions has no exclusion for 1526; no submission/novelty claim')
 print('PASS: 16 rows; 497 active units; 504 output base letters; 7 CH units; 23/23 labels; 1 contextual F')
 print('PASS: global/row/column position indices, saved literal, 9 replacements +2 inserted units, whole-plaintext fixed-key inverse')
 print('PASS: native upright pixels, 12 raw-NN controls and four refreshed indexed panels')
 for row,output in zip(rows,outputs):print(row['id']+' '+output)
 print('CAUTION: shallow v/F in DOUFAM remains target-specific/contextual, not proven to be public G16. Accents/repairs are editorial.')
 print('Literal slips retained: SECONA PRNEM CRDECKO KDERE ZACE SETRIDI DO DUTKLIVA VZDIT KDERY. Manual transcription, not OCR; hashes/inverse are not glyph truth.')
 print('Manual transcription SHA-256: '+sha(W/'transcription.json'))
if __name__=='__main__':main()
