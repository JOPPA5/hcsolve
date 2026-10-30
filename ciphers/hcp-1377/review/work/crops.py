from PIL import Image
im=Image.open('../../work/hires/pc_hcp_58_adr.JPG').convert('RGB')
r=im.crop((150,150,860,1140)).rotate(90,expand=True)
print(r.size); r.save('reading.png')
