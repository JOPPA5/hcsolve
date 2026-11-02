from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
for n,y in {'l04':232,'l07':342,'l11':540,'l14':692}.items():
    cr=im.crop((int(0*s),int((y-34)*s),int(150*s),int((y+34)*s))); cr.resize((cr.width*3,cr.height*3),Image.LANCZOS).save(f'crops/u_{n}.png')
