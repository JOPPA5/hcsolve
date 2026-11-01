import sys
from PIL import Image, ImageEnhance
src="work/hires/cpc_1915-09-26_HU_Mezokovesd_HU_Szomolya_szomolya-01_adr.jpg"
im=Image.open(src).convert("RGB")
boxes={"r1":(60,1860,900,2040),"r2":(860,1860,1700,2040),"r3":(1660,1860,2500,2040),"r4":(2460,1860,3260,2040),"up":(1880,1860,2800,1990)}
for n,b in boxes.items():
    c=im.crop(b); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c=ImageEnhance.Contrast(c).enhance(1.6); c.save(f"review/work/{n}.png")
