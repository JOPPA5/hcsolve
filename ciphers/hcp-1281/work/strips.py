from PIL import Image
im=Image.open('crops/sheared.png')
k=3445/1500
ys=[173,219,261,297,338,380,411,448,494,540,577,616,655,696,735,771,808,835,866,898]
for i,y in enumerate(ys,4):
    h=30
    out=Image.new('RGB',(1500,2*int(2*h*4.3)+6),'white')
    for j,(a,b) in enumerate([(25,375),(365,715)]):
        r=im.crop((int(a*k),int((y-h)*k),int(b*k),int((y+h)*k))).resize((1500,int(2*h*4.3)),Image.BICUBIC)
        out.paste(r,(0,j*(int(2*h*4.3)+6)))
    out.save('crops/row%02d.png'%i)
