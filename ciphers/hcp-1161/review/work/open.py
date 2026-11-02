from PIL import Image, ImageOps
b='work/hires/cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12_adr.jpg'
im=Image.open(b).convert('L')
R={'o2':(30,170,1340,265),'o3':(30,245,1340,345),'o4':(30,325,1340,430),'o5':(30,405,1340,515),'o6a':(30,480,700,600),'o6b':(700,440,1340,600),'o7':(30,515,720,620),
 'o10':(30,885,1340,985),'o12':(30,930,1340,1040),'o14':(380,1105,1380,1200),'o15':(30,1190,520,1300),'o21':(30,1690,1380,1790),'o22':(30,1760,1400,1860),'o23':(30,1820,1400,1910),
 'volnal':(1250,1460,1340,1570),'date':(1100,1920,2300,2110)}
for k,bx in R.items():
    c=ImageOps.autocontrast(im.crop(bx),cutoff=1); s=3 if c.width>800 else 5
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'review/work/{k}.png')
