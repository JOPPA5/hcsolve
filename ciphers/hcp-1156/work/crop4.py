from PIL import Image
im=Image.open('work/hires/cpc_1915-12-28_HU_Mezokovesd_HU_Szomolya_szomolya-13_adr.jpg').convert('RGB')
r=im.crop((1050,2000,1760,2100)); r.resize((r.width*4,r.height*4),Image.LANCZOS).save('work/crops/x_end.png')
r=im.crop((2400,430,3200,1200)); r.rotate(-75,expand=True).save('work/crops/x_pm.png')
