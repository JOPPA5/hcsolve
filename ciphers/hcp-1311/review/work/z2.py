from PIL import Image, ImageEnhance
import numpy as np
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg').convert('RGB')
C={
's7':(2780,690,3180,860,4),
's6':(2780,590,3160,740,4),
's1':(2720,360,3160,520,3.6),
's5':(2780,530,3080,640,4.5),
'row18b':(400,1430,620,1540,5),
}
for k,(a,b,c,d,s) in C.items():
    x=im.crop((a,b,c,d)); x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(1.8).save(f'review/work/crops/z_{k}.png')
    # green-minus-red mask: green ink dark in red channel but not in green
    a_=np.asarray(x).astype(int); g=a_[...,1]-a_[...,0]
    m=np.clip(255-(g+20)*6,0,255).astype('uint8')
    Image.fromarray(m).save(f'review/work/crops/z_{k}_m.png')
