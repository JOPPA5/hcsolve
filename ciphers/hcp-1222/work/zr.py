"""Crops in hi-res pixels for response to review 1. Run from the cipher dir: zr.py name l t r b scale"""
import sys
from PIL import Image
im=Image.open('work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-113_adr.jpg').convert('RGB')
n,l,t,r,b,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(l),int(t),int(r),int(b)));c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(f'work/crops/{n}.png')
