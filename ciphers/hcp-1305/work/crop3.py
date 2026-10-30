from PIL import Image
im=Image.open('hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg')
f=1.72
C=[('y1',40,1105,420,1235,3),('y2',400,1105,780,1235,3),('y3',760,1105,1140,1235,3),('y4',1130,1085,1520,1235,3),('y5',1500,1060,1890,1235,3),
('y6',1590,120,1880,270,4),('y7',1590,330,1880,420,4),('y8',470,410,800,470,3)]
for n,a,b,c,d,s in C:
    r=im.crop((int(a*f),int(b*f),int(c*f),int(d*f)));r=r.resize((r.width*s//2,r.height*s//2),Image.LANCZOS);r.save(f'crops/{n}.png')
r=im.crop((int(1760*f),int(860*f),int(1895*f),int(1240*f))).rotate(-90,expand=True);r=r.resize((r.width*3//2,r.height*3//2));r.save('crops/edgerot.png')
