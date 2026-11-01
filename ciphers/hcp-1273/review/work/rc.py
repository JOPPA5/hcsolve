"""Reviewer crop helper: rc.py x0 y0 x1 y1 scale name"""
import sys
from PIL import Image, ImageEnhance
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1273/work/hires/cpc_1912-05-04_HU__HU_Jasz-Arokszalas_jolanka-18_adr.jpg').convert('RGB')
if len(sys.argv)<3: print(im.size); sys.exit()
x0,y0,x1,y1=map(int,sys.argv[1:5]); s=float(sys.argv[5])
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
ImageEnhance.Contrast(c).enhance(1.3).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1273/review/work/crops/'+sys.argv[6]+'.png')
