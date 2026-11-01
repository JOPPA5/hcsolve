import sys
from PIL import Image
PY=None
H='work/hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_%s.jpg'
adr=Image.open(H%'adr').convert('RGB'); pic=Image.open(H%'pic').convert('RGB')
adr.save('review/work/_adr_full.png') if 0 else None
adr.resize((1734,1149)).save('review/work/adr_half.png')
pic.resize((1734,1149)).save('review/work/pic_half.png')
