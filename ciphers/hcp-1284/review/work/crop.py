from PIL import Image
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-74_adr.jpg').convert('RGB')
S=1.7225
rows=[(55,115),(118,178),(182,245),(240,305),(318,378),(388,448),(442,495),(512,568),(575,642),(645,702),(705,772),(775,832),(835,898),(893,962),(962,1038),(1032,1092),(1088,1165),(1130,1210)]
def c(x0,x1,y0,y1,s=3): 
    r=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S))); return r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS)
for g in range(0,18,3):
  for side,(x0,x1) in (('L',(55,450)),('R',(430,860))):
    parts=[c(x0,x1,*rows[i]) for i in range(g,g+3)]
    W=max(p.width for p in parts);H=sum(p.height+10 for p in parts)
    o=Image.new('RGB',(W,H),'white');y=0
    for p in parts:o.paste(p,(0,y));y+=p.height+10
    o.save(f'review/work/crops/rows{g+1:02d}{side}.png')
c(1520,1800,120,400,3).save('review/work/crops/stamp.png')
c(55,700,1130,1210,3).save('review/work/crops/r18a.png')
c(650,1360,1120,1200,3).save('review/work/crops/r18b.png')
