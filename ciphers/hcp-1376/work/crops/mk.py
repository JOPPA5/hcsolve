import sys
from PIL import Image
im=Image.open('hires/pc_hcp_57_adr.JPG').convert('RGB')
print(im.size)
m=im.crop((60,180,820,1080)).rotate(90,expand=True)
print(m.size); m.save('crops/msg.png')
w,h=m.size
for i in range(2):
    for j in range(2):
        pass
# horizontal segments
n=3
for k in range(n):
    x0=int(k*w/n)-40; x1=int((k+1)*w/n)+40
    c=m.crop((max(x0,0),0,min(x1,w),h)).resize((int((min(x1,w)-max(x0,0))*2.2),int(h*2.2)),Image.LANCZOS)
    c.save(f'crops/seg{k}.png')
