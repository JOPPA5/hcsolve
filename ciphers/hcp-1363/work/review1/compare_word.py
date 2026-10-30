#!/usr/bin/env python3
"""Response to review 1: compare the line-1 word with this card's f, j and h, and with accepted Mpwjoh."""
from PIL import Image, ImageDraw
from pathlib import Path
D=Path(__file__).resolve().parents[2]
im=Image.open(D/'work/hires/pc_hcp_44_adr.JPG').rotate(90,expand=True).convert('RGB')
panels=[('this card, line 1 (was Mpwfs): M p w j o h',(680,950,990,1075)),
        ('this card, line 4 Mpwf: f has a closed foot loop',(780,1265,1075,1390)),
        ('this card, line 4 Xjoetps: j with hooked foot',(370,1260,480,1390)),
        ('this card, line 6 h: stem falling to a low blob',(800,1450,890,1540))]
rows=[]
for t,b in panels:
    c=im.crop(b); rows.append((t,c.resize((c.width*3,c.height*3),Image.LANCZOS)))
for t,p in [('hcp-1361 accepted Mpwjoh',D.parent/'hcp-1361/work/crops/l2b.png'),('hcp-1367 accepted Mpwjoh',D.parent/'hcp-1367/work/crops/l1b.png')]:
    c=Image.open(p).convert('RGB'); s=900/c.width
    rows.append((t,c.resize((900,int(c.height*s)),Image.LANCZOS)))
W=max(r.width for _,r in rows)+20; H=sum(r.height+24 for _,r in rows)
o=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(o); y=0
for t,r in rows:
    d.text((6,y+6),t,fill='black'); o.paste(r,(6,y+22)); y+=r.height+24
o.save(D/'work/review1/cmp_mpwjoh_1363.png'); print(o.size)
