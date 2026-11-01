import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1260/work/hires/cpc_--25_HU__HU_Jasz-Arokszalas_jolanka-90_adr.jpg')
print(im.size)
o=im.copy(); o.thumbnail((1700,1100)); o.save('crops/full.png')
W,H=im.size
for i in range(6):
    y0=int(H*i/6)-40; y1=int(H*(i+1)/6)+40
    r=im.crop((0,max(0,y0),int(W*0.58),min(H,y1))); r.save(f'crops/band{i}.png')
