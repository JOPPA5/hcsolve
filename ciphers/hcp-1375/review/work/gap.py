from PIL import Image
import datetime
i=Image.open('work/hires/pc_hcp_56_adr.JPG').convert('L').crop((90,50,840,1110)).rotate(90,expand=True)
# column band around hook top (rot coords): bowl bottom ~y 402, hook top ~y 416, x 894-906 (from y_tq_hook: x=860+px/8)
for y in range(396,424):
    row=[i.getpixel((x,y)) for x in range(892,908)]
    print(y,min(row),sum(row)//len(row))
print('paper ref',sum(i.getpixel((x,y)) for x in range(920,935) for y in range(420,428))//(15*8))
print(datetime.date(1907,10,15).strftime('%A'))
p=Image.open('work/hires/pc_hcp_56_pic.JPG');p.thumbnail((1000,1000));p.convert('RGB').save('review/work/pic.jpg')
