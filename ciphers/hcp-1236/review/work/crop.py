from PIL import Image
import sys
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1236/work/hires/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_adr.jpg').convert('RGB')
# usage: crop.py name x0 y0 x1 y1 [scale] [rot]
n,*v=sys.argv[1:]
x0,y0,x1,y1=map(int,v[:4]); s=float(v[4]) if len(v)>4 else 1; r=float(v[5]) if len(v)>5 else 0
c=im.crop((x0,y0,x1,y1))
if r: c=c.rotate(r,resample=Image.BICUBIC,fillcolor=(255,255,255))
if s!=1: c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1236/review/work/'+n+'.png')
