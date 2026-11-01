import sys
from PIL import Image, ImageEnhance
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1258/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-70_adr.jpg'
im=Image.open(src).convert('RGB')
x0,y0,x1,y1,s,name=[*map(float,sys.argv[1:6]),sys.argv[6]]
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageEnhance.Contrast(c).enhance(1.6)
c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1258/work/crops/'+name+'.png')
