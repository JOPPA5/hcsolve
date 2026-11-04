import sys
from PIL import Image, ImageOps
f,out=sys.argv[1],sys.argv[2]
im=Image.open(f).convert('RGB')
def c(n,b,s):
    r=im.crop(b).resize((int((b[2]-b[0])*s),int((b[3]-b[1])*s)),Image.LANCZOS)
    ImageOps.autocontrast(r.split()[0],cutoff=1).save(out+'/'+n+'.png')
c('row1_6x',(2840,270,3060,340),6)
c('row4_6x',(2810,450,3020,520),6)
c('row5_6x',(2810,520,3150,600),5)
