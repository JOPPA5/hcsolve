from PIL import Image, ImageOps
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
def c(n,b,s=3):
    x=ImageOps.autocontrast(im.crop(b),cutoff=1); x.resize((x.width*s,x.height*s),Image.LANCZOS).save('crops/'+n+'.png')
c('r7',(560,730,1010,920),3)
c('r6',(600,620,1000,760),3)
