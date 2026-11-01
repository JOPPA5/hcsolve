import sys
from PIL import Image
im=Image.open('../../work/hires/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr.jpg').convert('RGB')
im.resize((im.width//3,im.height//3)).save('crops/full.png')
# left block overview, rows in 3 bands
W=1600
for i,(t,b) in enumerate([(60,560),(520,1020),(980,1480),(1440,1940),(1800,2150)]):
    c=im.crop((40,t,W,b));c.save(f'crops/band{i}.png')
