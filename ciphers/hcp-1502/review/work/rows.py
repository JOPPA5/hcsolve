import json
C=json.load(open('comps.json'))
C=[dict(x0=c[0],x1=c[1],y0=c[2],y1=c[3],cy=c[4],a=c[5]) for c in C]
starts=sorted([c for c in C if c['x0']<75 and c['y0']>40],key=lambda c:c['cy'])
used=set();rows=[]
for s in starts:
  if id(s) in used: continue
  row=[s];used.add(id(s));x=s['x1'];y=s['cy'];slope=0.0
  while True:
    cand=[c for c in C if id(c) not in used and x-2<=c['x0']<=x+40 and abs(c['cy']-(y+slope*(c['x0']-x)))<=4]
    if not cand: break
    c=min(cand,key=lambda c:c['x0']); used.add(id(c))
    if len(row)>3: slope=0.8*slope+0.2*((c['cy']-row[-4]['cy'])/max(1,c['x0']-row[-4]['x0']))
    row.append(c); x=c['x1']; y=c['cy']
  if len(row)>=5: rows.append(row)
def cls(c):
  L=c['x1']-c['x0']+1; h=c['y1']-c['y0']+1
  if h>=6 and L<=14: return 'B'
  if L<=4: return 'p'
  if L<=17: return '.'
  return '-'
for r in rows:
  if r[0]["cy"]>585: print([(c["x0"],c["x1"],round(c["cy"])) for c in r if c["x0"]>540])
  print('y%3d x%3d-%3d '%(r[0]['cy'],r[0]['x0'],r[-1]['x1'])+''.join(cls(c) for c in r))
M={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
print('---auto decode---')
for r in rows:
  s=''.join(cls(c) for c in r); out='';cur=''
  for ch in s+'p':
    if ch in '.-': cur+=ch
    else:
      if cur: out+=M.get(cur,'['+cur+']'); cur=''
      if ch=='B': out+=' '
  print('y%3d %s'%(r[0]['cy'],out))
