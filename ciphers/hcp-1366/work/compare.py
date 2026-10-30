#!/usr/bin/env python3
"""Comparison sheet for line 1 of hcp-1366 (run from this directory with the PIL python)."""
from PIL import Image, ImageDraw
def rot(p):
    i=Image.open(p).convert('RGB'); W=i.size[0]
    return i.rotate(90,expand=True),W
r,W=rot('hires/pc_hcp_47_adr.JPG')
m=r.crop((340,W-930,1100,W-180))
s=rot('../../hcp-1367/work/crops/msg.png')[0] if False else Image.open('../../hcp-1367/work/crops/l1b.png').convert('RGB')
t=Image.open('../../hcp-1361/work/crops/l2b.png').convert('RGB')
parts=[('1366 line 1 end: read here as Mpwjoh',m.crop((400,140,680,260)),4),
       ('hcp-1367 (FINAL) Mpwjoh Cpz',s,2),
       ('hcp-1361 (FINAL) Mpwjoh',t,2),
       ('1366 line 4 Mpwf: f foot is a closed loop',m.crop((30,440,330,550)),4),
       ('1366 line 6 Hjsm: j with open hooked foot',m.crop((390,640,660,730)),4),
       ('1366 line 6 first initial, then Nz of line 1',m.crop((130,610,300,700)),4),
       ('',m.crop((130,170,240,230)),4)]
ims=[(a,p.resize((p.size[0]*k,p.size[1]*k),Image.LANCZOS)) for a,p,k in parts]
w=max(p.size[0] for _,p in ims); h=sum(p.size[1]+24 for _,p in ims)
o=Image.new('RGB',(w,h),'white'); d=ImageDraw.Draw(o); y=0
for a,p in ims:
    d.text((4,y+4),a,fill='black'); y+=24; o.paste(p,(0,y)); y+=p.size[1]
o.save('crops/cmp_mpwjoh.png'); print(o.size)
