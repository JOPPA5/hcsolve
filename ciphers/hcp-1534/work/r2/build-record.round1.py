from pathlib import Path
import json,hashlib,csv
from PIL import Image,ImageDraw
p=Path(__file__).resolve().parent; root=p.parent
# Literal shape labels, authored from the full upright source; ? is unresolved overink.
rows=[
('U01',(35,50,634,83),'cht5sg3 n375 75t4m5, fh581 t4g q6 fs5h57c4 th6r1 84cd5g,'),
('U02',(35,78,634,112),'75mq nm5 b3d5c48. 86cg6 df375 ?nm5, th6r32cg2, m5cn4hm5'),
('U03',(35,106,634,141),'p86q4 6 75 n4 m57n4857c4 2d5r32, gt1q m57c5n c6n c5'),
('U04',(35,132,634,168),'c5p32 6 c5 cf5d5n nm5 3pg83b274s4n cb3g375m. fqb3n4-'),
('U05',(35,158,634,194),'m6n m6 cf374 r382p4sg2 s4cd32 d6g h6t 6 d6g s6cd3.'),
('U06',(35,185,634,221),'cd1cg6 c5 n4 b3 m4 f584s5. 3t5 tm5cg6 q6 n5c4s b375t2'),
('U07',(35,211,634,245),'m6 f1h3sm4 cH2q4 s5s48cg32, g m4q c5 d5md3gh6d5'),
('S01',(437,241,631,276),'c75t32 f6cg5h4'),
('S02',(474,269,631,304),'2t3f5 f5 cf5d5'),
('S03',(500,297,633,332),'c4h5n h3qdh32-'),
('S04',(484,324,633,360),'c5m4. t32F68'),
('S05',(492,353,631,386),'7c5n, q5 t3 d5'),
('S06',(495,380,631,413),'t3p1 p2t2'),
('S07',(498,408,635,443),'6cb3m c g3m-'),
('S08',(498,435,634,469),'s5hd5n cf5'),
('S09',(500,463,635,496),'bh6s5 r3d3f,'),
('S10',(490,490,635,524),'6fc6g bh3 m6-'),
('S11',(492,519,635,552),'f68 bh6s5 g6m-'),
('S12',(494,547,635,583),'s586hcg5 c3df6'),
('S13',(508,576,636,609),'d3r3 t3c6rm2.'),
('L01',(31,901,628,937),'cf5 d6g f6cm4f5 n486f6m5 cht5sg3 fh585 g c3p5'),
('L02',(31,929,628,963),'d4cgm5 6 d4c4s t832r1H, 284pm1H b2c n2 b3c486,'),
('L03',(30,954,628,985),'f5hm5 75r3 b5b32c, gd5h1 c5 m6 c84p5m32 t58c4'),
('L04',(30,975,431,1003),'q6p6f2 m5cn4hm5 d5c4.'),
]
key={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','7':'J','8':'L','q':'Z','g':'K','f':'V','h':'R','t':'D','r':'H','c':'S','s':'C','n':'M','m':'N','p':'B','b':'P','d':'T','H':'CH','F':'F','?':'[?]'}
meta={'source_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((root/'source').iterdir())},'coordinates':'picture.jpg lossless transpose 90 degrees counterclockwise; upright width=674 height=1024','unknown':'U02 overinked composite before MNE has unknown original component count; possible JE remains unassigned. S04 shallow-v/F was contextually inferred first, then compared to the photographed published proposed F in card199 RUDOLFINA; reference transfer, not independent validation.','rows':[{'id':n,'box':box,'cipher':s} for n,box,s in rows]}
(p/'transcription.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n'); (p/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
with (p/'indexed-units.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['ordinal','row','row_unit','glyph_label','plain','row_box'])
 k=0
 for n,box,s in rows:
  j=0
  for c in s:
   if c in key:
    k+=1;j+=1;w.writerow([k,n,j,c,key[c],','.join(map(str,box))])
manifest={f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in ['transcription.json','key.json','indexed-units.csv']}; (p/'record-hashes.json').write_text(json.dumps(manifest,indent=2)+'\n')
im=Image.open(root/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90); draw=ImageDraw.Draw(im)
for n,box,s in rows:
 draw.rectangle(box,outline='red',width=1);draw.text((box[0],box[1]-9),n,fill='red')
im.save(p/'indexed.png')
print(k)
