"""Stamp note crop: green channel minus blurred background. Run from ciphers/hcp-1272 with a Python that has PIL."""
from PIL import Image, ImageOps, ImageChops, ImageFilter
im = Image.open('work/hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
G = im.crop((2620, 600, 3120, 770)).resize((1500, 510), Image.BICUBIC).split()[1]
d = ImageChops.subtract(G.filter(ImageFilter.GaussianBlur(40)), G)
ImageOps.invert(ImageOps.autocontrast(d, cutoff=1)).resize((2000, 680)).save('work/crops/note_local.png')
