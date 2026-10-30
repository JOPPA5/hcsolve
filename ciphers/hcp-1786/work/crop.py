import sys
from PIL import Image, ImageOps
a=Image.open('hires/pc_hcp_467_adr.JPG').convert('RGB')
p=Image.open('hires/pc_hcp_467_pic.JPG').convert('RGB')
print(a.size)
# text block on address: scale 1785/1024=1.743
s=1785/1024
rows=[(130,195),(185,240),(235,290),(280,325),(320,375),(355,415),(400,450),(440,490),(490,535),(525,570)]
for i,(t,b) in enumerate(rows):
    c=a.crop((int(55*s),int(t*s),int(520*s),int(b*s)))
    c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
    c.save(f'crops/a{i:02d}.png')
