from PIL import Image, ImageOps
s=1785/1024
a=Image.open('../../hcp-1787/work/hires/pc_hcp_468_adr.JPG').convert('RGB')
rows=[(30,95),(95,155),(155,210),(210,260),(260,310),(305,355),(350,395),(390,440),(435,490),(485,530),(525,575),(570,640)]
for i,(t,b) in enumerate(rows):
    c=a.crop((int(35*s),int(t*s),int(470*s),int(b*s)))
    c=ImageOps.autocontrast(c.convert('L'),cutoff=0.5)
    c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'crops/s{i:02d}.png')
p=Image.open('../../hcp-1787/work/hires/pc_hcp_468_pic.JPG').convert('RGB')
for i,(b,x0,x1,t) in enumerate([(135,170,960,30),(650,50,960,490)]):
    c=p.crop((int(x0*s),int(t*s),int(x1*s),int(b*s)))
    c=ImageOps.autocontrast(c.split()[0],cutoff=0.5)
    c=c.resize((int(c.width*1.5),int(c.height*1.5)),Image.LANCZOS); c.save(f'crops/sp{i}.png')
