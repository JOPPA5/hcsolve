from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1270/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-72_adr.jpg').convert('RGB')
for i,y in enumerate(range(60,1720,330)):
    for j,x in enumerate((50,760)):
        c=im.crop((x,y,x+760,y+360)); c.resize((1520,720),Image.LANCZOS).save(f'crops/L{i}{"ab"[j]}.png')
for i,x in enumerate(range(50,3350,650)):
    c=im.crop((x,1700,x+700,2010)); c.resize((1400,620),Image.LANCZOS).save(f'crops/B{i}.png')
c=im.crop((2550,230,3250,800)); c.resize((1400,1140),Image.LANCZOS).save('crops/stamp.png')
