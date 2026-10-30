"""Closing re-read after review 1: enlarged crops, channel views and a sign comparison panel."""
from PIL import Image, ImageEnhance, ImageOps
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg').convert('RGB')
def save(name,box,s,enh=1.8,chan=None):
    x=im.crop(box)
    if chan is not None: x=ImageOps.autocontrast(x.split()[chan],cutoff=1)
    x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(enh).save(f'work/crops2/{name}.png')
save('v_frag',(2760,720,2880,800),10)
save('v_frag_r',(2760,720,2880,800),10,1.3,0)
save('k_smudge',(2900,640,3060,740),8)
save('k_smudge_r',(2900,640,3060,740),8,1.3,0)
save('k_smudge_b',(2900,640,3060,740),8,1.3,2)
save('s6_x',(2780,620,2960,740),7)
save('f_s7',(2930,750,3120,860),7)
save('f_s7_r',(2930,750,3120,860),7,1.3,0)
