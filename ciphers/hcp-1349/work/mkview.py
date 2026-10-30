from PIL import Image,ImageOps
for f,n in (('work/hires/pc_hcp_30_pic.JPG','pic'),('work/hires/pc_hcp_30_adr.JPG','adr')):
    im=ImageOps.exif_transpose(Image.open(f)); print(f,im.size)
    im2=im.copy(); im2.thumbnail((1400,1400)); im2.save(f'work/crops/{n}_view.jpg',quality=85)
