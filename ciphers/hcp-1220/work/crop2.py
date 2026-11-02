from PIL import Image, ImageOps, ImageEnhance
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
def c(n,b,s=5,col=False):
    x=im.crop(b)
    if col:
        r,g,bl=x.split(); x=ImageOps.autocontrast(g,cutoff=1)  # purple ink vs blue stamp: green channel keeps purple dark and blue mid
    else: x=ImageOps.autocontrast(x,cutoff=1)
    x.resize((x.width*s,x.height*s),Image.LANCZOS).save('crops/'+n+'.png')
c('r7mid',(690,800,1000,960),4)
c('st_bot',(2660,560,3150,740),3)
c('st_mid',(2680,310,3150,600),3,True)
c('st_top',(2660,170,3160,360),3,True)
c('top',(1400,40,2800,330),1)
c('pm',(1800,120,2500,820),2)
c('pm2',(2440,380,3200,1060),2)
c('r5end',(640,540,1400,700),2)
