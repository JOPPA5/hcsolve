from PIL import Image, ImageOps
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
# rows blocks
for i,(y0,y1) in enumerate([(70,380),(330,640),(590,900),(850,1160),(1110,1520)]):
    for j,(x0,x1) in enumerate([(50,820),(760,1540)]):
        c=im.crop((x0,y0,x1,y1)); c=ImageOps.autocontrast(c,cutoff=1)
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'crops/b{i}{j}.png')
c=im.crop((2640,170,3160,740)); c=ImageOps.autocontrast(c,cutoff=1); c.resize((c.width*3,c.height*3),Image.LANCZOS).save('crops/stamp.png')
c=im.crop((1300,50,2800,200)); c.resize((c.width*1,c.height*1)).save('crops/top.png')
