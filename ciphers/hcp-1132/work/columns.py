# Assign marks to columns (with slant correction), classify, print gaps.
import json,sys
c=json.load(open('work/comps.json'))
SL=0.008
for o in c:
    o['h']=o['y1']-o['y0']+1; o['w']=o['x1']-o['x0']+1
    o['xp']=o['x']-SL*o['y']
c=[o for o in c if o['h']<200]
CEN=[92,166,227,287,358,430,499,579,648,721,793,872,947,1021,1092,1171,1252,1328,1405,1475]
cols=[[] for _ in CEN]
for o in c:
    d=[abs(o['xp']-(x-SL*1100)) for x in CEN]
    cols[d.index(min(d))].append(o)
res=[]
for i,col in enumerate(cols):
    col.sort(key=lambda o:o['y'])
    print(f"col {i} xp~{round(sum(o['xp'] for o in col)/len(col))} n={len(col)}")
    prev=None; line=[]
    for o in col:
        if o['w']>o['h']*1.6 and o['w']>18: sym='h'
        elif o['h']<25: sym='.'
        else: sym='-'
        gap=None if prev is None else o['y0']-prev['y1']
        o['sym']=sym;o['gap']=gap
        line.append(f"{'' if gap is None else '['+str(gap)+'] '}{sym}{o['h']}@{o['y0']}")
        prev=o
    print('   '+' '.join(line))
    res.append([dict(sym=o['sym'],gap=o['gap'],y0=o['y0'],y1=o['y1'],x=o['x'],h=o['h'],w=o['w']) for o in col])
json.dump(res,open('work/columns.json','w'))
