from PIL import Image, ImageEnhance
B='work/hires/cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44_'
im=Image.open(B+'adr.jpg').convert('RGB')
f=2.1675
T={'open':(40,50,720,205,2),'hu':(270,915,420,975,5),'udv':(470,880,640,935,5),'par':(420,915,740,975,4),'em':(160,385,330,425,5),'blot':(370,395,470,470,5),
   'ezta':(30,730,180,775,5),'ment':(640,560,720,610,6),'virag':(30,605,300,650,4),'meg':(30,515,240,560,4)}
for k,(l,t,r,b,s) in T.items():
    c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f))); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c=ImageEnhance.Contrast(c).enhance(1.5); c.save('review/work/z_%s.png'%k)
c=im.crop((int(630*f),int(350*f),int(695*f),int(660*f))).rotate(90,expand=True); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save('review/work/z_margin.png')
c=im.crop((int(1100*f),int(10*f),int(1510*f),int(370*f))); c=c.resize((c.width*1,c.height*1)); c.save('review/work/z_pm.png')
c=im.crop((int(700*f),int(50*f),int(1500*f),int(910*f))); c.thumbnail((1500,1500)); c.save('review/work/z_addr.png')
