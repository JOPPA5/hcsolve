from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_adr.jpg').convert('RGB')
S=0.04
def strip(y,x0,x1,h=130,s=2.5):
    w=x1-x0
    t=im.transform((w,h),Image.AFFINE,(1,0,x0,-S,1,y-h/2+S*(x0-70)*0-S*(x0-70)*1+0),Image.BICUBIC)
    return t
def sheet(n,yL):
    # y at x: yL - S*(x-70)
    def st(x0,x1):
        h=130;w=x1-x0;yc=yL-S*(x0-70)
        return im.transform((w,h),Image.AFFINE,(1,0,x0,-S,1,yc-h/2),Image.BICUBIC).resize((int(w*2.5),int(h*2.5)),Image.LANCZOS)
    a,b=st(60,840),st(780,1600)
    c=Image.new('RGB',(2060,660),'white');c.paste(ImageEnhance.Contrast(a).enhance(1.6),(0,0));c.paste(ImageEnhance.Contrast(b).enhance(1.6),(0,335))
    c.save(f'crops/{n}.png')
import sys
ys=[int(v) for v in sys.argv[1:]]
for y in ys: sheet(f's{y}',y)
