# Crop of flipped colour image with an x-ruler (source pixel coords) for glyph-by-glyph reading.
import sys
from PIL import Image, ImageDraw
x0,x1,yc=map(int,sys.argv[1:4]); out=sys.argv[4]; s=4; h=38
d=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/flip_color.png')
c=d.crop((x0,yc-h,x1,yc+h)).resize(((x1-x0)*s,2*h*s),Image.LANCZOS)
W,H=c.size
canvas=Image.new('RGB',(W,H+30),'white'); canvas.paste(c,(0,0))
dr=ImageDraw.Draw(canvas)
for x in range((x0//10+1)*10,x1,10):
    X=(x-x0)*s
    dr.line([(X,H),(X,H+(14 if x%50==0 else 6))],fill='red',width=2)
    if x%50==0: dr.text((X+3,H+12),str(x),fill='red')
canvas.save(out)
