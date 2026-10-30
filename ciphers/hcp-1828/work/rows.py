from PIL import Image, ImageDraw
im=Image.open('hires/pc_hcp_509_adr.JPG').convert('RGB')
rows={3:(420,500),4:(495,570),5:(575,650),6:(660,745),7:(735,815),8:(825,905),9:(915,985),10:(1020,1090)}
for r,(y0,y1) in rows.items():
    for part,(x0,x1) in enumerate([(50,350),(330,630),(610,950)]):
        c=im.crop((x0,y0-8,x1,y1+8)); c=c.resize((c.width*4,c.height*4),Image.LANCZOS)
        d=ImageDraw.Draw(c)
        for x in range(x0-x0%50+50,x1,50):
            d.line([( (x-x0)*4,0),((x-x0)*4,12)],fill=(255,0,0),width=2); d.text(((x-x0)*4+3,0),str(x),fill=(255,0,0))
        c.save(f'crops/r{r}_{part}.png')
