import sys
from PIL import Image, ImageOps
im=Image.open('ciphers/hcp-919/work/hires/cpc_1908-01-03_DE_Bensberg_DE_Oberlausitz__adr.jpg')
for spec in sys.argv[1:]:
    p=spec.split(','); name=p[0]; x0,y0,x1,y1=map(int,p[1:5]); s=float(p[5]) if len(p)>5 else 3
    c=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)).convert('L'),cutoff=1)
    c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save('ciphers/hcp-919/work/crops/%s.png'%name)
