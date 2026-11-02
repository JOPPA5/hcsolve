import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1275/work/hires/cpc_1913-08-13_HU__HU_Jasz-Arokszalas_jolanka-40_adr.jpg').convert('RGB')
print(im.size)
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
mode=sys.argv[7] if len(sys.argv)>7 else 'rgb'
r=im.crop((x0,y0,x1,y1))
if mode in('r','g','b'):
    r=ImageOps.autocontrast(r.split()['rgb'.index(mode)],cutoff=1)
r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
r.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1275/work/rev2/'+n+'.png')
