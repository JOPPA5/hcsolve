from PIL import Image
im=Image.open('hires/pc_hcp_24_adr.JPG').convert('L')
s=1785/1400
p=im.crop([int(x*s) for x in (40,290,625,880)])
q=p.transform(p.size,Image.AFFINE,(1,0,0,0.04,1,-5),Image.BICUBIC,fillcolor=230)
Z=5
S=[]
# boxes in S-crop display coords (2000 wide => /1.12*... ) map: disp*1.1175/3 = q px; y offset section
def b(sec,x0,y0,x1,y1):
    off=[0,525,1090,1655][sec]  # approx q*3 top
    k=1.1175/3
    S.append(q.crop((int(x0*k),int((y0*1.1175+off)/3),int(x1*k),int((y1*1.1175+off)/3))))
b(0,60,70,1000,160)
b(0,1000,70,1950,160)
b(0,20,440,1000,540)
b(1,20,90,1000,200)
b(1,960,90,1990,200)
b(1,1100,230,1990,330)
b(2,880,0,1850,90)
b(3,30,330,1000,420)
b(3,950,330,1900,420)
b(3,30,430,1000,520)
H=sum(i.height*Z+8 for i in S);W=max(i.width*Z for i in S)
m=Image.new('L',(W,H),255);y=0
for i,c in enumerate(S):
    r=c.resize((c.width*Z,c.height*Z),Image.LANCZOS);r.save('crops/z%d.png'%i)
    m.paste(r,(0,y));y+=r.height+8
print(m.size)
half=H//2
m.crop((0,0,W,half)).save('crops/ZA.png');m.crop((0,half,W,H)).save('crops/ZB.png')
