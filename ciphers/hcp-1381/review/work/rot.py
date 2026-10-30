from PIL import Image,ImageOps
import sys
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1381/work/hires/pc_hcp_62_adr.JPG');print(im.size)
im.convert('RGB').resize((im.width//3,im.height//3)).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1381/review/work/full.png')
