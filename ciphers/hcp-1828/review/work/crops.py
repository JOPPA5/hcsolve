import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1828/work/hires/pc_hcp_509_adr.JPG').convert('RGB')
s=1785/1014
ys=[(145,178),(188,222),(232,275),(280,325),(328,368),(372,420),(422,466),(468,515),(520,565),(570,618)]
for i,(a,b) in enumerate(ys,1):
    c=im.crop((int(25*s),int(a*s),int(545*s),int(b*s)))
    w,h=c.size
    # two halves at 2.5x, overlapped
    for j,(l,r) in enumerate([(0,w*0.55),(w*0.45,w)]):
        p=c.crop((int(l),0,int(r),h)); p=p.resize((p.width*3,p.height*3),Image.LANCZOS)
        p.save(f'crops/r{i}_{j}.png')
