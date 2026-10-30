from PIL import Image, ImageEnhance
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1319/'
im=Image.open(D+'work/hires/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-107_adr.jpg').convert('RGB')
s=3445/1024
c=im.crop((int(25*s),int(106*s),int(180*s),int(142*s))); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); ImageEnhance.Contrast(c).enhance(1.6).save(D+'review/work/crops/z_r3utazas.png')
