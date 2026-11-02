import glob,sys
from PIL import Image
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
for a in sys.argv[1:]:
    n,x0,y0,x1,y1,z=a.split(','); x0,y0,x1,y1=map(int,(x0,y0,x1,y1)); z=float(z)
    c=im.crop((x0,y0,x1,y1)); c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS).save(f'crops/{n}.png')
