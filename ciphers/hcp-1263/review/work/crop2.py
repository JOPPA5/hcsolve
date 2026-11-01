from PIL import Image
im=Image.open('../../work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-109_adr.jpg').convert('RGB')
C={'r6':(400,580,920,675,3),'r7':(700,650,1100,760,4),'r8':(80,760,400,850,4),'r14':(840,1250,1130,1335,5),'r15':(1180,1360,1480,1450,5),
'r17':(820,1545,1320,1655,3.5),'r20':(90,1860,400,1945,5),'r21L':(90,1940,520,2065,4),'r21R':(800,1950,1200,2075,4),'r19b':(820,1740,1060,1840,6),'r21b':(1380,1960,1650,2075,5),
's57':(2670,570,3040,750,4),'s1':(2620,260,3030,350,4)}
for k,(a,b,c,d,s) in C.items():
    x=im.crop((a,b,c,d)); x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS).save(f'crops/z_{k}.png')
p=Image.open('../../work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-109_pic.jpg').convert('RGB'); p.resize((1200,770)).save('crops/pic.png')
