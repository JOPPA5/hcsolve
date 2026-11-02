from PIL import Image, ImageOps
import glob,sys
im=Image.open(glob.glob('work/hires/*_adr.jpg')[0]).convert('RGB')
# strips: (name,x0,y0,x1,y1,scale)
n=0
y=30
for y in range(30,2100,190):
    for j,(a,b) in enumerate([(30,800),(740,1540)]):
        c=im.crop((a,y,b,y+240)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c=ImageOps.autocontrast(c,cutoff=0.5)
        c.save(f'work/crops/s{y:04d}_{j}.png')
