"""Round-2 recheck: 4x crops of every row of the upright picture side (not part of reproduction)."""
import json,sys
from pathlib import Path
from PIL import Image
p=Path(__file__).resolve().parent; w=p.parent; root=w.parent
im=Image.open(root/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
rows=json.loads((w/'transcription.json').read_text())['rows']
for r in rows:
    x0,y0,x1,y1=r['box']
    c=im.crop((x0,y0-4,x1,y1+4))
    c=c.resize((c.width*3,c.height*3),Image.LANCZOS)
    c.save(p/f"row_{r['id']}.png")
# sheets of rows
def sheet(ids,name):
    cs=[Image.open(p/f'row_{i}.png') for i in ids]
    W=max(c.width for c in cs);H=sum(c.height for c in cs)
    s=Image.new('RGB',(W,H),'white');y=0
    for c in cs: s.paste(c,(0,y));y+=c.height
    s.save(p/name)
sheet(['U01','U02','U03','U04'],'sheet_U1.png')
sheet(['U05','U06','U07'],'sheet_U2.png')
sheet(['S01','S02','S03','S04','S05','S06','S07'],'sheet_S1.png')
sheet(['S08','S09','S10','S11','S12','S13'],'sheet_S2.png')
sheet(['L01','L02'],'sheet_L1.png')
sheet(['L03','L04'],'sheet_L2.png')
