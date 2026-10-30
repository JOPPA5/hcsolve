import sys
from PIL import Image, ImageEnhance
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1306/work/hires/cpc_1914-03-05_HU__HU_Jasz-Arokszalas_jolanka-49_adr.jpg').convert('RGB')
x0,y0,x1,y1,s,name=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5]),sys.argv[6]
c=im.crop((x0,y0,x1,y1)).rotate(-90,expand=True); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
ImageEnhance.Contrast(c).enhance(1.6).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1306/work/crops/'+name+'.png')
