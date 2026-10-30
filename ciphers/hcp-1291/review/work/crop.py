import sys
from PIL import Image, ImageOps
A='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1291/work/hires/cpc_1913-08-31_HU__HU_Jasz-Arokszalas_jolanka-41_adr.jpg'
im=Image.open(A).convert('L')
def crop(n,x0,y0,x1,y1,z=2):
    c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*z),int(c.height*z)),Image.BICUBIC)
    ImageOps.autocontrast(c,cutoff=0.5).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1291/review/work/'+n+'.png')
if __name__=='__main__':
    a=sys.argv; crop(a[1],*map(int,a[2:6]),float(a[6]) if len(a)>6 else 2)
