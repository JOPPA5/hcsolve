import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1797/work/hires/pc_hcp_478_adr.JPG')
print(im.size, im.info.get('dpi'))
im=im.rotate(90,expand=True)
print(im.size)
im.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1797/review/work/rot.png')
w,h=im.size
s=1400/w
im.resize((1400,int(h*s))).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1797/review/work/rot_small.png')
