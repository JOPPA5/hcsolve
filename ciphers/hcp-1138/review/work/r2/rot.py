import sys
from PIL import Image
src='ciphers/hcp-1138/work/hires/cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23_adr.jpg'
im=Image.open(src).convert('RGB');print(im.size)
im.thumbnail((1400,1400));im.save('ciphers/hcp-1138/review/work/r2/whole.png')
