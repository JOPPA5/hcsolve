from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
for k,b,s in (('j1',(920,235,1050,325),6),('j2',(600,360,1240,520),3)):
    x=im.crop(b); x.resize((x.width*s,x.height*s),Image.LANCZOS).save('crops/%s.png'%k)
