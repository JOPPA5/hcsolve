from PIL import Image
im=Image.open('hires/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_adr.jpg').convert('RGB')
s=1.72
rows=[(40,115),(125,205),(195,290),(275,360),(365,440),(435,530),(510,590),(570,655),(640,720),(725,800),(805,880),(875,950),(960,1040),(1030,1110),(1100,1190)]
for i,(a,b) in enumerate(rows,1):
    for j,(x0,x1) in enumerate([(50,480),(450,900)]):
        c=im.crop((int(x0*s),int(a*s),int(x1*s),int(b*s)))
        c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'crops/r{i:02d}{"ab"[j]}.png')
c=im.crop((int(1590*s),int(170*s),int(1800*s),int(380*s))); c.resize((c.width*4,c.height*4),Image.LANCZOS).save('crops/stamp.png')
