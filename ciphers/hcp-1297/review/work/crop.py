import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1297/work/hires/cpc_1912-07-07_HU__HU_Jasz-Arokszalas_jolanka-29_adr.jpg').convert('RGB')
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1297/review/work/crops/'
def c(n,x0,y0,x1,y1,z=2,g=False,rot=0):
    r=im.crop((x0,y0,x1,y1))
    if g: r=ImageOps.autocontrast(r.split()[1],cutoff=1)
    if rot: r=r.rotate(rot,expand=True)
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r.save(O+n+'.png')
if __name__=='__main__':
    a=sys.argv[1:]
    c(a[0],*map(int,a[1:5]),float(a[5]) if len(a)>5 else 2, len(a)>6 and a[6]=='g', int(a[7]) if len(a)>7 else 0)
