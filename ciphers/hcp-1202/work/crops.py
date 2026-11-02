import sys
from PIL import Image, ImageEnhance
import os
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(D+'/hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-58_adr.jpg').convert('RGB')
def crop(name,box,s=1.0,rot=0):
    c=im.crop(box)
    if rot: c=c.rotate(rot,expand=True)
    c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    c=ImageEnhance.Contrast(c).enhance(1.5)
    c.save(D+'/crops/'+name+'.png')
if __name__=='__main__':
    # overlapping horizontal bands, left then right
    y=120;i=0
    while y<2180:
        for j,(x0,x1) in enumerate([(150,1250),(1150,2250)]):
            crop(f'b{i:02d}_{j}',(x0,y,x1,y+330),1.4)
        y+=280;i+=1
    crop('top',(1500,110,2800,300),1.2)
    crop('stamp',(2750,300,3300,900),2.2)
