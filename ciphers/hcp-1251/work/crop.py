from PIL import Image
im=Image.open('hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg').convert('RGB')
ys=[100,191,275,360,437,515,590,667,735,805,889,956,1028,1100,1163,1238,1295,1371,1425,1484,1558,1620,1690,1739,1805]
for i in range(0,len(ys),4):
    for hx,(a,b) in enumerate([(60,620),(580,1140),(1100,1660)]):
        W=(b-a)*3;H=125*3
        m=Image.new('RGB',(W,(H+12)*len(ys[i:i+4])),'white')
        for j,y in enumerate(ys[i:i+4]):
            m.paste(im.crop((a,y-62,b,y+63)).resize((W,H),Image.LANCZOS),(0,j*(H+12)))
        m.save(f'rows/r{i:02d}_{hx}.png')
