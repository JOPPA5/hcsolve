from PIL import Image, ImageOps
import sys
im=Image.open('../../work/hires/pc_hcp_36_adr.JPG'); print(im.size)
r=im.rotate(90,expand=True); print(r.size); r.save('rot.png')
r2=r.copy(); r2.thumbnail((1600,1600)); r2.save('rot_small.png')
