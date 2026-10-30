from PIL import Image, ImageOps
im=Image.open('rot.png').convert('RGB')
print(im.size)
# find ink bounding of text area: dump a low-res map for orientation
im.resize((587,892)).save('rot_half.png')
