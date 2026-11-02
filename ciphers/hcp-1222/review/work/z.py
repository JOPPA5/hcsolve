from PIL import Image, ImageOps
import sys
im=Image.open('work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-113_adr.jpg').convert('RGB')
name,l,t,r,b,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(l),int(t),int(r),int(b)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(f'review/work/{name}.png')
# red channel separates grey-blue postmark ink less; also save channel-diff: brown script vs blue-grey stamp
R,G,B=c.split()
from PIL import ImageChops
d=ImageChops.subtract(B,R,scale=1,offset=128)
d=ImageOps.autocontrast(d)
d.save(f'review/work/{name}_br.png')
