from PIL import Image
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
s=3421/1024
Z={'blot12':(20,440,130,480,6),'row15end':(470,505,575,560,5),'r17viszo':(530,615,640,650,6),'r7end':(400,235,490,290,5),'r16wave':(180,590,300,630,5),'r4bars':(120,130,220,165,5),'r7n':(330,245,480,285,5),'r10start':(30,380,130,420,4)}
for k,(x0,y0,x1,y1,f) in Z.items():
    c=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)));c=c.resize((c.width*f//1,c.height*f//1),Image.LANCZOS)
    if c.width>1600:c=c.resize((1600,c.height*1600//c.width))
    c.save(f'z_{k}.jpg',quality=88)
