#!/usr/bin/env python3
"""Read-only manual record audit and fixed-key decoding; no OCR or network."""
from pathlib import Path
import hashlib,json,re
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
 source=load('source-sha256.json');frozen=json.loads((R/'batches/easy-2026-10-28/cz239-241-source-sha256.json').read_text())
 assert set(source)=={'picture.jpg','address.jpg','metadata.md'}
 for name,expected in source.items():assert sha(C/'source'/name)==expected==frozen[f'ciphers/hcp-1560/source/{name}']
 exclusion=json.loads((R/'register-exclusions.json').read_text()).get('entries',{}).get('1560',{})
 assert not exclusion.get('exclude_from_register',False) and not exclusion.get('exclude_from_new_discovery_count',False),'human exclusion now applies to target'
 key=load('key.json');family=json.loads((R/'ciphers/hcp-1520/work/key.json').read_text())
 assert key=={c:p.upper() for c,p in dict(family,v='f').items()}
 assert len(key)==len(set(key.values()))==23
 rows=load('rows.json')['rows'];positions=load('positions.json');unknowns=load('uncertainties.json')
 assert [r['id'] for r in rows]==[f'R{i:02}' for i in range(1,16)]
 raw='\n'.join(row['cipher'] for row in rows)+'\n';assert raw==(W/'transcription.txt').read_text()
 im=Image.open(C/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270);assert im.size==(674,1024)
 up=Image.open(W/'upright.png');assert up.size==im.size and up.tobytes()==im.tobytes()
 seen=[];outputs=[];ids=[];known=0
 for row in rows:
  out=[];ordinal=0;parsed=list(re.finditer(r'⟦U\d+⟧|.',row['cipher']))
  assert len(parsed)==len(row['tokens'])
  for match,item in zip(parsed,row['tokens']):
   token=match.group();assert item['column']==match.start()+1
   if token in key:
    known+=1;ordinal+=1
    assert item==dict(column=match.start()+1,type='glyph',cipher=token,base=key[token],known_index=known,row_known_ordinal=ordinal)
    seen.append(dict(known_index=known,row=row['id'],row_known_ordinal=ordinal,column=match.start()+1,label=token,base=key[token]));out.append(key[token])
   elif token.startswith('⟦'):
    ident=token[1:-1];assert item['type']=='unknown' and item['id']==ident and ident in unknowns
    assert unknowns[ident]['row']==row['id'] and unknowns[ident]['unit_count'] is None
    ids.append(ident);out.append(token)
   else:
    assert token in ' .,!?-' and item==dict(column=match.start()+1,type='separator',text=token);out.append(token)
  plain=''.join(out);assert plain==row['plaintext'] and ordinal==row['known_units'];outputs.append(plain)
  tile=im.crop(row['native_box']);s=row['crop_scale'];tile=tile.resize((tile.width*s,tile.height*s),Image.Resampling.NEAREST);actual=Image.open(W/row['crop'])
  assert tile.size==actual.size and tile.tobytes()==actual.tobytes(),(row['id'],'row crop mismatch')
 assert positions==seen and known==509 and sum(len(p['base']) for p in seen)==516
 assert sum(p['label']=='H' for p in seen)==7 and len(set(p['label'] for p in seen))==22
 assert not any(p['label']=='v' for p in seen)
 assert ids==['U1','U2','U3'] and set(ids)==set(unknowns)
 literal='\n'.join(outputs)+'\n';assert literal==(W/'literal.txt').read_text()
 # Actual whole-plaintext inverse under the ENTIRE fixed 23-entry key.
 # Unknown annotations remain opaque; they are not one presumed cipher unit.
 inverse={p:c for c,p in key.items()};encoded=[];offset=0
 while offset<len(literal):
  marker=re.match(r'⟦U\d+⟧',literal[offset:])
  if marker:encoded.append(marker.group());offset+=len(marker.group());continue
  if literal[offset:offset+2]=='CH':encoded.append(inverse['CH']);offset+=2
  else:encoded.append(inverse.get(literal[offset],literal[offset]));offset+=1
 assert ''.join(encoded)==raw,'whole-plaintext fixed-key inverse mismatch'
 controls=load('source-controls.json');assert controls['source_sha256']==source['picture.jpg']
 for rec in controls['controls']:
  tile=im.crop(rec['native_box']);s=rec['scale'];tile=tile.resize((tile.width*s,tile.height*s),Image.Resampling.NEAREST);actual=Image.open(W/rec['file'])
  assert tile.size==actual.size and tile.tobytes()==actual.tobytes(),rec['file']
 display=lambda value:value.replace('⟦','[').replace('⟧',']')
 font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',17);small=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',15)
 for k in range(0,15,5):
  part=rows[k:k+5];height=sum(62+(r['native_box'][3]-r['native_box'][1])*3 for r in part);expected=Image.new('RGB',(1900,height),'white');draw=ImageDraw.Draw(expected);y=0
  for row in part:
   draw.text((8,y),row['id']+' '+display(row['plaintext']),font=font,fill='black');draw.text((8,y+22),'Native box '+str(row['native_box'])+'; source NN3x; cipher '+display(row['cipher']),font=small,fill='black')
   tile=im.crop(row['native_box']);tile=tile.resize((tile.width*3,tile.height*3),Image.Resampling.NEAREST);expected.paste(tile,(8,y+54));y+=tile.height+62
  actual=Image.open(W/f'indexed-rows-{k+1:02}-{k+len(part):02}.png');assert expected.size==actual.size and expected.tobytes()==actual.tobytes()
 for k in range(0,len(controls['controls']),5):
  part=controls['controls'][k:k+5];height=sum(51+(r['native_box'][3]-r['native_box'][1])*r['scale'] for r in part);expected=Image.new('RGB',(1900,height),'white');draw=ImageDraw.Draw(expected);y=0
  for rec in part:
   draw.text((8,y),rec['description'],font=font,fill='black');draw.text((8,y+22),'Native box '+str(rec['native_box'])+'; nearest-neighbor '+str(rec['scale'])+'x',font=small,fill='black')
   tile=im.crop(rec['native_box']);tile=tile.resize((tile.width*rec['scale'],tile.height*rec['scale']),Image.Resampling.NEAREST);expected.paste(tile,(8,y+46));y+=tile.height+51
  actual=Image.open(W/f'control-panel-{k//5+1}.png');assert expected.size==actual.size and expected.tobytes()==actual.tobytes()
 print(f'PASS: 3 own original guard entries; {len(inputs)} immutable input hashes; {len(refs)} reference hashes; {len(records)} canonical record hashes')
 print('PASS: 15 physical rows; 509 known units; 516 known base letters; 7 CH; 22/23 classes used; F unused')
 print('PASS: source order/global known-index/row ordinal/text columns; saved literal; actual whole-fixed-key inverse with CH')
 print('PASS: native clockwise rotation, 15 raw row crops, 16 raw-NN controls, 3 indexed and 4 control panels')
 print('Known row counts:',','.join(str(r['known_units']) for r in rows))
 print('UNKNOWN: U1/U2 concealed cipher spans and U3 unclassified ink span all have unasserted lengths; total original units/coverage unknown.')
 print('U3 may contain punctuation/correction/no additional active unit. No cancellation or missing letter count is inferred.')
 print('CAUTION: manual transcription, not OCR. Hash/pixel-reproduction/inverse checks are record consistency, not glyph truth or acceptance. No novelty/submission claim.')
 for row,plain in zip(rows,outputs):print(row['id']+' '+plain)
if __name__=='__main__':main()
