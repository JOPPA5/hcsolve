from PIL import Image
im=Image.open('hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg')
f=1.72
r=im.crop((int(360*f),int(285*f),int(640*f),int(350*f)));r=r.resize((r.width*3,r.height*3),Image.LANCZOS);r.save('crops/x5.png')
