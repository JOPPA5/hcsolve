from PIL import Image, ImageFilter
import numpy as np
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/'
im=Image.open(W+'hires/cpc_1912-04-07_HU__HU_Jasz-Arokszalas_jolanka-15_adr.jpg').convert('RGB')
a=np.asarray(im).astype(float)
box=(60,350,1200,1050)
out=[]
for nm,ch in [('r',a[:,:,0]),('g',a[:,:,1]),('b',a[:,:,2]),('r-g',a[:,:,0]-a[:,:,1]),('b-g',a[:,:,2]-a[:,:,1]),('r-b',a[:,:,0]-a[:,:,2])]:
    c=ch[box[1]:box[3],box[0]:box[2]]
    bl=np.asarray(Image.fromarray(np.clip(c-c.min(),0,255).astype('uint8')).filter(ImageFilter.GaussianBlur(35))).astype(float)+c.min()
    s=(c-bl); s=np.clip(128+s/(s.std()*3)*128,0,255).astype('uint8')
    Image.fromarray(s).save(W+f'crops/ch_{nm}.png'); print(nm,c.mean(),c.std())
