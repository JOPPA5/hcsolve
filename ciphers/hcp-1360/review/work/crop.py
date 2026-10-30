from PIL import Image
im=Image.open('ciphers/hcp-1360/work/hires/pc_hcp_41_adr.JPG');print(im.size)
r=im.rotate(90,expand=True);r.save('ciphers/hcp-1360/review/work/rot.png');print(r.size)
r.thumbnail((1600,1600));r.save('ciphers/hcp-1360/review/work/rot_small.png')
