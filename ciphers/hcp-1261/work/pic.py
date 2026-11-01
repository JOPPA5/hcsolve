from PIL import Image
im=Image.open('hires/cpc_1912-03-07_HU__HU_Jasz-Arokszalas_jolanka-07_pic.jpg').convert('RGB')
S=3445/1024
c=im.crop((int(830*S),int(180*S),int(975*S),int(610*S))).rotate(-90,expand=True)
c.save('crops/pic_text.png'); print(c.size)
