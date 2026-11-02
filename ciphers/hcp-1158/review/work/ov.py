from PIL import Image
B='work/hires/cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44_'
for s in ('adr','pic'):
    im=Image.open(B+s+'.jpg'); im.thumbnail((1600,1600)); im.save('review/work/ov_%s.png'%s)
