from PIL import Image
import glob
im=Image.open(glob.glob('work/hires/*adr*')[0]).convert('RGB')
Z={'rv15end':(1150,1300,1750,1440,3),'rv16start':(60,1500,760,1680,3)}
for k,(a,b,c,d,s) in Z.items():
    r=im.crop((a,b,c,d));r.resize((r.width*s,r.height*s),Image.LANCZOS).save(f'work/crops/{k}.png')
