import sys
from PIL import Image, ImageOps
im=Image.open('hires/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-117_adr.jpg').convert('RGB')
def c(name,box,s=2.5,rot=0):
    r=im.crop(box)
    if rot: r=r.rotate(rot,expand=True)
    r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS)
    r=ImageOps.autocontrast(r.convert('L'),cutoff=1)
    r.save('crops/'+name+'.png')
if __name__=='__main__':
    # main block tiles
    y=50;i=0
    while y<2070:
        c(f'L{i:02d}',(60,y,860,y+230)); c(f'R{i:02d}',(780,y,1640,y+230),s=2.3)
        y+=200;i+=1
    c('top',(1560,40,3300,130),s=1.2)
    c('topA',(1560,40,2450,140),s=2.2); c('topB',(2400,40,3290,140),s=2.2)
    c('botA',(1540,1830,2450,2060),s=2.2); c('botB',(2400,1830,3290,2060),s=2.2)
    c('stamp',(2640,220,3170,780),s=3.5)
    c('right',(3150,40,3340,2040),s=1,rot=90)
    c('diag',(1500,130,1720,620),s=3)
    c('hand',(1700,220,2700,500),s=1.5)
