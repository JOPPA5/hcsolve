from PIL import Image
im=Image.open('../../work/hires/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_adr.jpg').convert('RGB')
c=im.crop((2330,440,2760,760));c.resize((c.width*3,c.height*3),Image.LANCZOS).save('z_szeprem.png')
