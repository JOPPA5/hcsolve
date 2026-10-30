# high-contrast windows along a line: hcwin.py line yc xs xe
import sys
from PIL import Image, ImageOps, ImageDraw
d=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/flip_color.png').convert('L')
ln,yc,xs,xe=map(int,sys.argv[1:5]); s=6; h=36
x=xs; i=0
while x<xe:
    x1=min(x+200,xe)
    c=ImageOps.autocontrast(d.crop((x,yc-h,x1,yc+h)),cutoff=1).resize(((x1-x)*s,2*h*s),Image.LANCZOS).convert('RGB')
    W,H=c.size; cv=Image.new('RGB',(W,H+26),'white'); cv.paste(c,(0,0)); dr=ImageDraw.Draw(cv)
    for t in range((x//10+1)*10,x1,10):
        X=(t-x)*s; dr.line([(X,H),(X,H+(14 if t%50==0 else 6))],fill='red',width=2)
        if t%50==0: dr.text((X+3,H+12),str(t),fill='red')
    cv.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/crops/H{ln:02d}_{i}.png')
    x+=180; i+=1
print(ln,i)
