from PIL import Image
import sys,glob
im=Image.open(glob.glob('work/hires/*adr.jpg')[0] if False else glob.glob('hires/*adr.jpg')[0]).convert('RGB')
# strips of ~3 lines, left and right half, 2.2x
S=1.927
ys=[(25,165),(145,270),(250,370),(355,490),(470,590),(575,700),(690,800),(780,900),(880,1000),(985,1120)]
for i,(a,b) in enumerate(ys):
    for j,(l,r) in enumerate([(20,470),(430,900)]):
        c=im.crop((int(l*S),int(a*S),int(r*S),int(b*S)))
        c=c.resize((int(c.width*2.1),int(c.height*2.1)),Image.LANCZOS)
        c.save(f'crops/s{i}_{j}.png')
