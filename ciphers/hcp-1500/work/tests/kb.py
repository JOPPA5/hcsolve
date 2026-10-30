rows=['1234567890','qwertyuiop','asdfghjkl','zxcvbnm']
t='abc ly xuder comde 13guf h lz kncv 13g4hs pne pnvvx cn mnyo'
pos={c:(r,i) for r,row in enumerate(rows) for i,c in enumerate(row)}
for dr,dc in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]:
  o=''
  for c in t:
    if c in pos:
      r,i=pos[c]; r2,i2=r+dr,i+dc
      o+= rows[r2][i2] if 0<=r2<4 and 0<=i2<len(rows[r2]) else '?'
    else: o+=c
  print(dr,dc,o)
