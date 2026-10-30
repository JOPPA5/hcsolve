from PIL import Image, ImageOps
r=Image.open('rot.png').convert('L')
b={'y_boe':(190,1095,400,1215,6),'y_year':(440,1480,720,1640,5),'y_efb':(600,930,800,1040,6),'y_tpn':(540,1010,800,1120,6)}
for k,v in b.items():
    c=ImageOps.autocontrast(r.crop(v[:4]),cutoff=1); c.resize((c.width*v[4],c.height*v[4]),Image.LANCZOS).save(k+'.png')
pm=Image.open('../../work/hires/pc_hcp_39_adr.JPG').crop((1420,290,1630,400)); pm.resize((pm.width*7,pm.height*7),Image.LANCZOS).save('y_pm.png')
