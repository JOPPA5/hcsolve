from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
cr=im.crop((int(30*s),int(975*s),int(420*s),int(1030*s)))
cr.resize((int(cr.width*2.6),int(cr.height*2.6)),Image.LANCZOS).save('crops/r_word.png')
cr.split()[0].resize((int(cr.width*2.6),int(cr.height*2.6)),Image.LANCZOS).save('crops/r_word_red.png')
