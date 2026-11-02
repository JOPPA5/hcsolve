from PIL import Image, ImageOps
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1295/work/hires/cpc_1912-06-06_HU__HU_Jasz-Arokszalas_jolanka-24_adr.jpg'
im=Image.open(src).convert('RGB').crop((80,20,1720,2160)).rotate(-3.2,resample=Image.BICUBIC,fillcolor=(230,200,160))
im.save('desk.png')
im2=im.resize((im.width//2,im.height//2)); im2.save('desk2.png'); print(im.size)
