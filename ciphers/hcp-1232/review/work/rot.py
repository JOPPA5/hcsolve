from PIL import Image
im=Image.open('../../work/hires/cpc_--24_HU__HU_Jasz-Arokszalas_jolanka-89_adr.jpg').convert('RGB')
c=im.crop((700,160,1320,800))
for a in (90,120,150,180,240,270):
    c.rotate(a,expand=True).save(f'crops/pm{a}.png')
