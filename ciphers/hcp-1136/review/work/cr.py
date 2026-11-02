from PIL import Image, ImageEnhance
import glob,sys
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1600
b=[('A',20,130),('B',120,220),('C',205,305),('D',320,420),('E',405,500),('F',485,585),('G',580,690),('H',715,815),('I',800,900),('J',885,975)]
for n,y0,y1 in b:
    for s,(x0,x1) in {'L':(30,410),'R':(390,790)}.items():
        c=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
        c=c.resize((int(c.width*1.8),int(c.height*1.8)),Image.LANCZOS)
        ImageEnhance.Contrast(c).enhance(1.3).save(f'c{n}{s}.png')
