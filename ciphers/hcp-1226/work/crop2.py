"""Solver's own stamp/row crops with green print suppressed (ink = min(r,g) relative to chroma)."""
from PIL import Image, ImageOps
import sys,os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)))
im=Image.open(D+'/hires/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-85_adr.jpg').convert('RGB')
print(im.size)
def inkview(box,scale,name):
    c=im.crop(box); px=c.load(); w,h=c.size
    o=Image.new('L',c.size)
    for y in range(h):
        for x in range(w):
            r,g,b=px[x,y]
            # violet ink: g low relative to b; green print: g >= b
            v=255-min(255,max(0,(b-g+10)*6)) if g<b+5 else 255
            o.putpixel((x,y),v)
    o.resize((w*scale,h*scale),Image.LANCZOS).save(D+'/crops2/'+name+'_ink.png')
    c.resize((w*scale,h*scale),Image.LANCZOS).save(D+'/crops2/'+name+'.png')
inkview((2780,330,3120,640),4,'stamp')
