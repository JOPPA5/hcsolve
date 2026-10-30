from PIL import Image,ImageOps,ImageFilter
import numpy as np
B='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1381/'
im=Image.open(B+'work/hires/pc_hcp_62_adr.JPG').convert('RGB')
c=im.crop((70,120,1000,1110)).rotate(90,expand=True)
a=np.asarray(c).astype(float)
# paper is tan, overlay/pencil neutral: overlay is flat grey; divide out with large median of grey plateau
g=a[:,:,1]
from PIL import Image as I
bg=np.asarray(I.fromarray(g.astype('uint8')).filter(ImageFilter.MedianFilter(13))).astype(float)
n=np.clip(g/bg,0.6,1.02); n=(n-0.6)/0.42*255
o=I.fromarray(n.astype('uint8'))
o.crop((640,230,960,350)).resize((1280,480),I.BICUBIC).save(B+'review/work/w2.png')
o.crop((600,410,880,540)).resize((1120,520),I.BICUBIC).save(B+'review/work/w4.png')
im.crop((0,0,1785,1175)).resize((892,587)).save(B+'review/work/adr_small.png')
Image.open(B+'work/hires/pc_hcp_62_pic.JPG').convert('RGB').resize((800,530)).save(B+'review/work/pic_small.png')
