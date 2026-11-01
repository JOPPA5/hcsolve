from PIL import Image, ImageEnhance
src="work/hires/cpc_1915-09-26_HU_Mezokovesd_HU_Szomolya_szomolya-01_adr.jpg"
im=Image.open(src).convert("RGB")
boxes={"z_kar":(2880,1940,3250,2040),"z_szeb":(2470,1940,2880,2040),"z_blot":(1080,1940,1500,2040),"z_ku":(1740,1870,2060,1990),"z_ned":(2080,1870,2340,1990),"z_ke":(2160,1880,2300,2000),"z_leg":(2240,1940,2520,2040)}
for n,b in boxes.items():
    c=im.crop(b); c=c.resize((c.width*5,c.height*5),Image.BICUBIC); c=ImageEnhance.Contrast(c).enhance(1.5); c.save(f"review/work/{n}.png")
