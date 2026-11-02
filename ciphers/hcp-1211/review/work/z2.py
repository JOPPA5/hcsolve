from PIL import Image
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
s=3421/1024
Z={'row15end':(440,555,575,600,4),'row14end':(440,525,575,572,4),'row5a':(440,175,540,205,5),'row15start':(25,560,160,600,4),'pm':(640,20,985,310,1)}
for k,(x0,y0,x1,y1,f) in Z.items():
    c=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)));c=c.resize((c.width*f,c.height*f),Image.LANCZOS)
    if c.width>1600:c=c.resize((1600,c.height*1600//c.width))
    c.save(f'z_{k}.jpg',quality=88)
