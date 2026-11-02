import sys
from PIL import Image, ImageOps
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1147/work/hires/cpc_1916-04-20_HU_Mezokovesd_HU_Szomolya_szomolya-29_adr.jpg'
im=Image.open(src); s=im.size[0]/1024.0
for a in sys.argv[1:]:
    p=a.split(','); n=p[0]; x0,y0,x1,y1=[float(v)*s for v in p[1:5]]; z=float(p[5])
    c=im.crop((int(x0),int(y0),int(x1),int(y1)))
    c=c.resize((int(c.width*z),int(c.height*z)),Image.BICUBIC)
    if len(p)>6:
        c=ImageOps.autocontrast(c.split()[0],cutoff=1).convert('RGB')
    c.save('crops/%s.png'%n); print(n,c.size)
