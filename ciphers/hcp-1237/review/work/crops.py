from PIL import Image
import glob
im=Image.open(glob.glob('work/hires/*adr*')[0]).convert('RGB')
n=0
# left block 80..1800 wide, y 90..2120
W=[(70,900),(800,1800)]
for yi,y in enumerate(range(90,2130,330)):
    for xi,(a,b) in enumerate(W):
        c=im.crop((a,y,b,y+400)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'review/work/L{yi}{"ab"[xi]}.png')
c=im.crop((1450,1780,3280,2120));c=c.resize((c.width*1,c.height*1));c.save('review/work/bottomR.png')
c=im.crop((2750,250,3200,720));c=c.resize((c.width*3,c.height*3),Image.LANCZOS);c.save('review/work/stamp.png')
