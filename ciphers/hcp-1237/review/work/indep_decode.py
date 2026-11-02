"""Reviewer's independent decoder for HCP1237. Run: python3 -I indep_decode.py (from review/work)"""
import difflib, re, unicodedata, collections
KEY=dict(zip('=#6(/+q\\!L$~WN&F)Txyz^',list('abcdfghijklmnorstuyzv')))
KEY['\\']='h'
KEY.update({'=':'a','#':'e','6':'b','(':'c','/':'d','+':'f','q':'g','!':'i','L':'j','$':'k','~':'l','W':'m','N':'n','&':'o','F':'r',')':'s','T':'t','x':'u','^':'v','y':'y','z':'z','?':'?'})
mine={}
for l in open('my_signs.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,b=l.split(); mine[a]=''.join(KEY[c] for c in b)
theirs={}
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,*t=l.split(); theirs[a]=''.join('?' if x=='X?' else x.split(':')[0].lower() for x in t)
bad=[k for k in theirs if theirs[k]!=mine.get(k)]
print('rows',len(theirs),'mismatch',bad)
for k in bad: print(k,mine.get(k),theirs[k])
lit=''.join(mine[k] for k in mine)
print('letters',len(lit),collections.Counter(lit).most_common())
print('unused key letters',set('abcdefghijklmnoprstuvyz')-set(lit))
n=open('../../work/normalized.txt',encoding='utf-8').read().lower().replace('over the stamp:','')
s=''.join(c for c in unicodedata.normalize('NFD',n) if c.isalpha())
print('normalized-vs-literal edits:')
for op,a,b,c,d in difflib.SequenceMatcher(None,lit,s,autojunk=False).get_opcodes():
    if op!='equal': print(' ',op,repr(lit[max(0,a-6):a]),repr(lit[a:b]),'->',repr(s[c:d]),repr(lit[b:b+6]))
