from PIL import Image
im=Image.open('../../work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_adr.jpg').convert('RGB')
ys=[(100,240),(250,395),(395,540),(530,690),(690,830),(830,960),(960,1090),(1090,1220),(1215,1365),(1350,1480),(1460,1600),(1590,1720),(1720,1880),(1850,1990),(1930,2080)]
# stack per group of 3 rows, left and right halves
for g in range(0,15,3):
  for side,(x0,x1) in {'L':(90,920),'R':(880,1720)}.items():
    rows=ys[g:g+3]
    H=sum((b-a)*2+10 for a,b in rows)
    c=Image.new('RGB',((x1-x0)*2,H),'white');y=0
    for a,b in rows:
      r=im.crop((x0,a,x1,b)).resize(((x1-x0)*2,(b-a)*2),Image.LANCZOS);c.paste(r,(0,y));y+=(b-a)*2+10
    c.save(f'g{g//3+1}{side}.png')
im.crop((2780,170,3300,720)).resize((1560,1650),Image.LANCZOS).save('stamp.png')
