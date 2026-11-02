from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
B={'szov':(40,555,200,630),'lehet':(440,310,640,380),'lehem':(590,415,780,480),'fel':(620,465,830,530),'mely':(640,145,830,215),'hogy':(190,415,330,480)}
for n,b in B.items():
    cr=im.crop(tuple(int(x*s) for x in b)); cr.resize((cr.width*4,cr.height*4),Image.LANCZOS).save(f'crops/v_{n}.png')
