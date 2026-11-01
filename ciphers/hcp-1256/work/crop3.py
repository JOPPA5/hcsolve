from PIL import Image
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_adr.jpg').convert('RGB')
Z={'x1':(1300,1440,1660,1560),'x2':(2500,1880,2950,1990),'x3':(2850,1880,3280,1990),'x4':(1030,1950,1420,2060),'x5':(1250,1700,1620,1790),
'x6':(40,1840,330,1960),'x7':(2620,120,3020,380),'x8':(2620,330,3020,580),'x9':(2620,520,3020,720),'x10':(1130,620,1450,720),'x11':(700,1280,1050,1380),'x12':(1050,870,1300,980)}
for k,b in Z.items():
    c=im.crop(b);s=4
    c.resize((c.width*s,c.height*s),Image.BICUBIC).save(f'crops/{k}.png')
