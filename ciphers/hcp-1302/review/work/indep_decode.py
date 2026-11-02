"""HCP1302 review: independent decode. review/work/rows.txt = my own sign-class reading from crops
(tokens named by shape, not letters). Key = table in ciphers/hcp-1216/SOLUTION.md. Compares base letters
with the solver's ledger-rev2.txt (accents, ?, brackets stripped). Run: python3 -I review/work/indep_decode.py"""
import os, re, unicodedata, difflib
D=os.path.dirname(os.path.abspath(__file__))
KEY={'BB':'a','SIX':'b','LB':'c','LS':'d','BBB':'e','PLUS':'f','OLD':'g','HP':'h','DC':'i','IT':'j','SEC':'k','S5':'k',
     'WV':'l','SSS':'m','SS':'n','LOOP':'o','F':'r','RB':'s','GAM':'t','X':'u','CHV':'v','Y':'y','ZX':'z','CS':'cs','N2':'2','N0':'0','N6':'6','?':''}
def base(s):
    s=re.sub(r'[\[\]()?\-]','',s); s=unicodedata.normalize('NFD',s)
    return ''.join(c for c in s if c.isalpha() or c.isdigit())
led={}
for l in open(os.path.join(D,'../../work/ledger-rev2.txt'),encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    p=l.split(); led[p[0]]=base(''.join(p[1:]))
tot=diff=0
for l in open(os.path.join(D,'rows.txt')):
    if not l.strip() or l.startswith('#'): continue
    p=l.split(); lab=p[0]; dec=''.join(KEY[t] for t in p[1:]); s=led[lab]
    s_cmp=s
    tot+=len(dec); r=difflib.SequenceMatcher(None,dec,s_cmp).ratio()
    ops=[o for o in difflib.SequenceMatcher(None,dec,s_cmp).get_opcodes() if o[0]!='equal']
    diff+=sum(max(o[2]-o[1],o[4]-o[3]) for o in ops)
    print(f'{lab:>3} {dec}'+('' if not ops else '   <> '+s_cmp+'  '+str([(o[0],dec[o[1]:o[2]],s_cmp[o[3]:o[4]]) for o in ops])))
print('letters',tot,'differing',diff)
