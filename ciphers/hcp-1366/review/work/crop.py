from PIL import Image, ImageOps
import sys
i=Image.open('../../work/hires/pc_hcp_47_adr.JPG').convert('RGB')
r=i.rotate(90,expand=True)  # CCW
print(r.size)
r.save('rot.png')
# region: orig x 170..920, y 340..1090 -> rot x=y, rot y=W-x
W=i.size[0]
c=r.crop((340,W-930,1100,W-180)); c.save('msg.png'); print(c.size)
c2=c.resize((c.size[0]*2,c.size[1]*2),Image.LANCZOS)
c2.save('msg2x.png')
