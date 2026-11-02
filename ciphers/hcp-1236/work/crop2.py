from PIL import Image
im=Image.open('hires/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_adr.jpg').convert('RGB')
s=3445/1024
y=250;n=0
while y<645:
    n+=1
    for j,(a,b) in enumerate([(15,260),(240,505)]):
        im.crop((int(a*s),int(y*s),int(b*s),int((y+85)*s))).save(f'crops/b{n:02d}_{j}.png')
    y+=60
print(n)
