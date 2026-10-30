# Independent decoder (reviewer). Strokes-based: a token names which sides are present.
import sys
# grid positions (row, col) -> sides present in standard pigpen (# grid)
# cell at row r col c has: top if r>0, bottom if r<2, left if c>0, right if c<2
def sides(r,c):
    s=set()
    if r>0:s.add('T')
    if r<2:s.add('B')
    if c>0:s.add('L')
    if c<2:s.add('R')
    return frozenset(s)
name={'BR':'BR','B':'BLR','BL':'BL','R':'TBR','C':'TBLR','L':'TBL','TR':'TR','T':'TLR','TL':'TL'}
cell={}
for r in range(3):
  for c in range(3):
    cell[sides(r,c)]=r*3+c
def dec(t):
  if t in '|&,.?-~': return {'|':' '}.get(t,t)
  t=t.lstrip('*')
  if t.startswith('NOKEY:'): return '<'+t[6:]+'>'
  if '/' in t: return '['+'/'.join(dec(x) for x in t.split('/'))+']'
  sh,n=t[:-1],int(t[-1])
  i=(n-1)*9+cell[frozenset(name[sh])]
  return chr(65+i) if i<26 else '#'
for l in open(sys.argv[1]):
  if l.strip() and not l.startswith('#'):
    print(''.join(dec(x) for x in l.split()))
