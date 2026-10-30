from PIL import Image, ImageEnhance, ImageDraw
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_adr.jpg').convert('RGB')
def g(b,s=4,k=1.8):
    x=im.crop(b);x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    return ImageEnhance.Contrast(x).enhance(k)
# row 3 soraim vs row 20-21 soraim
items=[('row 3: s o r a i m',g((1040,205,1440,300),3.2)),
       ('row 20 end: s ? r a',g((1360,1490,1600,1590),3.2)),
       ('row 21 start: ? m a',g((80,1610,330,1710),3.2)),
       ('row 7 TAILX in row 4 (szives)',g((560,300,720,400),3.2)),
       ('row 5 TAILX (Pesztorine)',g((230,400,360,500),3.2)),
       ('S6 feri',g((2980,620,3160,740),3.2))]
W=1400;H=sum(i.height+24 for _,i in items)
c=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(c);y=0
for t,i in items:
    d.text((4,y+4),t,fill='black');c.paste(i,(0,y+24));y+=i.height+24
c.save('review/work/r2/compare_soraim.png')
g((60,390,860,520),2.4).save('review/work/r2/w5b.png')
