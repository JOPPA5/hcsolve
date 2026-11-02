from PIL import Image, ImageOps
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
def c(n,b,s=4,ch=None):
    x=im.crop(b)
    if ch is not None: x=x.split()[ch]
    x=ImageOps.autocontrast(x,cutoff=1)
    x.resize((x.width*s,x.height*s),Image.LANCZOS).save('crops/'+n+'.png')
c('l4r',(2680,460,3130,640),3,0)   # red channel: blue stamp dark, purple? 
c('l4g',(2680,460,3130,640),3,1)
c('last',(2720,590,3150,700),4)
c('last_r',(2720,590,3150,700),4,1)
c('l1',(2680,190,3150,330),3)
c('l3',(2680,370,3130,500),3,1)
