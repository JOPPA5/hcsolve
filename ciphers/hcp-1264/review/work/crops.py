from PIL import Image
import sys
im=Image.open('work/hires/cpc_-02-04_HU__HU_Jasz-Arokszalas_jolanka-93_adr.jpg').convert('RGB')
im.resize((1722,1105)).save('review/work/crops/whole.png')
W,H=im.size
# left text block split in overlapping tiles, 2.5x
for r,(y0,y1) in enumerate([(60,420),(380,740),(700,1060),(1020,1380),(1340,1700),(1660,2120)]):
    for c,(x0,x1) in enumerate([(40,880),(800,1680)]):
        t=im.crop((x0,y0,x1,y1));t=t.resize((int(t.width*2),int(t.height*2)),Image.LANCZOS);t.save(f'review/work/crops/t{r}{c}.png')
