import sys
from PIL import Image
f='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1283/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-34_adr.jpg'
im=Image.open(f).convert('RGB')
print(im.size)
im.resize((1400,int(1400*im.height/im.width))).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1283/review/work/full.png')
