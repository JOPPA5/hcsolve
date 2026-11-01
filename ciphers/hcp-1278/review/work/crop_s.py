from PIL import Image
im=Image.open('../../work/hires/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr.jpg').convert('RGB')
c=im.crop((2650,180,3200,780)).rotate(-90,expand=True);c.resize((c.width*3,c.height*3),Image.LANCZOS).save('crops/stamp_rot.png')
c=im.crop((2880,250,3080,400)).rotate(-90,expand=True);c.resize((c.width*6,c.height*6),Image.LANCZOS).save('crops/stamp_marks.png')
