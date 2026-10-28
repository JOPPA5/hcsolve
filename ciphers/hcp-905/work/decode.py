#!/usr/bin/env python3
"""Read-only audit and decode of the manual HCP905 Pigpen inventory.
No image recognition; hash/round-trip checks do not establish glyph truth.
"""
import hashlib,json,re
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
C=Path(__file__).resolve().parents[1]; W=C/'work'; R=C.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(name):return json.loads((W/name).read_text())
def main():
 records=load('record-sha256.json')
 for name,expected in records.items():assert sha(W/name)==expected,(name,'record changed')
 inputs=load('input-sha256.json')
 for name,expected in inputs.items():assert sha(R/name)==expected,(name,'immutable input changed')
 d=load('transcript.json');frozen=json.loads((R/'batches/easy-2026-10-28/source-sha256.json').read_text())
 assert set(d['sha256'])=={'picture.jpg','address.jpg','metadata.md'}
 for name,expected in d['sha256'].items():
  assert sha(C/'source'/name)==expected==frozen[f'ciphers/hcp-905/source/{name}']
  print('SHA-256',name,expected)
 key=d['key'];assert key==load('key.json') and len(key)==len(set(key.values()))==24
 reverse={v:k for k,v in key.items()};positions=[];shapes=[];stream=[];active=cancelled=0
 mechanical=[];literal=[];totals=[]
 for row in d['rows']:
  words=[];rowcount=0
  for word in row['words']:
   text=''
   for g in word['glyphs']:
    positions.append(g['id']);rowcount+=1
    assert len(g['center'])==2 and len(g['bbox'])==4
    x,y=g['center'];x0,y0,x1,y1=g['bbox'];assert x0<=x<x1 and y0<=y<y1
    if g['status']=='cancelled':
     assert g['shape'] is None and g['id']==114
     cancelled+=1;text+='[CANCELLED]';stream.append('\ufffc');shapes.append('[CANCELLED]')
    else:
     assert g['status']=='active' and g['shape'] in key
     char=key[g['shape']];text+=char;active+=1;stream.append(char);shapes.append(g['shape'])
   expected=word['notation'].replace('J','I')
   if expected!='[CANCELLED]':expected=''.join(c for c in expected if c.isalpha())
   assert text==expected,(row['row'],text,expected)
   words.append(text)
  mechanical.append(' '.join(words));literal.append(row['literal_with_editorial_J']);totals.append(rowcount)
  # Diplomatic punctuation/J must not conceal a different base letter.
  normalized=row['literal_with_editorial_J'].replace('J','I').replace('[CANCELLED]','\ufffc')
  normalized=''.join(c for c in normalized if c.isalpha() or c=='\ufffc')
  expected=''.join(words).replace('[CANCELLED]','\ufffc')
  assert normalized==expected,(row['row'],'literal versus shape reading differs')
 assert [r['row'] for r in d['rows']]==list(range(1,15))
 assert totals==[17,20,20,21,24,23,23,25,22,28,29,27,32,36]
 assert positions==list(range(1,348)) and active==346 and cancelled==1
 glyphs={g['id']:g for row in d['rows'] for word in row['words'] for g in word['glyphs']}
 assert glyphs[153]['shape']=='E.' and glyphs[156]['shape']=='E' and glyphs[321]['shape']=='S'
 # Whole active plaintext stream is inverted under the complete fixed key;
 # no per-word or per-glyph saved reverse lookup is used to construct it.
 encoded=[reverse[c] if c!='\ufffc' else '[CANCELLED]' for c in ''.join(stream)]
 assert encoded==shapes,'whole-key inverse failed'
 assert '\n'.join(mechanical)+'\n'==(W/'mechanical.txt').read_text()
 assert '\n'.join(literal)+'\n'==(W/'literal.txt').read_text()
 picture=Image.open(C/'source/picture.jpg');font=ImageFont.truetype('/System/Library/Fonts/Monaco.ttf',20)
 for row in d['rows']:
  gs=[g for word in row['words'] for g in word['glyphs']];left=max(0,min(g['center'][0] for g in gs)-22);right=min(1024,max(g['center'][0] for g in gs)+23)
  y=row['y'];box=(left,max(0,y-28),right,min(680,y+27));tile=picture.crop(box).resize(((right-left)*3,(box[3]-box[1])*3))
  expected=Image.new('RGB',(tile.width,tile.height+65),'white');expected.paste(tile,(0,65));draw=ImageDraw.Draw(expected)
  for g in gs:
   x=(g['center'][0]-left)*3;char='X' if g['shape'] is None else key[g['shape']]
   draw.text((x-18,0),str(g['id']),font=font,fill='blue');draw.text((x-5,25),char,font=font,fill='blue');draw.line((x,50,x,65),fill='blue',width=1)
  actual=Image.open(W/f'indexed-{row["row"]:02}.png')
  assert actual.size==expected.size and actual.tobytes()==expected.tobytes(),(row['row'],'indexed aid stale')
 crops=load('review1-crops.json')
 for rec in crops:
  tile=Image.open(C/'source'/rec['source']).crop(rec['box']);s=rec['scale']
  tile=tile.resize((tile.width*s,tile.height*s),Image.Resampling.NEAREST);actual=Image.open(W/rec['file'])
  assert tile.size==actual.size and tile.tobytes()==actual.tobytes(),(rec['file'],'raw-NN crop mismatch')
 print(f'\nAudit: {len(inputs)} immutable input hashes, {len(records)} record hashes, 14 indexed aids and {len(crops)} raw-NN crops OK')
 print('Row totals:',', '.join(map(str,totals)))
 print(f'Total {len(positions)} positions: {active} active glyphs + {cancelled} cancelled field; 24/24 used key classes; whole-fixed-key inverse OK')
 print('Saved mechanical/diplomatic readings OK; glyph classes remain manual, not OCR or proof from hashes.')
 print('\nMechanical I/J-folded reading:')
 for i,line in enumerate(mechanical,1):print(f'{i:02}: {line}')
 print('\nDiplomatic layout (J is editorial for the shared I/J cell):')
 for line in literal:print(line)
if __name__=='__main__':main()
