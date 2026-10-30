from PIL import Image
im=Image.open('hires/pc_hcp_2_adr.JPG').convert('RGB')
W,H=im.size
# left half, rotated so text is upright
r=im.crop((180,150,930,1100)).rotate(90,expand=True)
print(r.size)
r.resize((r.width*2,r.height*2),Image.LANCZOS).save('crops/msg2x.png')
