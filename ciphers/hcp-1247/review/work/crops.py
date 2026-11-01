from PIL import Image, ImageOps
import sys
im=Image.open('../../work/hires/cpc_1913-09-19_HU__HU_Jasz-Arokszalas_jolanka-44_adr.jpg').convert('RGB')
w,h=im.size
im.resize((w//3,h//3)).save('c/all.jpg',quality=85)
# shear so rows horizontal (independent k estimate checked by eye)
k=0.045
s=im.transform((w,h),Image.AFFINE,(1,0,0,-k,1,k*800),Image.BICUBIC)
s.save('c/shear.png')
# left panel in overlapping vertical bands at 2x width-limited
y=0
i=0
while y<h:
    c=s.crop((60,y,1700,y+320)); c=ImageOps.autocontrast(c,cutoff=1).resize((1640,320))
    c.save(f'c/band{i:02d}.jpg',quality=90); i+=1; y+=260
print(i)
