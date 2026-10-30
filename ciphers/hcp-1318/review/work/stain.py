from PIL import Image, ImageOps
im=Image.open('work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-111_adr.jpg').convert('RGB').crop((480,620,920,1010))
r,g,b=im.split()
for n,c in (('r',r),('g',g),('b',b)):
    c=ImageOps.autocontrast(c,cutoff=1).resize((1320,1170),Image.LANCZOS); c.save(f'review/work/crops/stain_{n}.png')
# local contrast on the stain: subtract blurred
from PIL import ImageFilter, ImageChops
g2=g.filter(ImageFilter.GaussianBlur(25)); d=ImageChops.subtract(g2,g,0.25,128)
ImageOps.autocontrast(d,cutoff=0.5).resize((1320,1170),Image.LANCZOS).save('review/work/crops/stain_hp.png')
