from PIL import Image
im=Image.open('hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg').convert('RGB')
c=im.crop((1380,800,1740,920)); c.resize((c.width*4,c.height*4),Image.LANCZOS).save('tiles/z_r11e.png')
