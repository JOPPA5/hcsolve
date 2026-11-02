from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44_adr.jpg').convert('RGB')
f=2.1675
for k,(l,t,r,b,s) in {'hu2':(30,915,290,975,4),'hu3':(170,920,270,970,6)}.items():
    c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f))); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); ImageEnhance.Contrast(c).enhance(1.5).save('review/work/z_%s.png'%k)
c=im.crop((int(1100*f),int(10*f),int(1510*f),int(370*f)))
for a in (56,236):
    c.rotate(a,expand=True,fillcolor=(240,220,190)).save('review/work/z_pm%d.png'%a)
