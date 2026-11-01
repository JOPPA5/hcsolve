import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1281/work/hires/cpc_1914-06-10_HU__HU_Jasz-Arokszalas_jolanka-54_adr.jpg').convert('RGB')
s=1.7225
def c(n,x0,y0,x1,y1,z=2.0,rot=0):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    if rot: r=r.rotate(rot,expand=True)
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS)
    r.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1281/work/crops/%s.png'%n)
ys=list(range(35,1200,145))
for i,y in enumerate(ys):
    c('L%02d'%i,40,y,520,y+165)
    c('R%02d'%i,480,y,1000,y+165)
c('stamp',1580,140,1860,450,3)
c('edge',1860,840,1940,1190,3)
c('bot',800,1110,1940,1190,1.2)
