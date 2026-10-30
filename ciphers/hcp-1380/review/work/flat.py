import numpy as np
from PIL import Image
t=np.asarray(Image.open('work/hires/pc_hcp_61_adr.JPG').convert('L').crop((60,300,820,1140)).rotate(90,expand=True)).astype(float)
m=np.asarray(Image.open('review/work/wm_median.png')).astype(float)
r=np.clip(t/np.maximum(m,1),0,1.05)
r=np.clip((r-0.45)/(0.97-0.45),0,1)
im=Image.fromarray((r*255).astype('uint8'))
im.save('review/work/flat.png')
im.resize((im.width*2,im.height*2),Image.BICUBIC).save('review/work/flat2x.png')
for i,(a,b) in enumerate([(40,140),(120,230),(210,320),(300,420),(390,510),(470,590),(550,680),(630,760)]):
    x=im.crop((0,a,im.width,b)); x.resize((x.width*2,x.height*2),Image.BICUBIC).save(f'review/work/f{i+1}.png')
