from PIL import Image
im=Image.open('hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
r=im.split()[0].point(lambda v:0 if v<75 else (255 if v>150 else int((v-75)*3.4)))
for k,b in {'q1':(780,1170,1500,1290),'q2':(30,1420,1050,1570),'q3':(800,330,1500,450),'q4':(30,1540,1000,1720)}.items():
    x=r.crop(b); x=x.resize((int(x.width*2),int(x.height*2)),Image.BICUBIC); x.save('crops/i_%s.png'%k)
im.crop((1450,600,2900,1000)).save('crops/addr1.png')
