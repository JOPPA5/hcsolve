from PIL import Image, ImageEnhance
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1319/'
im=Image.open(D+'work/hires/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-107_adr.jpg').convert('RGB')
s=3445/1024
c=im.crop((int(810*s),int(135*s),int(930*s),int(215*s)))
c=c.rotate(14,expand=True,fillcolor=(235,205,165)).resize((c.width*3,c.height*3),Image.LANCZOS); c=ImageEnhance.Contrast(c).enhance(1.4); c.save(D+'review/work/crops/z_stampline2.png')
p=im.crop((int(440*s),int(50*s),int(640*s),int(260*s)))
for a in (-105,75):
    q=p.rotate(a,expand=True,fillcolor=(235,205,165)); q=q.resize((q.width*3//2,q.height*3//2),Image.LANCZOS); q=ImageEnhance.Contrast(q.convert('L')).enhance(2.2); q.save(D+f'review/work/crops/z_pm{a}.png')
