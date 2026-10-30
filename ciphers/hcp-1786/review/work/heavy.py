# Heavy-stroke map: erode dark ink with a 7x7 max filter; only strokes wider than ~7 hires px survive (red).
from PIL import Image, ImageFilter
import numpy as np
s=1785/1024
A=Image.open('work/hires/pc_hcp_467_adr.JPG').convert('RGB')
b=[int(v*s) for v in (60,140,505,570)]
c=A.crop(b); g=c.convert('L')
er=np.array(g.filter(ImageFilter.MaxFilter(7)))
keep=er<125
keep=np.array(Image.fromarray((keep*255).astype('uint8')).filter(ImageFilter.MaxFilter(5)))>0
a=np.array(c); a[keep]=[225,20,20]
Image.fromarray(a).resize((c.width*2,c.height*2)).save('review/work/heavy_map.png')
r=A.crop([int(v*s) for v in (310,175,360,225)]); r.resize((r.width*10,r.height*10),Image.BICUBIC).save('review/work/z_nesmis2.png')
