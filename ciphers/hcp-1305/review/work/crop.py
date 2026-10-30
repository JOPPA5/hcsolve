import sys
from PIL import Image
im=Image.open('../../work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg').convert('RGB')
F=3445/1024
# name,x0,y0,x1,y1 in 1024-display coords
C=[('r01a',25,25,250,60),('r01b',230,25,460,60),('r02a',25,52,250,92),('r02b',230,52,480,92),
('r03a',25,78,250,115),('r03b',230,78,460,115),('r04a',25,105,250,145),('r04b',230,105,500,145),
('r05a',25,142,250,178),('r05b',230,142,450,178),('r06a',25,172,250,208),('r06b',230,172,450,208),
('r07a',25,205,250,240),('r07b',230,205,450,240),('r08a',25,235,250,272),('r08b',230,235,460,272),
('r09a',25,268,250,308),('r09b',230,268,460,308),('r10a',25,300,250,338),('r10b',230,300,470,338),
('r11a',25,335,250,370),('r11b',230,335,460,370),('r12a',25,362,250,398),('r12b',230,362,460,398),
('r13a',25,392,250,428),('r13b',230,392,460,428),('r14a',25,425,250,460),('r14b',230,425,460,460),
('r15a',25,460,250,500),('r15b',230,460,460,500),('r16a',25,495,250,530),('r16b',230,495,470,530),
('r17a',25,528,250,565),('r17b',230,528,460,565),('r18a',25,560,250,600),('r18b',230,560,480,600),('r18c',470,560,760,600),('r18d',740,550,980,600),
('r19a',25,595,250,632),('r19b',230,595,480,632),('r19c',470,595,730,632),('r19d',710,590,980,632),
('edge',925,440,985,630),('stamp',815,60,950,215)]
for n,a,b,c,d in C:
    r=im.crop((int(a*F),int(b*F),int(c*F),int(d*F)))
    s=1800/r.width if r.width>r.height else 1
    if n=='edge': s=3
    if n=='stamp': s=2.2
    r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS).save(f'crops/{n}.png')
def mont(ns,o):
    ims=[Image.open(f'crops/{n}.png') for n in ns]
    W=max(i.width for i in ims);H=sum(i.height+10 for i in ims)
    m=Image.new('RGB',(W,H),'white');y=0
    for i in ims: m.paste(i,(0,y));y+=i.height+10
    m.save(f'crops/{o}.png')
for k in range(1,20,2):
    for side in 'ab':
        mont([f'r{k:02d}{side}',f'r{k+1:02d}{side}'] if k<19 else [f'r19{side}'],f'M{k:02d}{side}')
