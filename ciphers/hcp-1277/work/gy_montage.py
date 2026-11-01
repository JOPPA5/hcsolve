from PIL import Image, ImageEnhance, ImageDraw
im=Image.open('work/hires/cpc_1914-03-01_HU__HU_Jasz-Arokszalas_jolanka-48_adr.jpg').convert('RGB')
rows={}
for l in open('work/ledger-opus.txt'):
    if l[0]=='#' or l[0]=='S': continue
    p=l.split(); rows[p[0]]=p[1:]
items=[(k,i,len(v)) for k,v in rows.items() for i,t in enumerate(v) if t=='GY']
print(len(items))
def strip(k,i,n):
    r=int(k); y=165+70.4*(r-2); x=60+ (i+.5)*(1500/ n)
    c=im.crop((int(x-190),int(y-52),int(x+190),int(y+52))).resize((760,208),Image.LANCZOS)
    c=ImageEnhance.Contrast(c).enhance(1.4); ImageDraw.Draw(c).text((4,2),f'r{k} #{i}',fill=(255,0,0)); return c
for m,part in enumerate((items[:7],items[7:])):
    W=Image.new('RGB',(1530,212*4),'white')
    for j,it in enumerate(part):
        W.paste(strip(*it),((j%2)*770,(j//2)*212))
    W.save(f'work/crops2/gy{m}.png')
c=im.crop((1700,60,2500,520)); 
for a in (90,180,270): c.rotate(a,expand=True).save(f'work/crops2/pm{a}.png')
