from PIL import Image, ImageOps, ImageDraw
A='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1291/work/hires/cpc_1913-08-31_HU__HU_Jasz-Arokszalas_jolanka-41_adr.jpg'
im=Image.open(A).convert('L')
G=[('r1 edes d',170,105,250,185),('r4 kedve d',200,295,280,375),('r6 de d',570,440,650,530),('r15 edes d',105,1190,185,1270),
('r22 kedv d',900,2000,985,2075),('S2 ed d',2960,380,3005,435),('S3 rad d',3030,445,3070,510),('S5 ked d',2995,595,3050,655),
('r12 k?e',310,1020,390,1110),('r12 e?e',525,1040,605,1130),('r12 lap p',1070,1045,1150,1125),('r12 hoz h',1145,1045,1225,1125),
('r18 min? ',780,1590,860,1670),('r18 nap p',905,1590,995,1680),('r5 he h',205,370,285,450),('r7 ho h',0,0,1,1),
('r13 n#1',350,1130,420,1210),('r13 n/d#2',700,1140,775,1230),('r5 ne n',95,375,165,455),('r9 ton n',395,770,465,850),
('r14 end',0,0,1,1),('r2 n',0,0,1,1),('r16 an n',0,0,1,1),('S1 ten n',0,0,1,1)]
G=[g for g in G if g[3]>1]
cols=8; C=240; R=(len(G)+cols-1)//cols
M=Image.new('L',(cols*C,R*(C+24)),255); d=ImageDraw.Draw(M)
for i,(t,a,b,c,e) in enumerate(G):
    k=im.crop((a,b,c,e)); s=min(C/k.width,C/k.height); k=ImageOps.autocontrast(k.resize((int(k.width*s),int(k.height*s)),Image.BICUBIC),cutoff=.5)
    x,y=(i%cols)*C,(i//cols)*(C+24); M.paste(k,(x,y+22)); d.text((x+4,y+4),t,fill=0)
M.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1291/review/work/gallery.png')
