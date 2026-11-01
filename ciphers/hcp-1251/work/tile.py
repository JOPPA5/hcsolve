from PIL import Image
im=Image.open('hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg').convert('RGB')
for iy,y in enumerate(range(480,1900,420)):
    for hx,(a,b) in enumerate([(60,620),(580,1140),(1100,1660)]):
        im.crop((a,y,b,y+470)).resize(((b-a)*3,470*3),Image.LANCZOS).save(f'tiles/t{iy}_{hx}.png')
