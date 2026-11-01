from PIL import Image
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1250/work/hires/cpc_1913-06-16_HU__HU_Jasz-Arokszalas_jolanka-38_adr.jpg').convert('RGB')
for n,b in (('a5',(2640,440,2980,620)),('r17c',(740,1220,1000,1350)),('pm',(1620,380,2300,760))):
    c=im.crop(b); c=c.resize((c.width*4 if n!='pm' else c.width*2,c.height*4 if n!='pm' else c.height*2),Image.LANCZOS); c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1250/review/work/crops/'+n+'.png')
