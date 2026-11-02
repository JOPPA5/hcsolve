from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
B={'szov':(420,565,520,625) ,'mar':(240,965,420,1030),'kis':(40,955,250,1020)}
for n,b in B.items():
    cr=im.crop(tuple(int(x*s) for x in b)); cr.resize((cr.width*5,cr.height*5),Image.LANCZOS).save(f'crops/t_{n}.png')
# locate szoval by whole-row strip of L12a at moderate zoom
cr=im.crop((int(40*s),int(555*s),int(460*s),int(625*s))); cr.resize((cr.width*2,cr.height*2),Image.LANCZOS).save('crops/t_row12.png')
cr=im.crop((int(620*s),int(445*s),int(840*s),int(530*s))); cr.resize((cr.width*3,cr.height*3),Image.LANCZOS).save('crops/t_megy.png')
cr=im.crop((int(640*s),int(395*s),int(840*s),int(460*s))); cr.resize((cr.width*3,cr.height*3),Image.LANCZOS).save('crops/t_lehem.png')
cr=im.crop((int(170*s),int(395*s),int(320*s),int(460*s))); cr.resize((cr.width*3,cr.height*3),Image.LANCZOS).save('crops/t_hogy.png')
