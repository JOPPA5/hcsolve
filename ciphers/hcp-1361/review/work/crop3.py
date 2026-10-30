from PIL import Image, ImageOps
i=Image.open('work/hires/pc_hcp_42_adr.JPG').rotate(90,expand=True).convert('L')
rows={'stamp':(100,100,420,420,3),'cpz':(880,970,1090,1080,5),'cricket_end':(620,1060,800,1140,5),'head':(420,890,1060,990,3)}
for k,(a,b,c,d,s) in rows.items():
    x=ImageOps.autocontrast(i.crop((a,b,c,d)),cutoff=1)
    x.resize((x.width*s,x.height*s),Image.BICUBIC).save(f'review/work/{k}.png')
