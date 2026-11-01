from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/work/'
im=Image.open(W+'hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
# rows: step ~ 73 px. Three rows per strip, stepping 3 rows
import numpy as np
a=np.array(im.crop((80,60,1500,1950))).astype(int)
red=(a[:,:,0]-a[:,:,1]>60).sum(1)
s=''.join('#' if r>25 else '.' for r in red[::6]); print(s)
