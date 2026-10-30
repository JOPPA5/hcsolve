from PIL import Image, ImageOps
import sys
im=Image.open('work/hires/pc_hcp_66_adr.JPG').convert('RGB')
# left half, rotate CCW 
c=im.crop((150,380,830,1110)).rotate(90,expand=True)
c.save('work/crops/msg.png'); print(c.size)
W,H=c.size
n=0
for y0 in range(0,H-100,130):
    r=c.crop((0,y0,W,min(H,y0+190)))
    r=r.resize((r.width*2,r.height*2),Image.LANCZOS); r.save(f'work/crops/band{n}.png'); n+=1
print(n)
