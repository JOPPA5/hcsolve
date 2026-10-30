from PIL import Image,ImageOps,ImageEnhance
import sys
B='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1381/'
im=Image.open(B+'work/hires/pc_hcp_62_adr.JPG').convert('RGB')
print(im.size)
# full rot variants
r=im.rotate(90,expand=True); print(r.size)
r2=im.rotate(-90,expand=True)
r.resize((r.width//3,r.height//3)).save(B+'review/work/r90.png')
r2.resize((r2.width//3,r2.height//3)).save(B+'review/work/r270.png')
