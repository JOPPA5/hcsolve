from PIL import Image, ImageEnhance
import sys
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1207/work/hires/cpc_--_HU__HU_Budapest_jolanka-62_adr.jpg').convert('RGB')
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1207/review/work/crops/'
def c(n,box,s=2.0,con=1.9):
    i=im.crop(box); i=i.resize((int(i.width*s),int(i.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(i).enhance(con).save(O+n+'.png'); 
if len(sys.argv)>1:
    a=sys.argv[1:]; c(a[0],tuple(int(x) for x in a[1:5]),float(a[5]) if len(a)>5 else 2.0)
else:
    # bands: each 5 rows, left and right half
    bands=[(60,500),(440,880),(820,1260),(1200,1640),(1580,2080)]
    for k,(a,b) in enumerate(bands):
        c(f'L{k}',(60,a,860,b)); c(f'R{k}',(780,a,1660,b))
    c('stamp',(2780,200,3280,740),3)
    c('bottom',(1500,1880,3320,2080),1.1)
    c('addr',(1800,1600,3320,2060),1.2)
    c('addr2',(1800,350,3000,1600),0.8)
