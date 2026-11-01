from PIL import Image
import sys
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1256/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_adr.jpg').convert('RGB')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1256/review/work/'
# name x0 y0 x1 y1 scale
for a in sys.argv[1:]:
    n,x0,y0,x1,y1,s=a.split(',')
    x0,y0,x1,y1=map(int,(x0,y0,x1,y1)); s=float(s)
    c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save(out+n+'.png')
