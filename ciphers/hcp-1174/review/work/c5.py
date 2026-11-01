from PIL import Image
adr=Image.open('work/hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
c=adr.crop((930,1760,1330,1900)); c.resize((c.width*3,c.height*3),Image.LANCZOS).save('review/work/y_mondd4.png')
