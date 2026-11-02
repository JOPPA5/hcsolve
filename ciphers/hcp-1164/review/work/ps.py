import glob
from PIL import Image,ImageOps,ImageFilter
f=glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1164/work/hires/*_pic.jpg')[0]
im=Image.open(f).convert('RGB')
y=40;i=0
while y<2100:
    c=im.crop((30,y,300,y+620)).rotate(90,expand=True).filter(ImageFilter.GaussianBlur(1.2))
    r,g,b=c.split()
    c=ImageOps.autocontrast(r,cutoff=1)
    c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save('crops/ps%d.png'%i); i+=1; y+=560
print(i)
