from PIL import Image, ImageOps
import sys
im=Image.open('work/hires/pc_hcp_64_adr.JPG').convert('RGB')
# message area on hires (scale 1.743)
m=im.crop((150,80,950,1110)).rotate(90,expand=True)
print(m.size)
m.save('work/crops/msg.png')
W,H=m.size
# strips across (lines), split into 2 horizontal segments with 3x
for i,(x0,x1) in enumerate([(0,600),(500,1040)]):
  c=m.crop((x0,0,x1,H)).resize(((x1-x0)*2,H*2),Image.LANCZOS)
  c.save(f'work/crops/seg{i}.png')
