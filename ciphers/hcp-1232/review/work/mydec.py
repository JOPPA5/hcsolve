"""Independent decoder: my own reading of the ledger tokens via a sign-name table built from the
HCP1216 table (not decode.py); reports letters by sign class and frequency."""
import sys,collections,re
SIGN={'A':'two bars','6':'six','C':'left bowl','D':'tick+long','E':'three bars','+':'upright cross','G':'loop desc','H':'tall+short','P':'tall+short','I':'crossed curve','J':'inv T','K':'section','L':'wave','M':'3 strokes','N':'2 strokes','O':'loop','O:':'loop dots','F':'F-like',')':'right bowl','T':'gamma','X':'plain cross','X:':'plain cross dots','S':'right bowl','B':'six','V':'chevron','Y':'low desc','Z':'crossed diag'}
L={'two bars':'a','six':'b','left bowl':'c','tick+long':'d','three bars':'e','upright cross':'f','loop desc':'g','crossed curve':'i','inv T':'j','section':'k','wave':'l','3 strokes':'m','2 strokes':'n','loop':'o','loop dots':'ö','F-like':'r','right bowl':'s','gamma':'t','plain cross':'u','plain cross dots':'ü','chevron':'v','low desc':'y','crossed diag':'z'}
c=collections.Counter();out=[]
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab,*t=l.split();s=''
    for x in t:
        r=x.strip('{}')
        if r.startswith('='): s+=r[1:].lower();continue
        if r=='#': s+='?';continue
        n=SIGN[r];c[n]+=1
        s+= ('H' if r=='H' else 'P' if r=='P' else L[n])
    out.append((lab,s));print(lab,s)
print(c.most_common(), sum(c.values()))
