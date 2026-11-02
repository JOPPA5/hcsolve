from PIL import Image, ImageEnhance
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
o=im.copy(); o.thumbnail((1600,1100)); o.save('ov.png')
p=Image.open(glob.glob('../../work/hires/*pic.jpg')[0]).convert('RGB'); p.thumbnail((1000,800)); p.save('ovp.png')
