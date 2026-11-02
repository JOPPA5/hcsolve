"""Enlarge the right end of rows 13 to 15 (the magá- group). Run from repo root with a PIL python, -I."""
from PIL import Image, ImageEnhance
d='ciphers/hcp-1208/work/'
im=Image.open(d+'hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB').crop((1250,1130,1560,1420))
ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(2.2)).enhance(1.3).resize((1240,1160),Image.LANCZOS).save(d+'row14-15-end.jpg',quality=88)
