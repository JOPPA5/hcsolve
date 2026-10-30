import sys,os
from PIL import Image, ImageOps
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(D+'/hires/cpc_--26_HU__HU_Jasz-Arokszalas_jolanka-91_adr.jpg').convert('RGB')
name,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.BICUBIC)
c.save(D+'/crops/%s.png'%name)
