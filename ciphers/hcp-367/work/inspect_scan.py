from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance
p=Path(__file__).parent
im=Image.open(p.parent/'source/cryptogram.jpg').convert('RGB')
box=(50,370,990,477)
blue=im.getchannel('B').crop(box)
ImageOps.autocontrast(blue,cutoff=1).resize((2820,321)).save(p/'body-blue.png')
for i,(x,y,w,h) in enumerate([(420,380,180,50),(660,365,140,65),(150,380,180,55),(450,420,105,55)]):
 ImageOps.autocontrast(im.getchannel('B').crop((x,y,x+w,y+h)),cutoff=1).resize((w*5,h*5)).save(p/f'detail-{i}.png')
