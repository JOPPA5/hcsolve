import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
rows=[(60,125),(110,175),(170,235),(225,290),(285,345),(340,405),(395,455),(440,505),(495,560),(560,625),(620,680),(680,745),(735,795),(785,850),(845,905),(895,960),(950,1015),(1005,1060),(1050,1105),(1090,1155),(1135,1205)]
f=1.72
for i,(a,b) in enumerate(rows,1):
    for j,(l,r) in enumerate([(45,320),(290,580),(550,860)]):
        c=im.crop((int(l*f),int(a*f),int(r*f),int(b*f)))
        c=c.resize((c.width*3,c.height*3),Image.LANCZOS)
        c.save(f'{sys.argv[2]}/r{i:02d}_{j}.png')
