import sys
from PIL import Image, ImageDraw
im=Image.open(sys.argv[1]).convert('RGB')
S=1.72
rows=[(40,105),(105,170),(150,235),(225,290),(280,345),(340,405),(390,460),(450,520),(520,590),(575,645),(640,700),(700,770),(765,830),(825,880),(875,950),(950,1010),(1000,1055),(1040,1100),(1085,1150),(1130,1205)]
Z=2.2
for g in range(0,20,4):
  for j,(l,r) in enumerate([(40,500),(470,960)]):
    cs=[]
    for i,(a,b) in enumerate(rows[g:g+4],g+1):
        c=im.crop((int(l*S),int(a*S),int(r*S),int(b*S)))
        c=c.resize((int(c.width*Z),int(c.height*Z)),Image.LANCZOS)
        ImageDraw.Draw(c).text((3,3),str(i),fill=(0,0,255))
        cs.append(c)
    H=sum(c.height+6 for c in cs)
    m=Image.new('RGB',(cs[0].width,H),'white'); y=0
    for c in cs: m.paste(c,(0,y)); y+=c.height+6
    m.save(f'mont/m{g//4}{"LR"[j]}.png')
