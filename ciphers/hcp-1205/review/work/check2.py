"""Reviewer round 2: rerun the command, compare with SOLUTION block; own key table; my own class reading of rows 24-26;
test which words the signs of row 25 allow. Run: python3 -I ciphers/hcp-1205/review/work/check2.py"""
import re,subprocess
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1205/'
out=subprocess.run(['python3','-I',D+'work/decode.py'],capture_output=True,text=True,cwd=D+'../..').stdout
blk=re.search(r'## Literal decipherment.*?```\n(.*?)```',open(D+'SOLUTION.md',encoding='utf-8').read(),re.S).group(1)
want=[l.strip() for l in blk.splitlines() if l.strip()]
got=[l.strip() for l in out.splitlines() if re.match(r'\s*(\d\d|U\d|S\d) ',l)]
print('rows',len(got),'identical',got==want, re.search(r'\d+ signs.*',out).group(0))
T={'C':'cs','G':'gy','Y':'y','H':'h','P':'p','N':'n','D':'h','M':'m','#':'{struck}','?':'?'}
mine=[];n=0
for l in open(D+'work/ledger.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    a,t=l.split(); mine.append(a+' '+''.join(T.get(c,c) for c in t)); n+=sum(c!='?' for c in t)
print('own table equal',mine==got,'signs',n)
import collections
c=collections.Counter(ch for l in open(D+'work/ledger.txt',encoding='utf-8') if l[0]!='#' and l.strip() for ch in l.split()[1])
print({k:c[k] for k in 'HPNDMYG5'})
print('row25 with tall+short = p:', got[24].replace('jonenek','jonepek'))
