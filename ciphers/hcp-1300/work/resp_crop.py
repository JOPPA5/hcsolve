"""Colour crop for the review response: name x0 y0 x1 y1 scale. Writes work/crops2/<name>.png"""
import sys,os
from PIL import Image, ImageEnhance
W=os.path.dirname(os.path.abspath(__file__))
im=Image.open(W+'/hires/cpc_--26_HU__HU_Jasz-Arokszalas_jolanka-91_adr.jpg').convert('RGB')
n=sys.argv[1];x0,y0,x1,y1=map(int,sys.argv[2:6]);s=float(sys.argv[6])
c=ImageEnhance.Contrast(im.crop((x0,y0,x1,y1))).enhance(1.6)
c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(W+'/crops2/%s.png'%n)
