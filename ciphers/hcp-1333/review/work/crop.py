from PIL import Image
im=Image.open('work/hires/pc_hcp_14_adr.JPG').convert('RGB')
# strips (y0,y1) in hires, split in two x-halves, 3x
ys=[(120,190),(225,290),(280,350),(345,410),(400,470),(450,525),(505,575),(560,635),(625,690),(680,745),(740,810),(800,870),(860,930),(915,985),(980,1050),(1040,1110)]
for i,(a,b) in enumerate(ys):
    for j,(x0,x1) in enumerate([(50,320),(300,560),(540,840)]):
        im.crop((x0,a,x1,b)).resize(((x1-x0)*3,(b-a)*3),Image.LANCZOS).save(f'review/work/s{i:02d}_{j}.png')
# overview
im.crop((40,100,860,1120)).resize((1230,1530),Image.LANCZOS).save('review/work/over.png')
