from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_61_adr.JPG').convert('RGB')
c=im.crop((90,340,790,1100)).rotate(90,expand=True)
b={'z_come':(330,185,660,285),'z_sorry':(220,100,420,175),'z_about':(450,105,700,190),'z_to':(160,205,345,290),'z_end':(590,190,680,260)}
for k,v in b.items():
    x=c.crop(v);x=x.resize((x.width*6,x.height*6),Image.BICUBIC);ImageEnhance.Contrast(x).enhance(1.6).save(f'work/crops/{k}.png')
