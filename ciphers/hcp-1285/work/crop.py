import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1285/work/hires/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_adr.jpg').convert('RGB')
print(im.size)
# text block in orig px x 110..1460, y 60..2070
r=im.rotate(-90,expand=True)  # clockwise
print(r.size)
r.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1285/work/crops/rot.png')
W,H=r.size
r.crop((0,60,W,1500)).resize((2000,int(1440*2000/W))).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1285/work/crops/all.png')
