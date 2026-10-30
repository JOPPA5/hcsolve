from PIL import Image
r=Image.open('crops/rot.png')
ys=[(30,175),(170,300),(290,430),(425,560),(530,690),(640,790),(760,890),(880,1020),(990,1125),(1100,1290)]
f=2210/2000
for i,(a,b) in enumerate(ys,1):
    Y0,Y1=int(a*f+60),int(b*f+60)
    X=[(180,1150),(1000,2170)]
    for j,(x0,x1) in enumerate(X):
        c=r.crop((x0,Y0,x1,Y1)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'crops/r{i:02d}{"ab"[j]}.png')
