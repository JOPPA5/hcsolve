from PIL import Image, ImageOps
b='work/hires/cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12_adr.jpg'
im=Image.open(b).convert('L')
# name: (y0,y1)
R={'r01':(50,170),'r06':(525,625),'r07':(615,725),'r08':(705,810),'r09':(790,900),'r10':(885,975),'r12':(960,1040),'r13':(1020,1120),'r14':(1105,1200),'r15':(1190,1290),'r16':(1285,1385),'r17':(1370,1480),'r18':(1465,1565),'r19':(1555,1650),'r20':(1630,1730),'r21':(1720,1820),'r22':(1800,1900),'r23':(1900,1990),'r24':(1975,2090)}
for k,(y0,y1) in R.items():
    for s,(x0,x1) in {'a':(30,520),'b':(480,960),'c':(920,1400)}.items():
        c=im.crop((x0,y0,x1,y1)); c=ImageOps.autocontrast(c,cutoff=1)
        c.resize((c.width*4,c.height*4),Image.LANCZOS).save(f'review/work/{k}{s}.png')
