from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_1915-11-29_HU_Mezokovesd_HU_Szomolya_szomolya-07_adr.jpg').convert('RGB')
R={'z_nal':(1180,1370,1570,1500,5),'z_cso':(1000,2030,1420,2130,4),'z_mind':(150,2040,1100,2150,3),'z_ul':(560,1980,1000,2060,4)}
for k,(a,b,c,d,s) in R.items():
    x=im.crop((a,b,c,d)); x=x.resize((x.width*s,x.height*s),Image.LANCZOS); ImageOps.autocontrast(x,cutoff=1).save(f'crops/{k}.png')
