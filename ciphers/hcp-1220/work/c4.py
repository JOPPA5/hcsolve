from PIL import Image
im=Image.open('crops/un_pur.png')
im.crop((100,920,1180,1260)).resize((1620,510),Image.LANCZOS).save('crops/un_l4.png')
im.crop((40,1140,1300,1520)).resize((1890,570),Image.LANCZOS).save('crops/un_l5.png')
