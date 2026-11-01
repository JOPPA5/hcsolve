from PIL import Image, ImageOps
s=Image.open('crops/shear.png')
def c(n,box,sc):
    x=s.crop(box); x=x.resize((int(x.width*sc),int(x.height*sc)),Image.LANCZOS); ImageOps.autocontrast(x,cutoff=0.5).save('crops/'+n)
c('z5.png',(1200,370,1640,450),4)
c('z22.png',(1300,1700,1760,1790),4)
c('z19.png',(1000,1540,1640,1620),3)
