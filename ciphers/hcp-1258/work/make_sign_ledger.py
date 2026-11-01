"""One-off: rewrites ledger-opus.txt (letter labels) into ledger-signs.txt (sign-class tokens).
Round 2 corrections are applied here: row 28 gains the written a; row 29 tail is read."""
import os
H = os.path.dirname(os.path.abspath(__file__))
C = {'A':'BAR2','B':'SIX','C':'LBOWL','D':'TICK','E':'BAR3','F':'CROSS','G':'GLOOP','H':'TALL','I':'CURVE','J':'INVT',
     'K':'SECT','L':'WAVE','M':'STROKE3','N':'STROKE2','O':'LOOP','R':'FLIKE','S':'RBOWL','T':'GAMMA','U':'XPLAIN','V':'CHEV',
     'Y':'DESC','Z':'XTAIL','GY':'LOOPDESC','TY':'JOINTY','CS':'OPPBOWL'}
ACC = {'Á':('A','a'),'É':('E','a'),'Ö':('O','d'),'Ü':('U','d'),'Ű':('U','dd'),'Ó':('O','a')}
def conv(t):
    if t.isdigit() or t == '.': return t
    if t.startswith('['): return '[' + conv(t[1:-1]) + ']'
    if t in ACC:
        b, a = ACC[t]; return C[b] + ':' + a
    return C[t]
out = ['# HCP1258 sign ledger, round 2. One token per written sign, named by the shape class seen on the card (key table in decode_opus.py and SOLUTION.md).',
       '# Hand transcription from enlarged crops of work/hires/*_adr.jpg, not OCR, not blind. [X] = sign hidden by tear or smear. :a acute, :d dots, :dd double mark, visible on the card only.',
       '# Row 29 tail: second LOOP is overinked and may hide a sign; CROSS has a dot beside it (the . token).']
for line in open(os.path.join(H, 'ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *t = line.split()
    if lab == '28':
        assert t[-3:] == ['H','O','GY'] and t[-4] == 'L'; t.insert(-3, 'A')
    if lab == '29':
        i = t.index('?1'); assert t[i:i+2] == ['?1','?2']; t[i:i+2] = ['O','O']
        i = t.index('?X'); t[i:i+1] = ['F','.']
    out.append(lab + ' ' + ' '.join(conv(x) for x in t))
open(os.path.join(H, 'ledger-signs.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
