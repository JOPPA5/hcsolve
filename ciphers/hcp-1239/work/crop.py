import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
S=1.72
out=sys.argv[2]
# rows in display coords (y0,y1)
rows=[(40,105),(105,170),(150,235),(225,290),(280,345),(340,405),(390,460),(450,520),(520,590),(575,645),(650,700),(710,770),(770,830),(830,880),(880,950),(960,1010),(1000,1055),(1040,1100),(1085,1150),(1130,1205)]
for i,(a,b) in enumerate(rows,1):
    for j,(l,r) in enumerate([(40,350),(320,640),(610,960)]):
        c=im.crop((int(l*S),int(a*S),int(r*S),int(b*S)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'{out}/r{i:02d}_{j}.png')
