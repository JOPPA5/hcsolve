from PIL import Image, ImageOps
i=Image.open('work/hires/pc_hcp_42_adr.JPG').rotate(90,expand=True).convert('L')
rows={'gaunt':(780,1115,1080,1200),'up_day':(420,1120,770,1215),'after_L':(880,1190,1000,1270),'mh':(860,1210,1040,1300)}
for k,b in rows.items():
    c=ImageOps.autocontrast(i.crop(b),cutoff=1)
    s=6
    c.resize((c.width*s,c.height*s),Image.BICUBIC).save(f'review/work/{k}.png')
