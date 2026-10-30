import json,sys
from PIL import Image,ImageDraw
im=Image.open('source/address-large.jpg').convert('RGB')
lines=json.load(open('work/lines.json'));marks=json.load(open('work/auto_marks.json'))
Z=5
which=[int(a) for a in sys.argv[1].split(',')]
strips=[]
for li in which:
  L=lines[li-1]
  if li==1: L=[d for d in L if d['x0']>78]
  cy=sum(d['cy'] for d in L)/len(L)
  x0=max(30,int(min(d['x0'] for d in L))-6); x1=int(max(d['x1'] for d in L))+6
  for a,b in ([(x0,(x0+x1)//2+4),((x0+x1)//2-4,x1)]):
    cr=im.crop((a,int(cy)-9,b,int(cy)+9)).resize(((b-a)*Z,18*Z),Image.LANCZOS)
    canvas=Image.new('RGB',(cr.width,cr.height+22),'white');canvas.paste(cr,(0,0))
    dr=ImageDraw.Draw(canvas)
    for k,d in enumerate(L):
      if a<=d['cx']<b:
        dr.text(((d['cx']-a)*Z-3,cr.height+4),marks[li-1][k],fill='red')
    dr.text((2,2),str(li),fill='blue')
    strips.append(canvas)
W=max(s.width for s in strips);H=sum(s.height+6 for s in strips)
out=Image.new('RGB',(W,H),'white');y=0
for s in strips: out.paste(s,(0,y));y+=s.height+6
out.save(sys.argv[2])
