from PIL import Image, ImageOps
import glob,sys
im=Image.open(glob.glob('work/hires/*_adr.jpg')[0]).convert('RGB')
def c(n,b,s=2):
    x=im.crop(b); x=x.resize((x.width*s,x.height*s),Image.LANCZOS); ImageOps.autocontrast(x,cutoff=0.5).save(f'work/crops/{n}.png')
c('a0',(30,1800,800,2120))
c('a1',(740,1800,1540,2120))
c('a2',(1480,1900,2300,2120))
c('a3',(2250,1900,3300,2120),2)
c('b0',(30,1980,1000,2110),2)
