from PIL import Image
im=Image.open('work/hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_adr.jpg').convert('RGB')
J={ # name: box, scale
 'r18_end':(620,1860,1000,2010,4),
 'r17_end':(1100,1760,1650,1890,3),
 'r16_m':(70,1650,700,1800,3),
 'r16_strike':(780,1620,1500,1790,2.5),
 'r19_ve':(600,1960,1000,2090,4),
 'stamp':(2600,240,3120,640,3),
 'r15_start':(90,1520,500,1660,4),
 'r04_m':(780,380,1000,520,5),
 'r17_d':(80,1740,400,1890,4),
}
for k,(a,b,c,d,s) in J.items():
    o=im.crop((a,b,c,d)); o=o.resize((int(o.width*s),int(o.height*s)),Image.LANCZOS); o.save(f'review/work/crops/{k}.png')
