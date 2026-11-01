from PIL import Image
im=Image.open('../../work/hires/cpc_1912-03-07_HU__HU_Jasz-Arokszalas_jolanka-07_pic.jpg').convert('RGB')
im.thumbnail((1400,1400));im.save('crops/pic.png')
