from PIL import Image, ImageEnhance
import sys
im=Image.open('hires/pc_hcp_48_adr.JPG').convert('RGB')
r=im.rotate(90,expand=True)  # CCW; text reads left-right
print(r.size)
r.save('crops/reading.png')
# message region in rotated coords: x'=y, y'=W-x
W,H=im.size
box=(40,W-860,1100,W-130)
c=r.crop(box); print(c.size)
c.save('crops/msg.png')
