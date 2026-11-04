# Render columns as horizontal strips (column top -> left), right-most column first.
# usage: strips.py out.png col col ...   (each column split into two halves)
import sys
from PIL import Image, ImageDraw
import numpy as np
CEN=[92,166,227,287,358,430,499,579,648,721,793,872,947,1021,1092,1171,1252,1328,1405,1475]
SL=0.008; HW=37
im=np.asarray(Image.open('work/hires/cpc_--_HU_Debrecen_HU___adr.jpg').convert('RGB'))
out=sys.argv[1]; cols=[int(c) for c in sys.argv[2:]]
halves=[(40,1100),(1080,2140)]
rows=[]
for c in cols:
    for (a,b) in halves:
        strip=np.zeros((2*HW,b-a,3),np.uint8)
        for y in range(a,b):
            cx=int(round(CEN[c]+SL*(y-1100)))
            strip[:,y-a]=im[y,cx-HW:cx+HW][::-1]   # rotate CCW: column top -> left; left of column -> bottom
        img=Image.fromarray(strip)
        lab=Image.new('RGB',(b-a,16),(255,255,255)); d=ImageDraw.Draw(lab)
        d.text((2,2),f"col {c}  y{a}-{b}",fill=(255,0,0))
        for y in range((a//50+1)*50,b,50):
            d.line([(y-a,10),(y-a,16)],fill=(255,0,0)); 
            if y%100==0: d.text((y-a+2,2),str(y),fill=(0,0,255))
        rows+= [lab,img]
W=max(r.width for r in rows); H=sum(r.height for r in rows)
can=Image.new('RGB',(W,H),(255,255,255)); y=0
for r in rows: can.paste(r,(0,y)); y+=r.height
can.save(out)
