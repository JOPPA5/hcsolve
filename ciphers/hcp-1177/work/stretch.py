from PIL import Image, ImageOps
im=Image.open('work/hires/cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-31_pic.jpg').convert('L')
ImageOps.autocontrast(ImageOps.equalize(im)).resize((1400,928)).save('work/crops/pic_eq.png')
