from PIL import Image
im=Image.open('work/hires/pc_hcp_29_adr.JPG').convert('RGB')
r=im.rotate(90,expand=True)
print(r.size)
r.save('review/work/rot.png')
r.resize((r.width//2*1,r.height//2*1)).save('review/work/rot_small.png')
