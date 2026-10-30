from PIL import Image
im=Image.open('work/hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_adr.jpg').convert('RGB')
for k,b,s in [('s2_mid',(2780,330,2960,420),7),('s1_mid',(2740,270,2980,350),5),('postmark',(1800,220,2500,800),2)]:
    o=im.crop(b);o.resize((o.width*s,o.height*s),Image.LANCZOS).save(f'review/work/crops/{k}.png')
