from PIL import Image, ImageFilter, ImageOps, ImageChops
im=Image.open('work/hires/pc_hcp_63_adr.JPG').convert('L')
# hires 1785x1175; writing area left half
W,H=im.size
s=W/1024
box=(int(50*s),int(170*s),int(475*s),int(630*s))
c=im.crop(box).rotate(90,expand=True)
bg=c.filter(ImageFilter.MaxFilter(11))
import numpy as np
a=np.asarray(c,float)/np.maximum(np.asarray(bg,float),1)
a=np.clip((a-0.7)/0.3,0,1)*255
n=Image.fromarray(a.astype('uint8'))
c.save('review/work/raw.png');n.save('review/work/norm.png');print(n.size)
n.resize((n.width*2,n.height*2),Image.LANCZOS).save('review/work/norm2.png')
