from PIL import Image
im=Image.open('work/hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
print(im.size)
im.crop((80,430,700,520)).resize((1860,270),Image.LANCZOS).save('work/review1/r05_left.png')
s=im.copy(); s.thumbnail((1100,1100)); s.save('work/review1/adr_small.png')
