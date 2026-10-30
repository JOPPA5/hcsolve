from PIL import Image, ImageOps
r=Image.open('rot.png').convert('L')
b={'z_efb':(600,920,830,1040,5),'z_uijt':(255,1000,420,1130,5),'z_boe':(250,1120,420,1190,6),'z_oz':(790,1130,900,1200,7),
'z_gpw':(250,1195,400,1320,5),'z_pvsjuf':(380,1230,780,1330,4),'z_iznot':(740,1190,1080,1300,4),'z_mpwf':(300,1290,640,1420,4),
'z_gspn':(600,1340,790,1420,5),'z_zpvst':(810,1340,1100,1420,5),'z_hjsm':(570,1450,1000,1560,4),
'z_date':(420,1480,640,1600,5),'z_date2':(80,1480,480,1600,4)}
for k,v in b.items():
    c=ImageOps.autocontrast(r.crop(v[:4]),cutoff=1); c.resize((c.width*v[4],c.height*v[4]),Image.LANCZOS).save(k+'.png')
pm=Image.open('../../work/hires/pc_hcp_39_adr.JPG').crop((1280,100,1720,420)); pm.resize((pm.width*3,pm.height*3),Image.LANCZOS).save('z_pm.png')
