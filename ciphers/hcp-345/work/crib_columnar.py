from pathlib import Path
p=Path(__file__).parent;g=p.joinpath('transcription.txt').read_text().split()
phrases=['effektivnelei','effektivneleiposielamekurierom','effektivneleivamposielamekurierom','effektivneleivamposlemekurierom','leiposielamekurierom']
def compatible(c,w,phrase,start):
 h=len(c)//w;chunks=[c[j*h:(j+1)*h] for j in range(w)]
 allowed=[]
 for col in range(w):
  tests=[(i//w,phrase[i-start]) for i in range(start,start+len(phrase)) if i%w==col]
  allowed.append([j for j,s in enumerate(chunks) if all(s[r]==letter for r,letter in tests)])
 assign={}
 def match(col,seen):
  for j in allowed[col]:
   if j in seen:continue
   seen.add(j)
   if j not in assign or match(assign[j],seen):assign[j]=col;return True
  return False
 if not all(match(col,set()) for col in sorted(range(w),key=lambda c:len(allowed[c]))):return None
 cols=['']*w
 for j,col in assign.items():cols[col]=chunks[j]
 return ''.join(cols[j][r] for r in range(h) for j in range(w))
cases={f'omit-{i+1}':''.join(v for j,v in enumerate(g) if j!=i) for i in range(13)}
pt='effektivneleivamposielamekurieromprosimvaspotvrdteprijempenazix'[:60];key=list(range(19,-1,-1));cases['positive-single20']=''.join(pt[j::20] for j in key)
for label,c in cases.items():
 for phrase in phrases:
  hits=[]
  for w in [2,3,4,5,6,10,12,15,20]:
   for start in range(len(c)-len(phrase)+1):
    t=compatible(c,w,phrase,start)
    if t is not None:hits.append((w,start,t))
  print(label,phrase,'compatible placements',len(hits),'examples',hits[:2])
