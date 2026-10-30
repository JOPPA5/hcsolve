import sys
from PIL import Image, ImageOps, ImageEnhance
im=Image.open('work/hires/cpc_1913-08-31_HU__HU_Jasz-Arokszalas_jolanka-41_adr.jpg').convert('RGB')
n=sys.argv[1]; b=[int(float(v)*1.72) for v in sys.argv[2:6]]; z=int(sys.argv[6]) if len(sys.argv)>6 else 4
c=im.crop(b); c=c.resize((c.width*z,c.height*z),Image.BICUBIC)
c=ImageOps.autocontrast(c,cutoff=0.5); c.save('work/bands/'+n+'.png')
