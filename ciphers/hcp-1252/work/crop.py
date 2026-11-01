import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1252/work/hires/cpc_1913-06-13_HU__HU_Jasz-Arokszalas_jolanka-37_adr.jpg')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1252/work/crops/'
# rows: display y-centres
ys=[68,122,160,203,238,283,318,366]
ys=[68,122,160,203,238,281,318,366]
for i,y in enumerate(ys,1):
    Y=int(y*1.72)
    for j,(a,b) in enumerate([(100,850),(780,1560)]):
        c=im.crop((a,Y-62,b,Y+62)).resize(((b-a)*5//2,124*5//2),Image.LANCZOS)
        c.save(out+f'r{i}{"ab"[j]}.png')
