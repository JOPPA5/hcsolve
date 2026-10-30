from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg').convert('RGB')
C={
'row06':(1200,420,1600,560,4),
'row18':(420,1270,760,1400,4),
'row25':(800,1960,1180,2080,4),
'row26':(100,2040,420,2170,4),
'end':(1350,1930,1950,2190,3),
'stamp':(2640,260,3280,980,2.3),
'word':(1640,290,2200,440,3),
'row19k':(1350,1490,1620,1620,4),
'row1k':(1000,70,1600,190,3),
}
for k,(a,b,c,d,s) in C.items():
    x=im.crop((a,b,c,d)); x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(1.7).save(f'review/work/crops/z_{k}.png')
