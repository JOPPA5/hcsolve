from PIL import Image, ImageEnhance
import glob,sys
im=Image.open(glob.glob('work/hires/*adr.jpg')[0] if 0 else glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=3468/1600
bands=[('a',20,125),('b',120,215),('c',205,300),('d',325,425),('e',415,520),('f',500,600),('g',590,700),('h',715,815),('i',805,900),('j',890,975)]
for n,y0,y1 in bands:
    for side,(x0,x1) in {'L':(20,420),'R':(400,830)}.items():
        c=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c=ImageEnhance.Contrast(c).enhance(1.4)
        c.save(f'crops/{n}{side}.png')
