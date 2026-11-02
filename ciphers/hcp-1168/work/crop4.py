from PIL import Image, ImageOps
import glob
a=Image.open(glob.glob('work/hires/*_adr.jpg')[0]).convert('RGB')
p=Image.open(glob.glob('work/hires/*_pic.jpg')[0]).convert('RGB')
x=p.crop((30,250,160,1150)).rotate(-90,expand=True); x=x.resize((x.width*2,x.height*2)); ImageOps.autocontrast(x,cutoff=0.3).save('work/crops/pic_note.png')
x=a.crop((2500,50,3250,850)); ImageOps.autocontrast(x,cutoff=0.3).save('work/crops/stamp.png')
x=a.crop((300,1960,1120,2090)); x=x.resize((x.width*2,x.height*2),Image.BICUBIC); ImageOps.autocontrast(x,cutoff=0.3).save('work/crops/last1.png')
