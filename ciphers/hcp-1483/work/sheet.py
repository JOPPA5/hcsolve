# sheet.py out S label:y0:y1:x0:x1 ... -> grid of enlarged crops with labels
import sys
from PIL import Image, ImageOps, ImageDraw
out=sys.argv[1]; S=int(sys.argv[2]); items=[a.split(':') for a in sys.argv[3:]]
im=Image.open('work/upright.jpg').convert('L')
crops=[]
for lab,y0,y1,x0,x1 in items:
    y0,y1,x0,x1=map(int,(y0,y1,x0,x1))
    c=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=1).resize(((x1-x0)*S,(y1-y0)*S),Image.LANCZOS)
    crops.append((lab,c))
W=max(c.width for _,c in crops); per=max(1,1100//(W+10))
rows=(len(crops)+per-1)//per; H=max(c.height for _,c in crops)+18
sh=Image.new('L',(per*(W+10),rows*H),255); d=ImageDraw.Draw(sh)
for k,(lab,c) in enumerate(crops):
    r,q=divmod(k,per); sh.paste(c,(q*(W+10),r*H+16)); d.text((q*(W+10)+2,r*H+2),lab,fill=0)
sh.save(out)
