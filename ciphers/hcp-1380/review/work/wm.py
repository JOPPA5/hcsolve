import glob
import numpy as np
from PIL import Image, ImageEnhance
fs=[f for f in sorted(glob.glob('../hcp-13[4-9]*/work/hires/*adr.JPG')) if 'hcp-1380' not in f]
print(len(fs))
A=np.stack([np.asarray(Image.open(f).convert('L'))[300:1140,60:820] for f in fs[:25]])
med=np.median(A,axis=0).astype('uint8')
# per-card minimum envelope too
Image.fromarray(med).rotate(90,expand=True).save('review/work/wm_median.png')
t=Image.open('work/hires/pc_hcp_61_adr.JPG').convert('L').crop((60,300,820,1140)).rotate(90,expand=True)
m=Image.open('review/work/wm_median.png')
# region of the sign: frame = crops2 frame + (offset) ; crop (90,340,790,1100)->(60,300,820,1140): u+=40, v+=30
box=(430+40,170+30,760+40,300+30)
W=box[2]-box[0];H=box[3]-box[1]
o=Image.new('L',(W*4,H*8+10),255)
o.paste(t.crop(box).resize((W*4,H*4),Image.BICUBIC),(0,0))
o.paste(m.crop(box).resize((W*4,H*4),Image.BICUBIC),(0,H*4+10))
o.save('review/work/amp_vs_wm.png')
