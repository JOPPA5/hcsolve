import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1263/work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-109_adr.jpg')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1263/work/crops/'
# rows: 4 per image, left/right halves
y0=100; n=0
step=390
for i in range(5):
    t=y0+i*step; b=t+step+60
    for side,(l,r) in {'L':(80,860),'R':(800,1640)}.items():
        c=im.crop((l,t,r,b)); c=c.resize((c.width*5//2,c.height*5//2),Image.LANCZOS)
        c.save(f'{out}b{i}{side}.png')
c=im.crop((2580,240,3080,780)); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(out+'stamp.png')
