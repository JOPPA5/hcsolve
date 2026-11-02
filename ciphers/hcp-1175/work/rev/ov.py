from PIL import Image
import sys
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1175/work/hires/cpc_1915-10-25_HU_Mezokovesd_HU_Szomolya_szomolya-03_pic.jpg').convert('RGB')
print(im.size)
im2=im.copy(); im2.thumbnail((1600,1600)); im2.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1175/work/rev/ov.jpg')
