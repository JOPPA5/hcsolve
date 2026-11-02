from PIL import Image
im=Image.open('crops/un_pur.png')
im.crop((560,720,1240,1010)).resize((1700,725),Image.LANCZOS).save('crops/un_l3.png')
im.crop((250,1300,1400,1560)).resize((1725,390),Image.LANCZOS).save('crops/un_l6.png')
