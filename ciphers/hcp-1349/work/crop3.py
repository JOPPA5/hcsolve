from PIL import Image,ImageOps
m=Image.open('work/hires/pc_hcp_30_adr.JPG').convert('RGB').crop((110,420,920,1120)).rotate(90,expand=True)
def out(name,box,s=6):
    c=ImageOps.autocontrast(m.crop(box),cutoff=0.5)
    c.resize((c.width*s,c.height*s),Image.BICUBIC).save(f'work/crops/{name}.jpg',quality=90)
out('z_qq',(90,290,240,410),7)
out('z_NL1',(320,125,480,190),6)
out('z_NL3',(60,700,240,790),6)
out('z_Dd',(240,180,520,270),4)
