from pathlib import Path
import unicodedata,json
B=Path(__file__).resolve().parent;R=B.parents[1]
def row(letter):
 n=ord(letter.lower())-97;assert 0<=n<26;return n if n<22 else n-1

def enc(plain,key):
 w=len(key);block=25*w;assert len(plain)%block==0;order=sorted(range(w),key=lambda c:(key[c],c));out=[]
 for at in range(0,len(plain),block):
  text=plain[at:at+block];columns=[list(text[c::w])for c in range(w)];rotated=[]
  for c,col in enumerate(columns):
   shift=row(key[c]);rotated.append(col[-shift:]+col[:-shift]if shift else col)
  out.extend(rotated[c][r]for r in range(25)for c in order)
 return ''.join(out)

def dec(cipher,key):
 w=len(key);block=25*w;assert len(cipher)%block==0;order=sorted(range(w),key=lambda c:(key[c],c));plain=['']*len(cipher)
 for at in range(0,len(cipher),block):
  for i in range(block):
   r,rank=divmod(i,w);c=order[rank];pr=(r-row(key[c]))%25;plain[at+pr*w+c]=cipher[at+i]
 return ''.join(plain)
def normalize(text):return ''.join(c for c in unicodedata.normalize('NFD',text.lower())if 'a'<=c<='z')
def model():
 tables={};floors={}
 for n in range(2,6):
  lines=(B/f'model{n}.tsv').read_text().splitlines();floors[n]=float(lines[0].split()[1]);tables[n]={k:float(v)for k,v in(line.split()for line in lines[1:])}
 return tables,floors
def score(text,tables,floors):
 total=0.;windows={}
 for n,w in [(2,.2),(3,.15),(4,.4),(5,.8)]:
  windows[n]=0
  for i in range(len(text)-n+1):
   gram=text[i:i+n]
   if all('a'<=c<='z'for c in gram):total+=w*tables[n].get(gram,floors[n]);windows[n]+=1
 return total,windows
