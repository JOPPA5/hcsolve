"""Authoring utility: manual transcription, never OCR or image recognition."""
from pathlib import Path
from PIL import Image, ImageDraw
import json, hashlib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
key = {'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','b':'p','c':'s','d':'t','f':'v','g':'k','h':'r','m':'n','n':'m','p':'b','q':'z','r':'h','s':'c','t':'d','y':'j','H':'ch'}
(HERE/'key.json').write_text(json.dumps(key,indent=2)+'\n')
rows = [
 ('B01','d4c4s5h1 t4g, t2c4mg3 n3y5, q6 th6r5 bc6mg3, gd5h5',(45,687,645,735),'cw'),
 ('B02','nm5 f584s5 b3d5c483. d6g5 y6 fqb3n4m6n fh585 m6',(45,715,645,763),'cw'),
 ('B03','83mcg5r3 cf6d5r3 f6s86f6. n2c48 yc5n 3t83q4d4',(45,744,645,792),'cw'),
 ('B04','cf3y4 s5cd2 t3 2cd4 m6c85tg5n d3r3, q5 m6c fhHm4',(45,772,645,820),'cw'),
 ('B05','cbh6fs5 n2c48 fs5h6 3t3y5d4 m6 2h5tm4 g3n4cc4',(45,800,645,847),'cw'),
 ('B06','t3 H3sm5. b3y5t2 m1m4 rm5t 3tc2t q 2h6t2, gt5',(45,832,645,879),'cw'),
 ('B07','n6n y4q cf6 q6f6q6t86. p2t2 nm3r3 fqb3n4m6d4',(45,859,645,907),'cw'),
 ('B08','m6 cf32 q86d32 6m2cg2, gd5h32 fh585 qth6f4n 6',(45,886,645,938),'cw'),
 ('B09','d4c4sgh6d5 84p6n.',(45,915,345,960),'cw'),
 ('M01','3t5c486n 84cd5g y4q q bh6r1, b3m5f6tq b3cd3fm4',(337,557,970,611),'180'),
 ('M02','s5cd6 q 2cd4 t3 q4h3fm4s5 dhf6 6c4 tf6 tm1.',(337,598,970,654),'180'),
]
im=Image.open(ROOT/'source/picture.jpg')
rec={'schema':1,'method':'Manual image transcription, not OCR. H labels a single handwritten CH sign (r with caron-like stroke). y labels the 7-shaped J sign. Indexes count glyphs/punctuation/spaces; U01 marks partly obscured signs y5, (B01) and U02 a restored sign r (M01); see uncertainties. Row rectangles are navigation crops and include adjacent ascenders/descenders, not character bounding boxes.','source_sha256':{p.name:sha(p) for p in sorted((ROOT/'source').iterdir()) if p.is_file()},'key_sha256':sha(HERE/'key.json'),'uncertainties':{
 'U01':{'row':'B01','positions':[25,26,27],'symbols':'y5,','status':'partly obscured','reason':'Printed red cherry covers the tops of the signs after n3 (MO). Visible lower parts: angular 7-shaped descender of y (J, cf. yc5n B03, 3t3y5d4 B05), lower bowl of 5 (E), then a long slanting stroke read as a probable comma (longer than the writer\'s other commas). Read JE, = MOJE, (revised 2026-10-29 after review 1, finding 2).'},
 'U02':{'row':'M01','positions':[26],'symbols':'r','status':'restored','reason':'R of PRAHY (bh6r1) is not visible: hidden under the printed leaf stem or extremely faint. Restored from context and the PRAHA 7 postmark on the address side (review 1, finding 3).'}},'rows':[]}
for rid,s,box,orient in rows:
    tokens=[]; i=0
    while i<len(s):
        if s.startswith('[U01]',i):
            tokens.append({'kind':'span','id':'U01','glyph_count':None});i+=5
        else:
            c=s[i]; tokens.append({'kind':'glyph' if c in key else 'layout','symbol':c});i+=1
    for j,tok in enumerate(tokens,1):tok['position']=j
    rec['rows'].append({'id':rid,'orientation':orient,'crop_box':box,'transcription':s,'tokens':tokens})
    base=im.rotate(-90,expand=True) if orient=='cw' else im.rotate(180,expand=True)
    crop=base.crop(box).resize(((box[2]-box[0])*3,(box[3]-box[1])*3))
    # A position legend below the scan records exact transcription indexes without
    # implying automatically found pixel-to-glyph boundaries.
    lines=[]
    for st in range(0,len(tokens),16):
        lines.append('  '.join(f"{t['position']:02}:{t.get('symbol','[U01]') if t.get('symbol')!=' ' else '_'}" for t in tokens[st:st+16]))
    panel=Image.new('RGB',(max(crop.width,1200),crop.height+30+len(lines)*25),'white')
    panel.paste(crop,(0,0));d=ImageDraw.Draw(panel)
    d.text((5,crop.height+3),f'{rid}: manual token positions; _ = space; U01, U02 = see uncertainties in transcription.json',fill='black')
    for j,l in enumerate(lines):d.text((5,crop.height+27+j*25),l,fill='black')
    panel.save(HERE/f'panel-{rid}.png')
(HERE/'transcription.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
(HERE/'record-sha256.json').write_text(json.dumps({p.name:sha(p) for p in [HERE/'key.json',HERE/'transcription.json']},indent=2)+'\n')
