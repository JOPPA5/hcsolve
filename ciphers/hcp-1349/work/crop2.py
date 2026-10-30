from PIL import Image,ImageOps
import numpy as np
m=Image.open('work/hires/pc_hcp_30_adr.JPG').convert('RGB').crop((110,420,920,1120)).rotate(90,expand=True)
a=np.asarray(m).astype(float)
# ink keeps blue lower than red; grey watermark is neutral: use blue channel + saturation view
print(a.shape)
def out(name,box,s=5):
    c=m.crop(box); c=ImageOps.autocontrast(c,cutoff=0.5)
    c.resize((c.width*s,c.height*s),Image.BICUBIC).save(f'work/crops/{name}.jpg',quality=90)
out('w_oppos',(10,285,470,410),3)
out('w_park',(20,380,340,480),4)
out('w_place',(280,390,640,480),4)
out('w_stock',(370,550,660,650),4)
out('w_NL',(20,590,300,700),4)
