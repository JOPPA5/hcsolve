from PIL import Image, ImageEnhance
import numpy as np
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg').convert('RGB')
print(im.size)
C={'S_all':(2680,340,3220,880,2.6),
's5s6':(2760,520,3200,750,4),
's6s7':(2760,620,3200,870,4),
's1':(2700,350,3200,520,4),
'r26':(100,2040,420,2170,5),
'r28':(1400,2000,1900,2190,4),
'r25':(800,1960,1180,2080,6),
'r18':(400,1430,640,1540,6)}
for k,(a,b,c,d,s) in C.items():
    x=im.crop((a,b,c,d)); x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(1.7).save(f'work/crops2/{k}.png')
    A=np.asarray(x).astype(int); g=A[...,1]-A[...,0]
    Image.fromarray(np.clip(255-(g+20)*6,0,255).astype('uint8')).save(f'work/crops2/{k}_m.png')
