import sys; sys.path.insert(0,'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1291/review/work')
from crop import crop, im
from PIL import Image
crop('z_r01d',740,90,830,170,5); crop('z_r15d',170,1290,240,1370,5)
crop('z_r18d',660,1595,760,1680,5)
crop('z_r09',520,770,1060,860,2.8)
crop('z_r14',880,1250,1500,1340,2.4)
crop('z_r16',860,1400,1500,1480,2.4)
crop('z_r21',1000,1845,1650,1925,2.3)
crop('z_pm',2480,120,2800,780,1.3)
Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1291/work/hires/cpc_1913-08-31_HU__HU_Jasz-Arokszalas_jolanka-41_pic.jpg').convert('L').resize((1150,737)).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1291/review/work/pic.png')
