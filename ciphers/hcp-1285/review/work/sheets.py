from PIL import Image
r=Image.open('rot.png')
ys=[110,190,265,345,425,495,565,640,710,790]
f=1.7225
hw=110 # half height px
strips=[]
for i,y in enumerate(ys):
    Y=int(y*f)
    for x0,x1 in ((130,1180),(1100,2170)):
        c=r.crop((x0,Y-95,x1,Y+95)); strips.append(c.resize((int(c.width*1.85),int(c.height*1.85)),Image.LANCZOS))
for s in range(0,20,6):
    part=strips[s:s+6]
    W=max(p.width for p in part);H=sum(p.height+8 for p in part)
    o=Image.new('RGB',(W,H),'white');y=0
    for p in part:o.paste(p,(0,y));y+=p.height+8
    o.save(f'sheet{s//6+1}.png')
