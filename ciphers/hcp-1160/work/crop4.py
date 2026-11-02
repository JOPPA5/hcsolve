from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
R={'h1':(2350,35,2850,150,4),'h2':(1510,150,2150,260,3),'h3':(2050,150,2850,260,3)}
for k,(a,b,c,d,s) in R.items():
    x=im.crop((a,b,c,d)); x.resize((x.width*s,x.height*s),Image.LANCZOS).save('crops/%s.png'%k)
