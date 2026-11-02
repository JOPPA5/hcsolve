from PIL import Image, ImageFilter
import numpy as np
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-67_adr.jpg').convert('RGB')
O='review/work2/'
def mask(c):
    a=np.asarray(c.filter(ImageFilter.GaussianBlur(1))).astype(float)
    m=(a[...,0]+a[...,2])/2-a[...,1]
    m=np.clip((m-np.percentile(m,5))/(np.percentile(m,99.7)-np.percentile(m,5)),0,1)
    return Image.fromarray((255*(1-m)).astype('uint8'))
def crop(n,b,s=3,m=False,rot=0):
    c=im.crop(b)
    if m:c=mask(c)
    if rot:c=c.rotate(rot,expand=True)
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(O+n)
crop('b18a.png',(1500,1850,2400,2020),2)
crop('b18b.png',(2250,1840,3300,2030),2)
crop('b18bm.png',(2250,1840,3300,2030),2,True)
crop('t1.png',(2230,1850,2560,2010),5)
crop('t1m.png',(2230,1850,2560,2010),5,True)
crop('t2.png',(2500,1850,2830,2010),5)
crop('t2m.png',(2500,1850,2830,2010),5,True)
crop('t3.png',(2780,1840,3110,2000),5)
crop('t3m.png',(2780,1840,3110,2000),5,True)
crop('t4.png',(3000,1840,3320,2070),5)
crop('t4m.png',(3000,1840,3320,2070),5,True)
crop('b19.png',(70,1950,1800,2100),2)
crop('b19b.png',(1700,1950,3300,2110),2)
crop('b19bm.png',(1700,1950,3300,2110),2,True)
crop('r20a.png',(3040,1100,3300,2060),2,False,-90)
crop('r20am.png',(3040,1100,3300,2060),2,True,-90)
crop('r20b.png',(3040,100,3300,1150),2,False,-90)
crop('top.png',(1150,40,2900,190),2,False,180)
crop('box.png',(2560,200,3100,800),3)
crop('boxm.png',(2560,200,3100,800),3,True)
crop('L1.png',(60,80,1400,520),2)
crop('L2.png',(60,500,1400,950),2)
crop('L3.png',(60,930,1400,1380),2)
crop('L4.png',(60,1360,1400,1880),2)
crop('x20a.png',(3080,1460,3290,1720),6,False,-90)
crop('x20am.png',(3080,1460,3290,1720),6,True,-90)
crop('x20b.png',(3080,1680,3290,1960),6,False,-90)
crop('x20bm.png',(3080,1680,3290,1960),6,True,-90)
crop('r13end.png',(760,1340,1200,1480),5)
crop('sb.png',(2860,560,3130,810),6)
crop('sbm.png',(2860,560,3130,810),6,True)
# comparison panel: i of row 21 etc on hires
def panel(n,bs,s=5,h=160):
    ims=[]
    for b in bs:
        c=im.crop(b); ims.append(c.resize((c.width*s,c.height*s),Image.LANCZOS))
    W=sum(i.width+12 for i in ims);H=max(i.height for i in ims)
    p=Image.new('RGB',(W,H),'white');x=0
    for i in ims:p.paste(i,(x,0));x+=i.width+12
    p.save(O+n)
crop('r13e.png',(1050,1300,1420,1500),4)
# row 21 'isten' (rotated) above row 18 tail for direct comparison
a=im.crop((1500,50,2000,190)).rotate(180).resize((1500,420),Image.LANCZOS)
b=im.crop((2640,1860,3140,2000)).resize((1500,420),Image.LANCZOS)
p=Image.new('RGB',(1500,850),'white');p.paste(a,(0,0));p.paste(b,(0,430));p.save(O+'cmp_isten.png')
a=im.crop((1960,50,2460,190)).rotate(180).resize((1500,420),Image.LANCZOS)
b=im.crop((2640,1860,3140,2000)).resize((1500,420),Image.LANCZOS)
p=Image.new('RGB',(1500,850),'white');p.paste(a,(0,0));p.paste(b,(0,430));p.save(O+'cmp_isten.png')
crop('sign_join.png',(2840,1855,2990,1985),10)
crop('sign_join_m.png',(2840,1855,2990,1985),10,True)
# panel: same structure at same scale: row18 sign / row 18 o-diaeresis / row 21 i (rotated) / row 12 i / row 16 end i / row 3 i
L=[(2840,1855,3000,1985),(1760,1860,1920,1990)]
ims=[im.crop(b) for b in L]+[im.crop((2070,60,2230,190)).rotate(180)]
ims=[i.resize((i.width*4,i.height*4),Image.LANCZOS) for i in ims]
p=Image.new('RGB',(sum(i.width+10 for i in ims),ims[0].height),'white');x=0
for i in ims:p.paste(i,(x,0));x+=i.width+10
p.save(O+'cmp_loop.png')
crop('sign_h.png',(2560,1850,2720,1990),8)
crop('sign_h_m.png',(2560,1850,2720,1990),8,True)
