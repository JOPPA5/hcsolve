"""Usage: crop.py name x0 y0 x1 y1 scale  -- crop of the hires address side into work/crops/"""
import sys,os
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(D+'/hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-60_adr.jpg')
a=sys.argv
b=tuple(map(int,a[2:6])); s=float(a[6])
x=im.crop(b); x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS); x.save(D+'/crops/'+a[1]+'.png')
