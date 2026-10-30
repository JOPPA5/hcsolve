from PIL import Image
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
reg=im.crop((50,40,900,1120))
r=reg.rotate(90,expand=True)
r.save('work/crops/rot90.png')
print(r.size)
r=reg.rotate(-90,expand=True); r.save('work/crops/rotm90.png')
r=reg.rotate(180,expand=True); r.save('work/crops/rot180.png')
