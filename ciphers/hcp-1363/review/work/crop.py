from PIL import Image, ImageOps
import sys
im=Image.open('../../work/hires/pc_hcp_44_adr.JPG'); print(im.size)
r=im.rotate(90,expand=True); print(r.size); r.save('adr_ccw.png')
r2=r.copy(); r2.thumbnail((1400,1400)); r2.save('adr_ccw_small.png')
