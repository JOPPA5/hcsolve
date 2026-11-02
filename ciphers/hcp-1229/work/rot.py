from PIL import Image
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1229/work/crops/'
im=Image.open(d+'right.png').rotate(90,expand=True)
w=im.width
im.crop((0,0,w//2,im.height)).save(d+'rightA.png'); im.crop((w//2,0,w,im.height)).save(d+'rightB.png')
