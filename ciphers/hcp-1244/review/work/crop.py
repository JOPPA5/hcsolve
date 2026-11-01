import sys
from PIL import Image
src='work/hires/cpc_1912-04-10_HU__HU_Jasz-Arokszalas_jolanka-16_adr.jpg'
im=Image.open(src).convert('RGB')
print(im.size)
im.resize((im.width//2,im.height//2)).save('review/work/crops/full.png')
