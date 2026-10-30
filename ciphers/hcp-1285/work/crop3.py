from PIL import Image
im=Image.open('hires/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_adr.jpg').convert('RGB')
r=Image.open('crops/rot.png')
def s(img,box,n,z): 
    c=img.crop(box); c.resize((c.width*z,c.height*z),Image.LANCZOS).save('crops/'+n)
s(r,(1800,1270,2200,1540),'end.png',5)
s(im,(2720,240,3200,800),'box.png',3)
s(r,(1000,80,1300,240),'jolankam.png',5)
s(r,(1180,270,1400,420),'blot2.png',5)
s(im,(1560,420,2760,800),'stamptext.png',2)
s(im,(1500,1250,3350,2100),'addr.png',1)
s(r,(1100,880,1450,1100),'r7f.png',5)
