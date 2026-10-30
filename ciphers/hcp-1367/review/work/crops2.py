from PIL import Image, ImageEnhance
r=Image.open('work/hires/pc_hcp_48_adr.JPG').convert('RGB').rotate(90,expand=True)
boxes={'z_ibooz':(410,1225,740,1320),'z_retu':(700,1225,960,1320),'z_retu2':(800,1230,1085,1320),'z_mp':(735,1040,880,1120),'z_ng':(860,1040,1040,1140),'z_nl':(960,1425,1080,1490)}
for k,b in boxes.items():
    c=r.crop(b); s=6 if (b[2]-b[0])<300 else 4
    c=c.resize((c.width*s,c.height*s),Image.BICUBIC); ImageEnhance.Contrast(c).enhance(1.6).save(f'review/work/{k}.png')
