import json,sys
from PIL import Image, ImageDraw
T=json.load(open(sys.argv[1])); x0,y0,x1,y1=map(int,sys.argv[2:6]); sc=float(sys.argv[6]); out=sys.argv[7]
im=Image.open('work/hires/cpc_--_HU_Debrecen_HU___adr.jpg').convert('RGB').crop((x0,y0,x1,y1))
im=im.resize((int((x1-x0)*sc),int((y1-y0)*sc))); d=ImageDraw.Draw(im)
cols=[(255,0,0),(0,160,0),(0,0,255),(200,0,200),(0,150,150),(220,120,0)]
for i,t in enumerate(T):
    c=cols[i%len(cols)]
    pts=[((o['x']-x0)*sc,(o['y']-y0)*sc) for o in t]
    d.line(pts,fill=c,width=1)
    for o in t:
        d.rectangle([((o['x0']-x0)*sc-1,(o['y0']-y0)*sc-1),((o['x1']-x0)*sc+1,(o['y1']-y0)*sc+1)],outline=c)
    d.text(pts[0],str(i),fill=c)
im.save(out)
