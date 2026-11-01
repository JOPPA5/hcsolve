from PIL import Image
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_adr.jpg').convert('RGB')
Z={'y1':(2560,420,2920,590),'y2':(2620,130,2830,260)}
for k,b in Z.items():
    c=im.crop(b);s=5
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'crops/{k}.png')
