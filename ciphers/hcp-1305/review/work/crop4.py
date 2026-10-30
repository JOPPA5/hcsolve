from PIL import Image
im=Image.open('../../work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg').convert('RGB')
F=3445/1024
r=im.crop((int(760*F),int(100*F),int(830*F),int(190*F))).rotate(-65,expand=True)
r.resize((r.width*2,r.height*2),Image.LANCZOS).save('crops/z_pm_rot.png')
p=Image.open('../../work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_pic.jpg').convert('RGB')
r=p.crop((int(90*F),int(15*F),int(250*F),int(85*F)));r.resize((r.width,r.height),Image.LANCZOS).save('crops/z_pic_mark.png')
