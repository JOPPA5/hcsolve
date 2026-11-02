from PIL import Image
im=Image.open('../hires/cpc_1915-10-25_HU_Mezokovesd_HU_Szomolya_szomolya-03_adr.jpg').convert('RGB')
im2=im.copy(); im2.thumbnail((1700,1700)); im2.save('adr_ov.jpg')
