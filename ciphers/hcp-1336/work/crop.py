import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1336/work/hires/pc_hcp_17_adr.JPG')
print(im.size)
s=1785/1024
L=[(0,'l1',(90,235,470,295)),(1,'l2',(80,310,420,370)),(2,'l3',(85,380,460,450)),(3,'l4',(85,445,420,500)),(4,'l5',(85,495,280,545))]
for i,n,b in L:
    bb=[int(x*s) for x in b]
    c=im.crop(bb); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1336/work/crops/{n}.png')
