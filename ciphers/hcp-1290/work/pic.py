from PIL import Image
im=Image.open('hires/cpc_-02-_HU__HU_Jasz-Arokszalas_jolanka-92_pic.jpg').convert('RGB')
c=im.crop((60,200,760,1950)).rotate(-90,expand=True); c.resize((1600,640)).save('crops/verse.jpg',quality=85)
