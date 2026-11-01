import sys
from PIL import Image, ImageOps, ImageEnhance
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-69_adr.jpg').convert('RGB')
def z(name,box,s=4,enh=False):
    c=im.crop(box)
    if enh:
        r,g,b=c.split()
        c=ImageOps.autocontrast(r,cutoff=1).convert('RGB')
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save('crops/'+name+'.jpg',quality=90)
if __name__=='__main__':
    for a in sys.argv[1:]:
        n,x0,y0,x1,y1,s,e=a.split(',')
        z(n,(int(x0),int(y0),int(x1),int(y1)),int(s),e=='1')
