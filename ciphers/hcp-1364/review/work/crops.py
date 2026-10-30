from PIL import Image
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1364/'
im=Image.open(d+'work/hires/pc_hcp_45_adr.JPG').convert('RGB')
print(im.size)
# find text box in original orientation via ink colour
px=im.load();W,H=im.size
xs=[];ys=[]
for y in range(0,H,2):
    for x in range(0,W,2):
        r,g,b=px[x,y]
        if b-r>25 and r<130: xs.append(x);ys.append(y)
print(min(xs),max(xs),min(ys),max(ys),len(xs))
