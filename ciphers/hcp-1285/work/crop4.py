from PIL import Image
im=Image.open('hires/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_adr.jpg').convert('RGB')
c=im.crop((2800,290,3120,680)); c.resize((c.width*4,c.height*4),Image.LANCZOS).save('crops/box_up.png')
c2=c.rotate(-90,expand=True); c2.resize((c2.width*4,c2.height*4),Image.LANCZOS).save('crops/box_cw.png')
