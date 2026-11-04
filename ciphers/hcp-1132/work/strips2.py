# Render columns (polylines from cols21.py) as horizontal strips: column top -> left, column's left side -> bottom.
# usage: strips2.py out.png halfwidth k k k ...
import sys
sys.path.insert(0,'work')
from cols21 import xat
from PIL import Image, ImageDraw
import numpy as np
im=np.asarray(Image.open('work/hires/cpc_--_HU_Debrecen_HU___adr.jpg').convert('RGB'))
out=sys.argv[1]; HW=int(sys.argv[2]); ks=[int(k) for k in sys.argv[3:]]
halves=[(40,1100),(1080,2140)]
rows=[]
for k in ks:
    for (a,b) in halves:
        strip=np.zeros((2*HW,b-a,3),np.uint8)
        for y in range(a,b):
            cx=int(round(xat(k,y)))
            strip[:,y-a]=im[y,cx-HW:cx+HW][::-1]
        lab=Image.new('RGB',(b-a,14),(255,255,255)); d=ImageDraw.Draw(lab)
        for y in range((a//50+1)*50,b,50):
            d.line([(y-a,9),(y-a,14)],fill=(255,0,0))
            if y%100==0: d.text((y-a+2,0),str(y),fill=(0,0,255))
        d.text((2,0),f"C{k}",fill=(255,0,0))
        rows+=[lab,Image.fromarray(strip)]
W=max(r.width for r in rows); H=sum(r.height for r in rows)
can=Image.new('RGB',(W,H),(255,255,255)); y=0
for r in rows: can.paste(r,(0,y)); y+=r.height
can.save(out)
