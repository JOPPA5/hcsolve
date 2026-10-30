# Per text line: stacked enlarged segments (5x) with x-ruler in source (flipped, deskewed) pixel coords.
import sys
from PIL import Image, ImageDraw
d=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/flip_color.png')
ys={1:1020,2:1080,3:1135,4:1190,5:1250,6:1305,7:1362,8:1416,9:1470,10:1524,11:1568,12:1618,13:1660,14:1715}
s=5; h=36
def seg(x0,x1,yc):
    c=d.crop((x0,yc-h,x1,yc+h)).resize(((x1-x0)*s,2*h*s),Image.LANCZOS)
    W,H=c.size; cv=Image.new('RGB',(W,H+26),'white'); cv.paste(c,(0,0)); dr=ImageDraw.Draw(cv)
    for x in range((x0//10+1)*10,x1,10):
        X=(x-x0)*s; dr.line([(X,H),(X,H+(14 if x%50==0 else 6))],fill='red',width=2)
        if x%50==0: dr.text((X+3,H+12),str(x),fill='red')
    return cv
for ln in map(int,sys.argv[1:]):
    for part,ranges in (('a',[(170,400),(390,620)]),('b',[(610,840),(830,1060)])):
        ims=[seg(a,b,ys[ln]) for a,b in ranges]
        W=max(i.size[0] for i in ims); H=sum(i.size[1] for i in ims)
        out=Image.new('RGB',(W,H),'white'); y=0
        for i in ims: out.paste(i,(0,y)); y+=i.size[1]
        out.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/crops/S{ln:02d}{part}.png')
