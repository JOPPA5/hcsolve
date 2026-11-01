from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/work/'
im=Image.open(W+'hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
p=im.crop((1330,60,1750,1000)); p.resize((840,1880),Image.LANCZOS).save(W+'rows/margin1.png')
p=im.crop((1330,980,1750,1920)); p.resize((840,1880),Image.LANCZOS).save(W+'rows/margin2.png')
