import sys
from PIL import Image, ImageOps
src='work/hires/cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40_adr.jpg'
im=Image.open(src).convert('RGB')
def crop(name,box,s=2):
    c=im.crop(box); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save('work/crops/%s.png'%name)
if len(sys.argv)>1:
    a=sys.argv[1:]; crop(a[0],tuple(map(int,a[1:5])),int(a[5]) if len(a)>5 else 3); sys.exit()
# left block
y=30;i=0
while y<2150:
    crop('L%02da'%i,(30,y,900,y+330)); crop('L%02db'%i,(830,y,1700,y+330)); y+=290;i+=1
y=0;i=0
while y<900:
    crop('Ra%d'%i,(1630,y,2600,y+330)); y+=290;i+=1
