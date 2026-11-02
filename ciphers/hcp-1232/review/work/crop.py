"""Reviewer crop tool: crop.py NAME x0 y0 x1 y1 Z  (coords = hires pixels, address side)"""
from PIL import Image
import sys,os
d=os.path.dirname(os.path.abspath(__file__))
im=Image.open(d+'/../../work/hires/cpc_--24_HU__HU_Jasz-Arokszalas_jolanka-89_adr.jpg').convert('RGB')
a=sys.argv[1:]
c=im.crop(tuple(int(x) for x in a[1:5]));z=int(a[5]);c=c.resize((c.width*z,c.height*z),Image.LANCZOS);c.save(d+'/crops/'+a[0]+'.png')
