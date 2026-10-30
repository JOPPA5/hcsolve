from PIL import Image
s=1785/1024
p=Image.open('hires/pc_hcp_467_pic.JPG').convert('RGB')
c=p.crop((int(390*s),int(50*s),int(690*s),int(310*s))); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save('crops/p0.png')
for i,(t,b) in enumerate([(50,120),(115,180),(170,240),(235,310)]):
    c=p.crop((int(390*s),int(t*s),int(690*s),int(b*s))); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'crops/p{i+1}.png')
a=Image.open('../../hcp-1787/work/hires/'+__import__('os').listdir('../../hcp-1787/work/hires')[0]).convert('RGB')
