import sys
from PIL import Image
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1147/work/hires/cpc_1916-04-20_HU_Mezokovesd_HU_Szomolya_szomolya-29_adr.jpg'
im=Image.open(src); W,H=im.size
print(W,H)
s=W/1024.0
# name, box in large-preview coordinates, scale of output
for a in sys.argv[1:]:
    n,x0,y0,x1,y1,z=a.split(','); x0,y0,x1,y1=[float(v)*s for v in (x0,y0,x1,y1)]; z=float(z)
    c=im.crop((int(x0),int(y0),int(x1),int(y1)))
    c=c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS); c.save('crops/%s.png'%n); print(n,c.size)
