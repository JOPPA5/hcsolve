from PIL import Image
im=Image.open('../../work/hires/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr.jpg').convert('RGB')
B={
'y12':(60,1440,760,1600,3),
'y13a':(860,1570,1560,1720,3),
'y13b':(60,1570,860,1720,3),
'y15':(520,1790,1560,1920,2),
'y10':(60,1240,1500,1370,2),
'y11':(60,1340,1300,1480,2),
'y5':(60,580,1500,720,2),
'y6':(60,690,1500,840,2),
'y1':(60,70,1500,200,2),
'pm2':(2440,100,3000,860,2),
}
for k,(l,t,r,b,s) in B.items():
    c=im.crop((l,t,r,b));c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'crops/{k}.png')
c=im.crop((2440,100,3000,860)).rotate(90,expand=True);c.resize((c.width*2,c.height*2),Image.LANCZOS).save('crops/pm2rot.png')
