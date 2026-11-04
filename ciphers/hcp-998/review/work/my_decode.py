"""Reviewer's independent decode of hcp-998 (own sign names, own reading of the scan)."""
import sys, collections
KEY = {'loopb':'m','circ':'e','Hbar':'i','six':'n','vee':'s','box':'o','plus':'p','Iser':'h',
 'tri':'v','Tee':'l','pi':'l','slash':'d','tick':'d','ex':'a','kay':'k','zero':'f','cupU':'ü',
 'loopU':'ü','rho':'r','bar':'b','wave':'z','lam':'t','bsl':'c','dblu':'w','dash':'g','eps':'u','exU':'ä'}
LINES = """loopb circ Hbar six _ vee box plus Iser Hbar six — tri Hbar circ Tee circ six _
tri Hbar circ Tee circ six _ slash ex six kay _ zero cupU rho _ slash circ Hbar six circ six
Tee Hbar circ bar circ six _ bar rho Hbar circ zero , vee box bar ex Tee tick _
Hbar bsl Iser _ wave circ Hbar lam _ Iser ex bar circ _ vee bsl Iser rho circ Hbar =
bar circ _ Hbar bsl Iser _ slash Hbar rho . circ Hbar six vee lam dblu circ Hbar =
pi circ six _ vee circ Hbar _ wave exU rho lam Tee Hbar bsl Iser _ dash circ =
kay loopU vee vee lam _ loopb circ Hbar six _ Tee Hbar circ bar vee lam circ vee _
tri box six _ slash circ Hbar six circ rho _ lam rho . zero rho circ eps six slash Hbar six
loopb ex dash slash ex .""".split('\n')
out=''; cnt=collections.Counter(); n=0
for ln in LINES:
    toks=ln.split()
    for t in toks:
        if t in KEY: out+=KEY[t]; cnt[t]+=1; n+=1
        elif t=='_': out+=' '
        elif t=='=': pass
        else: out+=t+(' ' if t in '.,' else '')
    if toks[-1]!='=': out+=' '
print(' '.join(out.replace('—',' — ').split()))
print('letter signs:',n,'distinct:',len(cnt)); print(dict(cnt))
