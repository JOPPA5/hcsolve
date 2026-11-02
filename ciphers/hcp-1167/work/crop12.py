from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
cr=im.crop((int(30*s),int(960*s),int(180*s),int(1030*s)));cr.resize((cr.width*5,cr.height*5),Image.LANCZOS).save('crops/s_kis.png')
cr=im.crop((int(330*s),int(965*s),int(560*s),int(1035*s)));cr.resize((cr.width*4,cr.height*4),Image.LANCZOS).save('crops/s_kait.png')
