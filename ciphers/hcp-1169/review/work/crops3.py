from PIL import Image
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1024
def c(n,x0,y0,x1,y1,z=4):
    k=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    k.resize((k.width*z,k.height*z),Image.LANCZOS).save('crops/'+n+'.jpg',quality=92)
c('end1',310,385,505,425,2+1)
c('end2',380,415,505,475,3)
c('megf',170,575,400,625,3)
c('year',385,590,560,630,3)
c('stamp',710,5,860,140,3)
c('uj',400,50,500,85,4)
c('borsod',540,570,830,625,3)
c('szomolya',640,520,980,590,2)
pic=Image.open(glob.glob('../../work/hires/*pic.jpg')[0]).convert('RGB'); pic.thumbnail((1200,1200)); pic.save('crops/pic.jpg')
