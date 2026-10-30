import sys
from PIL import Image, ImageDraw
d=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/flip_color.png')
def ruler(x0,x1,yc,out,s=4,h=38):
    c=d.crop((x0,yc-h,x1,yc+h)).resize(((x1-x0)*s,2*h*s),Image.LANCZOS)
    W,H=c.size
    cv=Image.new('RGB',(W,H+30),'white'); cv.paste(c,(0,0)); dr=ImageDraw.Draw(cv)
    for x in range((x0//10+1)*10,x1,10):
        X=(x-x0)*s; dr.line([(X,H),(X,H+(14 if x%50==0 else 6))],fill='red',width=2)
        if x%50==0: dr.text((X+3,H+12),str(x),fill='red')
    cv.save(out)
ys={1:1020,2:1080,3:1135,4:1190,5:1250,6:1305,7:1362,8:1416,9:1470,10:1524,11:1568,12:1618,13:1660,14:1715}
for ln in map(int,sys.argv[1:]):
    for x0 in (40,300,560,820):
        ruler(x0,x0+290,ys[ln],f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/crops/R{ln:02d}_{x0}.png')
