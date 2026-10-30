from PIL import Image, ImageEnhance
r=Image.open('work/hires/pc_hcp_48_adr.JPG').convert('RGB').rotate(90,expand=True)
boxes={'z_uif':(620,1335,780,1400),'z_zpvs':(500,1425,660,1500),'z_nl2':(860,1420,1060,1500),'z_h':(960,1050,1050,1125),'z_f2':(700,1290,790,1330),'z_ebz':(800,1320,1050,1400)}
for k,b in boxes.items():
    c=r.crop(b); s=6
    c=c.resize((c.width*s,c.height*s),Image.BICUBIC); ImageEnhance.Contrast(c).enhance(1.6).save(f'review/work/{k}.png')
p=Image.open('work/hires/pc_hcp_48_pic.JPG').convert('RGB'); print(p.size); p.thumbnail((900,900)); p.save('review/work/pic.png')
