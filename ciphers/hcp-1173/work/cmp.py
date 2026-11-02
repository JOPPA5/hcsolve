import glob
from PIL import Image, ImageOps
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
r=im.split()[0]
a=r.crop((1280,1130,1800,1240)); b=r.crop((860,350,1540,440))
W=Image.new('L',(2040,600),255)
W.paste(ImageOps.autocontrast(a).resize((1560,330)),(0,0)); W.paste(ImageOps.autocontrast(b).resize((2040,270)),(0,330)); W.save('crops/cmp_g.png')
