from PIL import Image
import sys
P='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1163/'
im=Image.open(P+'work/hires/cpc_1916-02-26_HU_Mezokovesd_HU_Szomolya_szomolya-20_adr.jpg').convert('RGB')
im.resize((1734,1149)).save(P+'review/work/crops/ov.png')
p=Image.open(P+'work/hires/cpc_1916-02-26_HU_Mezokovesd_HU_Szomolya_szomolya-20_pic.jpg').convert('RGB')
p.resize((867,574)).save(P+'review/work/crops/pic.png')
