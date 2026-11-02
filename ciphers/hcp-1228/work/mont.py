from PIL import Image,ImageDraw
p='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1228/work/'
im=Image.open(p+'hires/cpc_1913-09-07_HU__HU_Jasz-Arokszalas_jolanka-42_adr.jpg').convert('RGB')
rows=[(50,85),(88,125),(125,165),(165,205),(205,245),(240,285),(275,320),(305,350),(335,385),(375,415),(410,450),(445,485),(475,520),(505,555),(535,590),(575,620),(600,655),(635,680),(665,710),(700,750),(745,790),(775,825),(810,860),(835,885),(870,915),(900,950),(935,980),(965,1020),(1025,1065),(1075,1120),(1115,1160),(1165,1205)]
for g in range(0,len(rows),4):
  for j,(x0,x1) in enumerate([(35,490),(470,930)]):
    strips=[]
    for i in range(g,min(g+4,len(rows))):
        a,b=rows[i]
        c=im.crop((int(x0*1.72),int((a-8)*1.72),int(x1*1.72),int((b+8)*1.72)))
        s=1900/c.width; c=c.resize((1900,int(c.height*s)),Image.LANCZOS); strips.append((i+1,c))
    H=sum(c.height+6 for _,c in strips)
    o=Image.new('RGB',(1950,H),'white'); y=0; d=ImageDraw.Draw(o)
    for n,c in strips:
        o.paste(c,(50,y)); d.text((5,y+40),str(n),fill='red'); y+=c.height+6
    o.save(p+f'crops/m{g//4+1:02d}_{j}.png')
