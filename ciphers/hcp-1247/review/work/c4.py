from PIL import Image, ImageOps
s=Image.open('c/shear.png')
def c(n,box,sc):
    x=s.crop(box); x=ImageOps.autocontrast(x,cutoff=1).resize((int(x.width*sc),int(x.height*sc)),Image.LANCZOS); x.save('c/'+n,quality=92)
# band05 y=1300 .. band coordinates: row19 y~1300+190
c('z19a.jpg',(90,1440,720,1560),2.4)
c('z19b.jpg',(700,1440,1660,1560),1.65)
c('z20e.jpg',(1300,1520,1720,1640),3.5)
c('z17s.jpg',(90,1270,500,1390),3.5)
c('z8.jpg',(90,600,560,720),3.2)
c('z1e.jpg',(1100,50,1620,190),2.9)
