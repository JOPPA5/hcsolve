# 6x windows (170 px wide, 20 px overlap) along one text line of the flipped/deskewed colour scan, with x-ruler.
import sys
from PIL import Image, ImageDraw
d=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/flip_color.png')
ln=int(sys.argv[1]); yc=int(sys.argv[2]); xs=int(sys.argv[3]); xe=int(sys.argv[4])
s=6; h=34
x=xs; i=0
while x<xe:
    x1=min(x+170,xe)
    c=d.crop((x,yc-h,x1,yc+h)).resize(((x1-x)*s,2*h*s),Image.LANCZOS)
    W,H=c.size; cv=Image.new('RGB',(W,H+26),'white'); cv.paste(c,(0,0)); dr=ImageDraw.Draw(cv)
    for t in range((x//10+1)*10,x1,10):
        X=(t-x)*s; dr.line([(X,H),(X,H+(14 if t%50==0 else 6))],fill='red',width=2)
        if t%50==0: dr.text((X+3,H+12),str(t),fill='red')
    cv.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/crops/W{ln:02d}_{i}.png')
    x+=150; i+=1
print(i)
