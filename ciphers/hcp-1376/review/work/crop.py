from PIL import Image
import sys
im=Image.open('ciphers/hcp-1376/work/hires/pc_hcp_57_adr.JPG'); print(im.size)
r=im.rotate(90,expand=True); r.save('ciphers/hcp-1376/review/work/rot.png'); print(r.size)
s=r.copy(); s.thumbnail((1500,1500)); s.save('ciphers/hcp-1376/review/work/rot_small.png')
