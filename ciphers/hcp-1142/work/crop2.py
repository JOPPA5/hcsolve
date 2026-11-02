from PIL import Image
im=Image.open('hires/cpc_1906--_HU_Mezokovesd_HU_Szomolya_szomolya-41_adr.jpg').convert('RGB')
f=1.73
def s(n,box,z):
    c=im.crop(tuple(int(v*f) for v in box)); c=c.resize((c.width*z,c.height*z),Image.LANCZOS); c.save('crops/'+n)
s('bot1.png',(50,1120,340,1195),3)
s('bot2.png',(330,1120,640,1195),3)
s('bot3.png',(620,1120,960,1195),3)
s('L12x.png',(40,830,480,925),2)
s('L12y.png',(450,835,930,925),2)
s('ty.png',(300,685,420,770),5)
s('L14end.png',(760,1000,890,1070),5)
s('stamp.png',(1290,60,1840,600),1)
s('L5mid.png',(330,320,520,375),4)
