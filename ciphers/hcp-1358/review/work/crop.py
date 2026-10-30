import sys
from PIL import Image
im=Image.open('ciphers/hcp-1358/work/hires/pc_hcp_39_adr.JPG');print(im.size)
r=im.rotate(90,expand=True);print(r.size)
r.save('ciphers/hcp-1358/review/work/rot.png')
r.resize((r.width//3,r.height//3)).save('ciphers/hcp-1358/review/work/rot_small.png')
im.resize((im.width//3,im.height//3)).save('ciphers/hcp-1358/review/work/orig_small.png')
