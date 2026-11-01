from PIL import Image, ImageOps
im=Image.open('work/hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
print(im.size)
S=im.size[0]/1024
box=(int(842*S),int(72*S),int(960*S),int(112*S))
x=im.crop(box); x=x.resize((x.width*5,x.height*5),Image.LANCZOS); x.save('work/crops/z_box_rows23.png')
# blue-green ratio: the two inks differ most here (dark red strokes vs pale pink wash)
r,g,b=x.split()
ImageOps.autocontrast(g.point(lambda v:min(255,int(v)))).save('work/crops/z_box_rows23_g.png')
