from PIL import Image
for n,f in (('1353','pc_hcp_34'),('1354','pc_hcp_35')):
    im=Image.open(f'hcp-{n}/work/hires/{f}_adr.JPG').convert('L')
    print(n,im.size)
    im.rotate(90,expand=True).resize((im.height*2//3,im.width*2//3)).save(f'hcp-1348/review/work/full_{n}.png')
