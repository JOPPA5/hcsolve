# Two halves of a text line, high contrast, 3.5x, with ruler. half.py line yc [x0]
import sys
from PIL import Image, ImageOps, ImageDraw
d=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/flip_color.png').convert('L')
ln,yc=map(int,sys.argv[1:3]); x0=int(sys.argv[3]) if len(sys.argv)>3 else 190
s=3.5; h=36
for i,(a,b) in enumerate([(x0,x0+(1100-x0)//2+20),(x0+(1100-x0)//2-20,1100)]):
    c=ImageOps.autocontrast(d.crop((a,yc-h,b,yc+h)),cutoff=1)
    c=c.resize((int((b-a)*s),int(2*h*s)),Image.LANCZOS).convert('RGB')
    W,H=c.size; cv=Image.new('RGB',(W,H+24),'white'); cv.paste(c,(0,0)); dr=ImageDraw.Draw(cv)
    for t in range((a//10+1)*10,b,10):
        X=int((t-a)*s); dr.line([(X,H),(X,H+(12 if t%50==0 else 5))],fill='red',width=2)
        if t%50==0: dr.text((X+3,H+10),str(t),fill='red')
    cv.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/crops/Q{ln:02d}{"ab"[i]}.png')
