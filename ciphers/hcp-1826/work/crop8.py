from PIL import Image
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
c=im.crop((140,180,370,265)).rotate(180,expand=True); c.resize((c.width*5,c.height*5),Image.LANCZOS).save('work/crops/would2.png')
