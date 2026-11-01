from PIL import Image, ImageEnhance
src="work/hires/cpc_1915-09-26_HU_Mezokovesd_HU_Szomolya_szomolya-01_adr.jpg"
im=Image.open(src).convert("RGB")
boxes={"y_hook":(2010,1900,2190,1990,8),"y_blot":(1280,1945,1560,2040,7),"y_start":(1560,1870,1800,1990,7),"y_end":(3060,1920,3250,2045,8),"y_8dot":(2980,1960,3120,2045,10)}
for n,(a,b,c,d,s) in boxes.items():
    x=im.crop((a,b,c,d)); x=x.resize((x.width*s,x.height*s),Image.BICUBIC); x=ImageEnhance.Contrast(x).enhance(1.5); x.save(f"review/work/{n}.png")
# blot, red channel stretched to separate pencil strokes within the blot
x=im.crop((1280,1945,1560,2040)).split()[1]; lo,hi=x.getextrema(); x=x.point(lambda v:min(255,max(0,(v-lo)*255/(110-lo)))); x=x.resize((x.width*7,x.height*7),Image.BICUBIC); x.save("review/work/y_blot_g.png")
