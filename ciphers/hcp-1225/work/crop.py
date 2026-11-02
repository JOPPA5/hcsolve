from PIL import Image
import sys
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1225/work/hires/cpc_1912-02-29_HU__HU_Jasz-Arokszalas_jolanka-06_adr.jpg')
print(im.size)
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1225/work/crops/'
# overlapping bands, left & right
y0=40;h=330;step=240;i=0
y=y0
while y<2180:
    for side,(a,b) in {'L':(40,960),'R':(860,1820)}.items():
        c=im.crop((a,y,b,y+h)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'{out}b{i:02d}{side}.png')
    i+=1;y+=step
print(i)
