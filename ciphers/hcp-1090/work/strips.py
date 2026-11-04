# Render each column (along its fitted line) as a horizontal strip, top of column at left.
import json,sys
from PIL import Image, ImageDraw
im=Image.open(sys.argv[1]).convert('L')
lines=json.load(open(sys.argv[2]))
HW=50
for half,(y0,y1) in enumerate(((0,1150),(1080,2240))):
  for grp in range(0,15,5):
    out=Image.new('L',((y1-y0)+60,(2*HW+12)*5),255)
    d=ImageDraw.Draw(out)
    for j,ci in enumerate(range(grp,min(grp+5,15))):
        a,k=lines[ci]
        for y in range(y0,y1):
            xc=int(round(a+k*y))
            for dx in range(-HW,HW):
                x=xc+dx
                if 0<=x<im.width and y<im.height:
                    out.putpixel((y-y0+60,j*(2*HW+12)+dx+HW),im.getpixel((x,y)))
        d.text((5,j*(2*HW+12)+HW-5),str(ci+1),fill=0)
        # tick marks every 100px
        for t in range(0,y1-y0,100):
            d.line([(t+60,j*(2*HW+12)+2*HW+2),(t+60,j*(2*HW+12)+2*HW+8)],fill=0)
    # rotate so that column's left side (dx<0) is at top? we mapped dx-> vertical; image x = y (top->left)
    out.save('work/crops/strip_h%d_g%d.png'%(half,grp//5))
