import sys
from PIL import Image, ImageOps
im=Image.open('hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB')
def c(name,box,s=2.5):
    r=im.crop(box)
    # purple ink: use green channel (ink dark), black postmark dark in all
    g=ImageOps.autocontrast(r.split()[1],cutoff=1)
    g=g.resize((int(g.width*s),int(g.height*s)),Image.LANCZOS)
    g.save('crops/%s.png'%name)
y=50
i=0
while y<2050:
    for side,(a,b) in {'L':(80,860),'R':(780,1560)}.items():
        c('b%02d%s'%(i,side),(a,y,b,y+400))
    y+=340;i+=1
