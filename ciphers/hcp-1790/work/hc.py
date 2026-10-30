# high-contrast grey zoom with x ruler: hc.py x0 x1 yc out [scale] [halfheight]
import sys
from PIL import Image, ImageOps, ImageDraw
x0,x1,yc=map(int,sys.argv[1:4]); out=sys.argv[4]
s=int(sys.argv[5]) if len(sys.argv)>5 else 8; h=int(sys.argv[6]) if len(sys.argv)>6 else 28
d=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/flip_color.png').convert('L')
c=ImageOps.autocontrast(d.crop((x0,yc-h,x1,yc+h)),cutoff=1).resize(((x1-x0)*s,2*h*s),Image.LANCZOS).convert('RGB')
W,H=c.size; cv=Image.new('RGB',(W,H+26),'white'); cv.paste(c,(0,0)); dr=ImageDraw.Draw(cv)
for t in range((x0//10+1)*10,x1,10):
    X=(t-x0)*s; dr.line([(X,H),(X,H+(14 if t%50==0 else 6))],fill='red',width=2)
    if t%50==0: dr.text((X+3,H+12),str(t),fill='red')
cv.save(out)
