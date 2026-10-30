import json
M={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
lines=json.load(open('work/lines.json'))
def cls(d):
  w=d['x1']-d['x0']+1;h=d['y1']-d['y0']+1
  if w<=4 and h<=4: return 'd'
  if h>=5 and w<=11 and d['n']>=16: return 'B'
  if w<=4: return 'd'
  if h>=5 and w>=12: return 'M'
  if w<=11: return 'S'
  return 'L'
out=[]
for i,L in enumerate(lines):
  if i==0: L=[d for d in L if d['x0']>78]
  s=''.join(cls(d) for d in L)
  out.append(s)
  # decode
  txt='';cur=''
  for ch in s+'d':
    if ch in 'SL?M': cur+={'S':'.','L':'-','?':'?','M':'M'}[ch]
    else:
      if cur: txt+=M.get(cur,'['+cur+']'); cur=''
      if ch=='B': txt+=' '
  print(i+1,s);print('   ',txt)
json.dump(out,open('work/auto_marks.json','w'))
