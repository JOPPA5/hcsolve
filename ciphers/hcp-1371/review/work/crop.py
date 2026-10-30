from PIL import Image, ImageEnhance
im=Image.open('../../work/hires/pc_hcp_52_adr.JPG').convert('RGB').rotate(90,expand=True)
W,H=im.size
print(W,H)
# left half of postcard maps to bottom of rotated image
msg=im.crop((0,H-1000,W,H)); msg.save('msg.png'); print(msg.size)
