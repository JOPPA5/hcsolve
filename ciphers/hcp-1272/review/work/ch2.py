from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
r=im.crop((2640,640,3120,740)); G=ImageOps.autocontrast(r.split()[1],cutoff=2)
G.resize((G.width*5,G.height*5),Image.BICUBIC).save('crops/s_l6_7.png')
