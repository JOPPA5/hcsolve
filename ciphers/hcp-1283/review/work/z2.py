from PIL import Image
f='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1283/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-34_adr.jpg'
im=Image.open(f).convert('RGB')
for n,b,s in (('b1',(50,1880,800,2090),2),('b2',(760,1890,1500,2090),2),('b3',(1450,1900,2250,2080),2),('b4',(2200,1900,3000,2080),2),('st1',(2620,100,3120,420),3),('st2',(2620,380,3120,720),3)):
    c=im.crop(b); c.resize((c.width*s,c.height*s),Image.LANCZOS).save('z_%s.png'%n)
