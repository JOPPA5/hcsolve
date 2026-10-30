from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1828/work/hires/pc_hcp_509_adr.JPG').convert('RGB')
s=1785/1014
# hires px centres, per sign (eyeballed from crops): large-coord x,y; lens searched ±9 large px vertical around y
S=dict(R2e=(314,207),R4e1=(262,304),R4e2=(415,304),R6e=(500,392),R7e=(59,436),R9e=(429,544),R10e=(127,592),
       R3x=(395,250),R6x1=(277,398),R6x2=(414,398),R7x=(499,440),R8x=(121,491))
for n,(x,y) in S.items():
    g=im.convert('L')
    X=int(x*s);Y=int(y*s);res=[]
    for yy in range(Y-8,Y+9,4):
        row=[g.getpixel((xx,yy)) for xx in range(X-24,X+25)]
        d=[i for i,v in enumerate(row) if v<150]
        if not d: continue
        res.append(d[-1]-d[0]+1)
    # darkest and lightest in centre column band
    print(n,'widths',res)
g=im.convert('L');r,gg,b=im.split()
X=int(127*s);Y=int(592*s)
for yy in range(Y-14,Y+15,2):
    print(yy-Y,' '.join(f'{g.getpixel((xx,yy)):3d}' for xx in range(X-12,X+13,2)))
