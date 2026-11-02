from PIL import Image
im=Image.open('hires/cpc_1912-10-12_HU__HU_Jasz-Arokszalas_jolanka-32_adr.jpg').convert('RGB')
for i,y0 in enumerate(range(640,2110,150)):
    r=im.crop((60,y0,1800,y0+190)); r=r.resize((int(r.width*1.15),int(r.height*1.15)),Image.LANCZOS); r.save('crops/F%02d.png'%i)
print(i)
