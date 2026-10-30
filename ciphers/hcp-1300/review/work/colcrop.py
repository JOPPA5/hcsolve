# colour crop (pencil vs printed seal ink): name x0 y0 x1 y1 scale
import sys,os
from PIL import Image, ImageEnhance
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(D+'/../../work/hires/cpc_--26_HU__HU_Jasz-Arokszalas_jolanka-91_adr.jpg').convert('RGB')
n=sys.argv[1];x0,y0,x1,y1=map(int,sys.argv[2:6]);s=float(sys.argv[6])
c=ImageEnhance.Contrast(im.crop((x0,y0,x1,y1))).enhance(1.8)
c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(D+'/crops/%s.png'%n)
