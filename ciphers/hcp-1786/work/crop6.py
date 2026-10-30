from PIL import Image, ImageOps, ImageFilter
s=1785/1024
p=Image.open('hires/pc_hcp_467_pic.JPG').convert('RGB').split()[0].filter(ImageFilter.GaussianBlur(0.7))
boxes=[(495,55,600,125),(410,125,540,185),(530,125,670,185),(410,175,540,240),(530,175,670,240),(420,205,540,255),(540,205,680,255),(510,240,630,310)]
for i,b in enumerate(boxes):
    c=p.crop(tuple(int(v*s) for v in b)); c=ImageOps.autocontrast(c,cutoff=1)
    c=c.resize((c.width*4,c.height*4),Image.BICUBIC); c.save(f'crops/q{i}.png')
