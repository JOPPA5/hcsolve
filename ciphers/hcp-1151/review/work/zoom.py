import glob
from PIL import Image, ImageOps
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1151/'
im=Image.open(glob.glob(base+'work/hires/*_adr.jpg')[0]).convert('RGB')
g=im.split()[1]
Z={'z_tovabba':(200,550,840,660,3),'z_lapodat':(40,170,300,260,4),'z_soka':(1300,1000,1640,1100,4),
   'z_szib':(1100,1560,1680,1680,3),'z_baja':(30,890,330,1000,4),'z_kaptis':(30,1000,330,1110,4),'z_kapt_end':(1400,950,1700,1040,4)}
for n,(a,b,c,d,s) in Z.items():
    r=ImageOps.autocontrast(g.crop((a,b,c,d)),cutoff=0.5); r.resize((r.width*s,r.height*s),Image.LANCZOS).save(base+'review/work/crops/%s.png'%n)
