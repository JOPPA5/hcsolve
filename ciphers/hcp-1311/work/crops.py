from PIL import Image, ImageEnhance
import sys
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg').convert('RGB')
y=60;n=0
while y<2190:
    for s,(a,b) in zip('LR',[(90,900),(860,1670)]):
        c=im.crop((a,y,b,y+300)).resize((1944,720),Image.LANCZOS)
        c=ImageEnhance.Contrast(c).enhance(1.5)
        c.save(f'crops/b{n:02d}{s}.png')
    y+=270;n+=1
c=im.crop((2650,270,3250,960)).resize((1500,1725),Image.LANCZOS);ImageEnhance.Contrast(c).enhance(1.6).save('crops/stamp.png')
c=im.crop((450,1900,1950,2190)).resize((1950,377),Image.LANCZOS);c.save('crops/end.png')
c=im.crop((450,280,1100,420)).resize((1950,420));
im.crop((460,300,1150,420)).resize((1380,240)).save('crops/plain_tmp.png')
im.crop((1650,300,2450,420)).resize((1600,240)).save('crops/plain.png')
print(n)
