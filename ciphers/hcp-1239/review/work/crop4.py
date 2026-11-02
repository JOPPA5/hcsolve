from PIL import Image
im=Image.open('work/hires/cpc_1912-06-_HU__HU_Jasz-Arokszalas_jolanka-105_adr.jpg').convert('RGB')
S=1.72
for n,a,c,b,d,z in [('h13',740,755,880,830,5),('sig',1640,320,1800,370,6),('m11',45,690,160,740,6),('sig2',1640,325,1720,365,8)]:
    k=im.crop((int(a*S),int(c*S),int(b*S),int(d*S))); k.resize((int(k.width*z*0.6),int(k.height*z*0.6)),Image.LANCZOS).save(f'review/work/crops2/{n}.png')
