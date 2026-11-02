import glob
from PIL import Image,ImageOps,ImageFilter
f=glob.glob('hires/*adr.jpg')[0]
im=Image.open(f).convert('RGB').crop((2800,270,3160,600))
g=im.split()[1].filter(ImageFilter.GaussianBlur(0.8))
g=ImageOps.equalize(g).resize((1440,1320),Image.BICUBIC);g.save('crops/triG.png')
b=im.resize((1440,1320),Image.BICUBIC);b.save('crops/triRGB.png')
