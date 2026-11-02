from PIL import Image
p='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1228/work/'
im=Image.open(p+'hires/cpc_1913-09-07_HU__HU_Jasz-Arokszalas_jolanka-42_adr.jpg').convert('RGB')
rows=[(50,85),(88,125),(125,165),(165,205),(205,245),(240,285),(275,320),(305,350),(335,385),(375,415),(410,450),(445,485),(475,520),(505,555),(535,590),(575,620),(600,655),(635,680),(665,710),(700,750),(745,790),(775,825),(810,860),(835,885),(870,915),(900,950),(935,980),(965,1020),(1025,1065),(1075,1120),(1115,1160),(1165,1205)]
for i,(a,b) in enumerate(rows,1):
    for j,(x0,x1) in enumerate([(30,350),(330,640),(620,930)]):
        c=im.crop((int(x0*1.72),int((a-8)*1.72),int(x1*1.72),int((b+8)*1.72)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(p+f'crops/r{i:02d}_{j}.png')
# montage of rows, 3 strips per page
