from PIL import Image
im=Image.open('hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
x=im.crop((1500,1960,2080,2110)); x=x.resize((x.width*3,x.height*3),Image.BICUBIC); x.save('crops/y_tail.png')
x=im.crop((130,30,1250,150)); x=x.resize((x.width*2,x.height*2),Image.BICUBIC); x.save('crops/y_T.png')
