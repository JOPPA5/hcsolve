"""Independent re-decode of the HCP1269 ledger (reviewer). Own key table typed from the
family description; applies the reviewer's pixel corrections and shows the effect.
Run from repo root: python3 -I ciphers/hcp-1269/review/work/verify.py"""
import os,re
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
key={c:c.lower() for c in 'ADEGIJKLMNOTVYZ'}
key.update({'6':'b','+':'f','H':'h','F':'r',')':'s','X':'u','CS':'cs','Z?':'z','??':'?','^':'','.':'.'})
acc={'O:diaeresis':'ö','O:dbl':'ő','X:diaeresis':'ü'}
rows={}
for l in open(os.path.join(D,'work/ledger-opus.txt'),encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,*t=l.split(); rows[a]=t
dec=lambda t:''.join(acc[x] if x in acc else key[x] for x in t)
lit={a:dec(t) for a,t in rows.items()}
all_=''.join(lit[a] for a in rows)
print('rows',len(rows),'signs',sum(len(t) for t in rows.values()),'unknown tokens',sum(t.count('??') for t in rows.values()))
for w in ('hogy','edesem','sora','becses'): print(w,all_.count(w))
# reviewer's corrections: row -> (old, new)
fix={'15':('egeszenek','egesznek'),'23':('ahezal','ahafel'),'28':('csakmerot','csakmarot'),
     '30':('vanekkozt','vanakőzt'),'S5':('vese','vesse'),'05':('onog','onőg'),'32':('le{z|f}','lez')}
for r,(o,n) in fix.items():
    s=lit[r].replace('z?','z')
    print(r,'ledger has',o,':',o.replace('{z|f}','z') in s,'->',s.replace(o.replace('{z|f}','z'),n))
out=open(os.path.join(D,'SOLUTION.md'),encoding='utf-8').read()
m=[a for a in lit if a.isdigit() and lit[a].replace('z?','') and lit[a] not in out and a!='32']
print('rows not found verbatim in SOLUTION.md:',m)
