import sys
from PIL import Image, ImageOps, ImageFilter
im=Image.open('hires/pc_hcp_62_adr.JPG').convert('RGB')
W,H=im.size
# message-side crop then rotate
c=im.crop((70,120,1000,1110)).rotate(90,expand=True)
c.save('crops/msg_rot.png')
r,g,b=c.split()
# blue channel: pencil dark; watermark gray
g2=ImageOps.autocontrast(g,cutoff=(1,1))
g2.save('crops/msg_g.png')
bg=g.filter(ImageFilter.GaussianBlur(25))
from PIL import ImageChops
d=ImageChops.subtract(bg,g,scale=1,offset=0)
d=ImageOps.autocontrast(d,cutoff=(0,0.5)); d=ImageOps.invert(d)
d.save('crops/msg_d.png')
print(c.size)
