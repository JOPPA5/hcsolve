from PIL import Image
im=Image.open('hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg')
f=1.72
r=im.crop((int(640*f),int(275*f),int(860*f),int(350*f)));r=r.resize((r.width*3,r.height*3),Image.LANCZOS);r.save('crops/x5.png')
r=im.crop((int(380*f),int(520*f),int(700*f),int(620*f)));r=r.resize((r.width*2,r.height*2),Image.LANCZOS);r.save('crops/x9.png')
