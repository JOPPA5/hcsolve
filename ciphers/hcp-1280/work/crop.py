from PIL import Image
im=Image.open('hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
S=3445/1024
ys=[42,82,122,162,202,240,277,315,352,390,430,472,512,555,597]
for i,y in enumerate(ys):
    t=int((y-26)*S); b=int((y+26)*S)
    for j,(l,r) in enumerate([(15,250),(235,475)]):
        c=im.crop((int(l*S),t,int(r*S),b)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'crops/r{i+1:02d}{"ab"[j]}.png')
Image.Image.save(im.crop((int(820*S),int(40*S),int(975*S),int(215*S))).resize((1040,1176)),'crops/stamp.png')
Image.Image.save(im.crop((int(450*S),int(120*S),int(985*S),int(530*S))),'crops/addr.png')
