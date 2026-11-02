from PIL import Image, ImageFilter
import numpy as np
im=Image.open('work/hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
box=(3040,190,3240,470)
a=np.asarray(im.crop(box)).astype('float32')
out=[]
for name,c in (('g',a[...,1]),('b',a[...,2]),('sat',(a[...,0]-a[...,1]))):
    if name=='sat': c=-c
    u=Image.fromarray(np.clip((c-c.min())/(c.max()-c.min())*255,0,255).astype('uint8'))
    bg=np.asarray(u.filter(ImageFilter.GaussianBlur(22))).astype('float32')
    d=np.asarray(u.filter(ImageFilter.GaussianBlur(1.2))).astype('float32')-bg
    l,h=np.percentile(d,1),np.percentile(d,99.5)
    out.append(Image.fromarray((np.clip((d-l)/(h-l),0,1)**1.3*255).astype('uint8')).resize((a.shape[1]*4,a.shape[0]*4),Image.BICUBIC))
M=Image.new('L',(sum(o.width for o in out)+20,out[0].height),255)
x=0
for o in out: M.paste(o,(x,0)); x+=o.width+10
M.save('work/crops2/blot.png')
