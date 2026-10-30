"""Independent review decoder for HCP1297. Own key table written from the SOLUTION key description;
does not import the solver's script. Reads the solver ledger, applies reviewer corrections with --fix."""
import sys, unicodedata
L='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1297/work/ledger-opus.txt'
K={'A':'a','6':'b','CS':'cs','D':'d','E':'e','+':'f','G':'g','GY':'gy','H':'h','P':'p','I':'i','J':'j','K':'k','L':'l','M':'m',
   'N':'n','O':'o','F':'r',')':'s','T':'t','X':'u','V':'v','Z':'z','S':'s','/':'?','|':'·'}
fix='--fix' in sys.argv
n=0; rows={}
for ln in open(L,encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    lab,*t=ln.split()
    if fix and lab=='20': t.append('L')
    if fix and lab=='25': i=t.index('O:d'); assert t[i-1]=='+'; t[i-1]='J'
    s=''
    for x in t:
        b,_,a=x.partition(':'); c=K[b]
        s+= {'o':'ö','u':'ü'}[c] if a else c
    rows[lab]=s; n+=len(t)
    print(lab,s)
print(n,'signs'); 
import collections
c=collections.Counter(x.partition(':')[0] for ln in open(L,encoding='utf-8') if not ln.startswith('#') and ln.strip() for x in ln.split()[1:])
print(sorted(c.items(),key=lambda kv:-kv[1]))
