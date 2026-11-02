from PIL import Image
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1024
# (yc left, yc right) in large coordinates; lines slope
rows=[(28,22),(64,66),(90,90),(116,118),(146,148),(176,176),(202,204),(230,232),(258,260),(286,288),(314,316),(342,346),(372,372),(386,410),(410,425)]
for i,(a,b) in enumerate(rows):
    out=Image.new('RGB',(1464,1250),'white')
    for p in range(3):
        x0=30+p*158; x1=x0+168
        yc=a+(b-a)*(p+.5)/3
        c=im.crop((int(x0*S),int((yc-24)*S),int(x1*S),int((yc+24)*S)))
        c=c.resize((1464,int(c.height*1464/c.width)),Image.LANCZOS)
        out.paste(c,(0,p*415))
    out.save(f'crops/row{i:02d}.jpg',quality=92)
