import sys
from PIL import Image, ImageOps
src='ciphers/hcp-1295/work/hires/cpc_1912-06-06_HU__HU_Jasz-Arokszalas_jolanka-24_adr.jpg'
im=Image.open(src).convert('RGB')
for spec in sys.argv[1:]:
    n,x0,y0,x1,y1,s=spec.split(','); x0,y0,x1,y1,s=map(int,(x0,y0,x1,y1,s))
    c=im.crop((x0,y0,x1,y1)); g=c.split()[1]; g=ImageOps.autocontrast(g,cutoff=1)
    W=Image.new('RGB',(c.width*s,c.height*s*2+6),'white')
    W.paste(c.resize((c.width*s,c.height*s),Image.LANCZOS),(0,0))
    W.paste(g.resize((c.width*s,c.height*s),Image.LANCZOS).convert('RGB'),(0,c.height*s+6))
    W.save('ciphers/hcp-1295/work/crops/'+n+'.png')
