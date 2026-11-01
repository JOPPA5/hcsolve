"""Crops for response to review 1. Run: python -I crop7.py name,x0,y0,x1,y1,scale ..."""
from PIL import Image
import sys, os
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(D+'/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_adr.jpg').convert('RGB')
for a in sys.argv[1:]:
    n,*v=a.split(','); x0,y0,x1,y1=map(int,v[:4]); s=float(v[4])
    c=im.crop((x0,y0,x1,y1)); c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(D+'/crops2/'+n+'.png')
