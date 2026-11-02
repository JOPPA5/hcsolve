from PIL import Image, ImageOps
b='work/hires/cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12_adr.jpg'
im=Image.open(b).convert('L')
R={'kab':(40,800,520,985,4),'volnal2':(860,1460,1100,1570,6),'open2':(30,170,700,345,3),'open2b':(660,170,1340,345,3),'open3':(30,320,700,500,3),'open3b':(660,320,1340,500,3),'o10a':(30,880,700,985,3),'o10b':(660,840,1340,985,3),'o14b':(380,1100,1380,1205,2),'o15a':(30,1190,520,1300,3)}
for k,(x0,y0,x1,y1,s) in R.items():
    c=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=1)
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'review/work/{k}.png')
