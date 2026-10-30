from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1354/work/hires/pc_hcp_35_adr.JPG')
print(im.size)
im=im.rotate(90,expand=True); print(im.size)
im.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1354/review/work/rot.png')
t=im.copy(); t.thumbnail((1600,1600)); t.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1354/review/work/rot_small.png')
