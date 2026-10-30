from PIL import Image
r=Image.open('crops/rot.png')
def s(box,n,z):
    c=r.crop(box); c.resize((c.width*z,c.height*z),Image.LANCZOS).save('crops/'+n)
f=2210/2000
def b(x0,y0,x1,y1): return (int(x0*f),int(y0*f+60),int(x1*f),int(y1*f+60))
s(b(1280,760,1890,885),'r7end.png',4)
s(b(160,890,420,1010),'r8st.png',5)
s(b(170,1000,330,1120),'r9st.png',5)
s(b(690,790,900,890),'r7blot.png',5)
s(b(310,520,520,690),'r5blot.png',5)
s(b(170,1100,350,1240),'r10st.png',5)
