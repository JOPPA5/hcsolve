from PIL import Image, ImageOps
r=Image.open('adr_ccw.png').convert('RGB')
print(r.size)
W,H=r.size
# message occupies lower or upper part of rotated
r.resize((W//2,H//2)).save('ov.png')
