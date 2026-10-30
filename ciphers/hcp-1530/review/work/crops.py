import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).transpose(Image.ROTATE_90)
im.save(out+'/upright.png')
top = im.crop((28,35,642,195)).rotate(180)
top.save(out+'/top.png')
def c(img,box,name,s=4):
    r=img.crop(box); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save(out+'/'+name)
c(top,(0,0,614,40),'T01x3.png',3)
c(top,(300,0,614,40),'U1x5.png',5)
c(im,(400,770,674,822),'U2x5.png',5)
c(im,(300,915,470,958),'U4x5.png',5)
c(im,(280,950,500,992),'U3x5.png',5)
c(im,(0,660,674,1000),'bottom.png',2)
c(top,(0,0,614,160),'topx2.png',2)
