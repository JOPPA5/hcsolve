from pathlib import Path
import json
B=Path(__file__).resolve().parent

def enc(text,key):
 width=len(key);rows=[list(text[i:i+width])for i in range(0,len(text),width)];assert sorted(key)==list(range(width));return ''.join(row[col]for col in key for row in rows if col<len(row))
def inverse(text,key):
 n=len(text);width=len(key);shape=[min(width,n-i)for i in range(0,n,width)];columns={};at=0
 for col in key:
  length=sum(col<r for r in shape);columns[col]=text[at:at+length];at+=length
 assert at==n;return ''.join(columns[col][row]for row,size in enumerate(shape)for col in range(size))
def check(keys,p,c):
 x=p
 for k in keys:x=enc(x,k)
 y=c
 for k in keys[::-1]:y=inverse(y,k)
 return dict(matches=sum(a==b for a,b in zip(x,c)),full_observed_reencryption_exact=x==c,full_observed_inverse_exact=y==p,predicted_ciphertext=x,observed_inverse=y)
if __name__=='__main__':
 cases=[]
 for j in range(2):
  p,c=(B/f'control{j}.txt').read_text().split()
  for name in [f'control{j}-result.txt',f'middle-control{j}-result.txt',f'coordinate-control{j}-result.txt',f'hybrid-control{j}-result.txt',f'fragment-control{j}-result.txt']:
   path=B/name
   if not path.exists():continue
   lines=path.read_text().splitlines();keys=[list(map(int,x.split()))for x in lines[1:4]];r=check(keys,p,c);assert r['matches']==int(lines[0].split()[0]);cases.append(dict(file=name,control=j,**r))
  for name in [f'cp-lns-control{j}.json',f'error-best{j}.json',f'hard-unique-control{j}.json']:
   path=B/name
   if not path.exists():continue
   r=json.loads(path.read_text())
   if'keys'in r:cases.append(dict(file=name,control=j,**check(r['keys'],p,c)))
 for tr in json.loads((B/'equal17-control-truth.json').read_text()):
  p,c=tr['p'],tr['c'];name=f"coordinate17-{tr['label']}-result.txt";path=B/name
  if path.exists():
   lines=path.read_text().splitlines();keys=[list(map(int,x.split()))for x in lines[1:4]];r=check(keys,p,c);assert r['matches']==int(lines[0].split()[0]);cases.append(dict(file=name,control=tr['label'],**r))
 (B/'independent-candidate-verification.json').write_text(json.dumps(cases,indent=2)+'\n');print('independently verified',len(cases),'candidate key sets; complete witnesses',sum(r['full_observed_reencryption_exact']for r in cases))
