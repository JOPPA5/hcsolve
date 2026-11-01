import re,subprocess
R='/Users/tomaspavuk/Desktop/hcsolve/'
o=subprocess.run(['python3','-I',R+'ciphers/hcp-1270/work/decode.py'],capture_output=True,text=True).stdout
rows=dict(re.findall(r'^\s*(\d\d) (\S+)$',o,re.M))
s=open(R+'ciphers/hcp-1270/SOLUTION.md').read()
b=s.split('```')[3]
cl={}
for m in re.finditer(r'(\d\d) (\S+)',b): cl[m.group(1)]=m.group(2)
print(len(rows),len(cl),[k for k in rows if rows[k]!=cl.get(k)])
t=''.join(rows[k] for k in sorted(rows)).replace('[','').replace(']','')
for w in ['hogy','edesem','ilet','mert','nincs']: print(w,t.count(w))
print(len(t))
import collections
n=open(R+'ciphers/hcp-1270/work/normalized.txt').read()
print('mert',n.lower().count('mert'), 'mer[t]',n.count('Mer[t]'))
