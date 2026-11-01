from PIL import Image, ImageOps, ImageChops
s=Image.open('crops/shear.png')
def c(n,box,sc=4):
    x=s.crop(box); x=x.resize((int(x.width*sc),int(x.height*sc)),Image.LANCZOS); ImageOps.autocontrast(x,cutoff=0.5).save('crops/'+n)
c('z17.png',(85,1270,420,1390),5)
c('z1.png',(780,50,1640,130),2.3)
c('z13.png',(90,1000,900,1090),2.4)
c('z13b.png',(860,1000,1640,1090),2.5)
c('z10b.png',(90,770,1640,850),1.3)
