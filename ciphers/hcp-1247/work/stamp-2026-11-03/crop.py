import sys
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]).convert('RGB')
out=sys.argv[2]
def c(n,box,sc,rot=0):
    x=im.crop(box)
    if rot: x=x.rotate(rot,expand=True,fillcolor=(255,255,255))
    x=x.resize((int(x.width*sc),int(x.height*sc)),Image.LANCZOS)
    ImageOps.autocontrast(x,cutoff=1).save(out+'/'+n)
c('overview.jpg',(2600,0,3445,900),1)
c('b4.png',(2750,420,3250,640),3.5)
