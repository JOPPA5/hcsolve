from PIL import Image
im=Image.open('hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg').convert('RGB')
xs=[1600,2000,2400,2800,3050]
for i,x in enumerate(xs):
    im.crop((x,1790,x+430,2050)).resize((430*4-40,260*4),Image.LANCZOS).save(f'tiles/b{i}.png')
# stamp
im.crop((2740,100,3280,720)).resize((540*3,620*3),Image.LANCZOS).save('tiles/stamp.png')
im.crop((1540,130,1700,700)).resize((160*4,570*4),Image.LANCZOS).save('tiles/redge.png')
