import sys,glob
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
f=glob.glob('hires/*_pic.jpg')[0]
im=Image.open(f).convert('RGB')
x0,x1=int(sys.argv[1]),int(sys.argv[2])
step=500
y=40;i=0
while y<2090:
    c=im.crop((x0,y,x1,y+step+40)).rotate(90,expand=True).filter(ImageFilter.GaussianBlur(1))
    c=ImageOps.autocontrast(c.convert('L'),cutoff=1)
    c=c.resize((c.width*3,c.height*3),Image.LANCZOS)
    c.save('crops/%s%d.png'%(sys.argv[3],i)); i+=1; y+=step
print(i)
