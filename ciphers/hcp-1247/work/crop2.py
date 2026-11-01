from PIL import Image, ImageOps
im=Image.open('hires/cpc_1913-09-19_HU__HU_Jasz-Arokszalas_jolanka-44_adr.jpg').convert('RGB')
w,h=im.size
k=0.045
s=im.transform((w,h+150),Image.AFFINE,(1,0,0,0,1,-k*0-100+ -0, ),Image.BICUBIC) if 0 else im.transform((w,h),Image.AFFINE,(1,0,0,-k,1,k*800),Image.BICUBIC)
s.save('crops/shear.png')
s.resize((w//2,h//2)).crop((0,0,850,1100)).save('crops/shear_small.png')
