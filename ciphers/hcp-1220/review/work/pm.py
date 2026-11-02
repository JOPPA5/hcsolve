from PIL import Image, ImageOps
import glob
im=Image.open(glob.glob('work/hires/*adr.jpg')[0]).convert('L')
# centre of receiving cancel at about (2000,430) radius 340, overview (960,200)
c=im.crop((1830,120,2410,800))
for a in (90,110,130):
    r=ImageOps.autocontrast(c.rotate(-a+180,expand=True,fillcolor=255),cutoff=1)
    r.save(f'review/work/pm_{a}.png')
d=im.crop((2450,380,3200,1100)); ImageOps.autocontrast(d,cutoff=1).save('review/work/pm2.png')
p=Image.open(glob.glob('work/hires/*pic.jpg')[0]); p.thumbnail((1000,1000)); p.save('review/work/pic.png')
