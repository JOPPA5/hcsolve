from PIL import Image
im=Image.open('ciphers/hcp-1349/work/hires/pc_hcp_30_adr.JPG')
print(im.size)
r=im.rotate(90,expand=True)
print(r.size)
r.save('ciphers/hcp-1349/review/work/rot.png')
r2=r.copy(); r2.thumbnail((1400,1400)); r2.save('ciphers/hcp-1349/review/work/rot_small.jpg')
