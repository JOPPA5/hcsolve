import sys
from PIL import Image
im=Image.open('work/hires/cpc_1914-03-01_HU__HU_Jasz-Arokszalas_jolanka-48_adr.jpg').convert('RGB')
print(im.size)
im.resize((1400,int(1400*im.size[1]/im.size[0]))).save('review/work/full.png')
