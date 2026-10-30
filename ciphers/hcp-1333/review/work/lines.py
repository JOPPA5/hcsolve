from PIL import Image
im=Image.open('work/hires/pc_hcp_14_adr.JPG').convert('RGB')
Y={3:407,4:480,5:540,6:607,7:667,8:722,9:787,10:853,11:917,12:967,13:1023}
for n,y in Y.items():
    for j,(a,b) in enumerate([(50,430),(410,830)]):
        im.crop((a,y-48,b,y+48)).resize(((b-a)*3,288),Image.LANCZOS).save(f'review/work/line{n:02d}{"ab"[j]}.png')
