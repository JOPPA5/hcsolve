from PIL import Image,ImageOps
im=Image.open('work/crops/all_ccw.png').convert('RGB')
b=(660,270,840,350);c=ImageOps.autocontrast(im.crop(b),cutoff=0.5).resize((1080,480),Image.BICUBIC);c.save('work/crops/z_my.png')
b=(800,170,960,290);c=ImageOps.autocontrast(im.crop(b),cutoff=0.5).resize((960,720),Image.BICUBIC);c.save('work/crops/z_new.png')
