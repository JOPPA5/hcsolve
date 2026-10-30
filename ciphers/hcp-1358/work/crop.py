from PIL import Image,ImageOps
import sys
im=Image.open('work/hires/pc_hcp_39_adr.JPG').convert('RGB')
# text area
c=im.crop((180,90,920,1100)).rotate(90,expand=True)
c.save('work/crops/all_ccw.png')
c2=im.crop((180,90,920,1100)).rotate(-90,expand=True)
c2.save('work/crops/all_cw.png')
print(c.size)
