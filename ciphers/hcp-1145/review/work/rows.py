from PIL import Image,ImageOps
im=Image.open('../../work/hires/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_adr.jpg').convert('RGB')
S=3468/1800
R=[(40,100),(92,165),(150,208),(195,258),(240,312),(295,358),(345,402),(390,448),(435,492),(485,542),(530,602),(595,642),(640,692),(685,738),(730,795),(795,848),(840,898),(900,962),(955,1012),(1000,1062),(1050,1112)]
for i,(a,b) in enumerate(R):
    for j,(x0,x1) in enumerate([(30,460),(440,870)]):
        c=im.crop((int(x0*S),int(a*S),int(x1*S),int(b*S)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        ImageOps.autocontrast(c,cutoff=1).save('r%02d_%d.png'%(i+1,j))
