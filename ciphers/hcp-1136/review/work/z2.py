from PIL import Image, ImageEnhance
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1600
Z={'csok':(280,790,560,850,4.5),'sig':(30,860,640,935,2.6),'hu':(30,855,300,925,3.5)}
for n,(a,b,c,d,f) in Z.items():
    k=im.crop((int(a*S),int(b*S),int(c*S),int(d*S)))
    k=k.resize((int(k.width*f),int(k.height*f)),Image.LANCZOS)
    ImageEnhance.Contrast(k).enhance(1.4).save('z_'+n+'.png')
