from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=1.9267
rows=[(25,150),(120,240),(210,335),(300,430),(400,525),(500,640),(620,780),(740,860)]
for i,(a,b) in enumerate(rows):
    for p,(x0,x1) in enumerate([(70,300),(285,500),(485,700),(680,900)]):
        c=im.crop((int(x0*S),int(a*S),int(x1*S),int(b*S)))
        c=c.resize((int(c.width*3.2),int(c.height*3.2)),Image.LANCZOS); c.save(f'crops/r{i}{"abcd"[p]}.png')
