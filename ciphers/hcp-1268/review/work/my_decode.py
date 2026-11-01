"""Reviewer's independent decode: own shape ledger + key restated by the reviewer; diffs against solver's ledger."""
import os,re,sys
D=os.path.dirname(os.path.abspath(__file__))
K={'2':'a','3':'e','6':'b','Y':'d','V':'v','S':'s','C':'g','B':'cs','J':'j','O':'o','Q':'ő','L':'l','N':'n','M':'m','K':'k','T':'t','R':'r','I':'i','H':'h','P':'p','Z':'z','U':'ü','G':'gy','F':'f','.':'.','meg':'[meg]','hi':'[hi]',
 '?O+n?':'on?','?3':'{e}','?2':'{a}','?C':'c'}
my={}
for l in open(D+'/my_ledger.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    a,*t=l.split(); my[a]=''.join(K[x] for x in t)
sol={}
M={'GY':'gy','CS':'cs',"I'":'i','O:dia':'ő','U:dia':'ü','{a}':'{a}','{c|k}':'c','.':'.','meg':'[meg]','hi':'[hi]'}
for l in open(D+'/../../work/ledger.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    a,*t=l.split(); sol[a]=''.join(M.get(x,x.lower()) for x in t)
n=0
for a in my:
    f='' if my[a]==sol[a] else '   <-- DIFF solver: '+sol[a]
    n+=my[a]!=sol[a]
    print(a,my[a],f)
print('rows differing:',n,'of',len(my))
