import sys
from PIL import Image, ImageOps
im=Image.open('work/hires/pc_hcp_20_adr.JPG').convert('RGB')
print(im.size)
# lines in 1785-wide coordinates (scale 1.76 from 1014-wide view)
rows={'l1':(170,410,760,540),'l2':(170,530,820,650),'l3':(170,650,820,780),'l4':(170,760,800,880),'l5':(170,860,540,980)}
for k,b in rows.items():
    c=im.crop(b); c=ImageOps.autocontrast(c,cutoff=1).resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'work/crops/{k}.png')
