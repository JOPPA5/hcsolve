from PIL import Image
im=Image.open('work/hires/cpc_1912-06-_HU__HU_Jasz-Arokszalas_jolanka-105_adr.jpg').convert('RGB')
S=1.72
R=[('r19a',40,1140,420,1210,3),('r19b',400,1130,760,1210,3),('r19c',740,1120,1110,1210,3),('r19d',1100,1120,1490,1210,3),('r19e',1480,1070,1930,1210,2.5),
('r8',40,475,240,540,5),('r5',520,285,700,340,5),('r13',560,780,880,850,4),('r14',430,830,640,890,5),('stamp',1620,110,1880,380,4),('r6',40,335,240,410,4),('r9',40,525,200,600,4),('pm',1020,80,1360,350,3)]
for n,a,c,b,d,z in [(r[0],r[1],r[2],r[3],r[4],r[5]) for r in R]:
    k=im.crop((int(a*S),int(c*S),int(b*S),int(d*S))); k.resize((int(k.width*z/1.0*0.6),int(k.height*z/1.0*0.6)),Image.LANCZOS).save(f'review/work/crops2/{n}.png')
