from PIL import Image
import sys
im=Image.open('work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-113_adr.jpg').convert('RGB')
print(im.size)
im.resize((1700,1090)).save('review/work/adr_ov.png')
