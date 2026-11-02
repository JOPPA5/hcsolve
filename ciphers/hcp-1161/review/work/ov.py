from PIL import Image
import sys
b='work/hires/cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12_'
for n in('adr','pic'):
    i=Image.open(b+n+'.jpg'); i.convert('RGB').resize((1734,1149)).save(f'review/work/ov_{n}.png')
