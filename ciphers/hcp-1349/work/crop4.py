from PIL import Image,ImageOps
import numpy as np
m=Image.open('work/hires/pc_hcp_30_adr.JPG').convert('RGB').crop((110,420,920,1120)).rotate(90,expand=True)
def out(name,box,s=6):
    c=ImageOps.autocontrast(m.crop(box),cutoff=0.5)
    c.resize((c.width*s,c.height*s),Image.BICUBIC).save(f'work/crops/{name}.jpg',quality=90)
out('z_Q',(15,330,145,470),7)
# watermark-suppressed: ink is warm or very dark; grey watermark is cool neutral
a=np.asarray(m.crop((10,290,350,490))).astype(float)
warm=a[...,0]-a[...,2]
L=a.mean(2)
paperdiff=np.clip((warm-8)*6,0,255)  # brown ink
dark=np.clip((150-L)*4,0,255)
o=255-np.maximum(paperdiff,dark)
Image.fromarray(o.astype('uint8')).resize((340*4,200*4),Image.BICUBIC).save('work/crops/z_Qink.jpg',quality=90)
