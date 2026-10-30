from PIL import Image, ImageOps
import numpy as np
im=Image.open('ciphers/hcp-1363/work/hires/pc_hcp_44_adr.JPG').convert('RGB').rotate(90,expand=True)
print(im.size)
im.save('ciphers/hcp-1363/review/work/r2/rot.png')
w,h=im.size
im.resize((w//2,h//2)).save('ciphers/hcp-1363/review/work/r2/rot_half.png')
