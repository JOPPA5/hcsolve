from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/work/'
im=Image.open(W+'hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
for y in range(60,1900,290):
    for k,(a,b) in enumerate([(70,830),(760,1530)]):
        c=im.crop((a,y,b,y+340)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(W+f'strips/y{y:04d}_{k}.png')
