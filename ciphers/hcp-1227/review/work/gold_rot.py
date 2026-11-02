from PIL import Image
f='work/hires/cpc_-09-26_HU__HU_Jasz-Arokszalas_jolanka-95_pic.jpg'
im=Image.open(f).convert('RGB').crop((2950,620,3250,1320)).rotate(-90,expand=True)
im=im.resize((im.width*2,im.height*2),Image.LANCZOS); im.save('review/work/gold_rot.png')
