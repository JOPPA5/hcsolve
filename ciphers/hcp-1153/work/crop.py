#!/usr/bin/env python3
"""crop.py x0 y0 x1 y1 scale name : enlarged, contrast-stretched crop of hires address side."""
import sys
from PIL import Image,ImageOps
f='work/hires/cpc_1916-06-09_HU_Mezokovesd_HU_Szomolya_szomolya-38_adr.jpg'
x0,y0,x1,y1=map(int,sys.argv[1:5]);s=float(sys.argv[5]);n=sys.argv[6]
im=Image.open(f).convert('RGB').crop((x0,y0,x1,y1))
im=ImageOps.autocontrast(im,cutoff=1).resize((int((x1-x0)*s),int((y1-y0)*s)),Image.LANCZOS)
im.save('work/crops/'+n+'.png')
