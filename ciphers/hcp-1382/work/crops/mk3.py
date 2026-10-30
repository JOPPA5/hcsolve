from PIL import Image,ImageOps,ImageFilter
import numpy as np
r=Image.open('crops/rot.png').convert('L')
a=np.asarray(r,float)
bg=np.asarray(r.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(2)),float)
n=np.clip(a/bg,0,1)
n=np.clip((n-0.55)/0.42,0,1)**1.3
o=Image.fromarray((n*255).astype('uint8')); o.save('crops/norm.png')
def c(name,box,s=3):
    x=o.crop(box); x=x.resize((x.width*s,x.height*s),Image.BICUBIC); x.save('crops/'+name+'.jpg',quality=93)
c('n_all',(0,0,800,740),2)
c('n4a',(0,230,420,400)); c('n4b',(380,180,800,350)); c('n5',(60,300,520,480)); c('n5b',(380,320,800,480))
