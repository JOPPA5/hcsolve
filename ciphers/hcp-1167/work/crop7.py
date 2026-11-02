from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
B={'a':(30,235,300,285),'b':(30,322,340,372),'c':(320,322,660,372),'d':(560,425,790,472),'e':(30,575,250,625),'f':(400,740,640,795),
   'g':(55,828,290,880),'h':(640,630,830,685),'i':(30,190,230,240),'j':(20,925,420,985),'k':(420,945,840,1010),'l':(30,985,540,1040),'m':(640,185,830,240)}
W=1500
for n,b in B.items():
    cr=im.crop(tuple(int(x*s) for x in b)); z=min(4,W/cr.width)
    cr.resize((int(cr.width*z),int(cr.height*z)),Image.LANCZOS).save(f'crops/x_{n}.png')
