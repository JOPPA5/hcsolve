# independent automatic classification per line; line geometry (y at left/right end) taken from work/lines.json
import json,re
from PIL import Image
im=Image.open('source/address-large.jpg').convert('RGB')
L=json.load(open('work/lines.json'))
tr={}
for l in open('work/transcription.txt'):
    m=re.match(r'L(\d+): (.*)',l)
    if m: tr[int(m.group(1))]=m.group(2).strip()
def tok(t): return re.sub(r'\s+',' ',t.replace('/',' / ')).strip()
for i,line in enumerate(L,1):
    a=min(line,key=lambda d:d['cx']); b=max(line,key=lambda d:d['cx'])
    x0=int(a['x0'])-2; x1=int(b['x1'])+3
    def yc(x): return a['cy']+(b['cy']-a['cy'])*(x-a['cx'])/max(1,(b['cx']-a['cx']))
    cols=[]
    for x in range(x0,x1):
        y=int(round(yc(x)))
        d=[yy for yy in range(y-4,y+5) if im.getpixel((x,yy))[0]<140]
        cols.append(len(d))
    runs=[];k=0
    while k<len(cols):
        if cols[k]:
            j=k
            while j<len(cols) and cols[j]: j+=1
            runs.append((x0+k,j-k,max(cols[k:j])));k=j
        else:k+=1
    s='';cur=''
    for x,w,h in runs:
        if h>=5 and w>=5 and w<=12: s+=cur+' / ';cur='';continue
        if w<=3: 
            if cur: s+=cur+' ';cur=''
            continue
        cur+='.' if w<=12 else ('-' if w>=15 else '?')
    s+=cur
    auto=tok(s); man=tok(tr[i])
    flag='' if auto.replace(' ','')==man.replace(' ','') else '  <<DIFF'
    print(f'L{i:02d} man : {man}\n    auto: {auto}{flag}')
