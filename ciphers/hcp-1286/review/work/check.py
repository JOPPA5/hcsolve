"""Independent decode of the ledger with the hcp-1216 table, then align with the normalized text."""
import re,unicodedata,difflib
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1286/work/'
K=dict(zip('ABCDEFHIJKLMNOTUVXYZG','a b c d e r h i j k l m n o t u v u y z g'.split()))
K.update({'6':'b',')':'s','+':'f','GY':'gy','CS':'cs','G?':'g'})
def d(t):
    t=t.strip('[]').split(':')[0]
    return K.get(t,'')  # marks, numerals, stray strokes dropped
rows=[l.split() for l in open(W+'ledger-rev2.txt',encoding='utf-8') if l.strip() and l[0]!='#']
lit=''.join(d(t) for r in rows for t in r[1:])
n=open(W+'normalized-rev2.txt',encoding='utf-8').read()
n=n.replace('Under the stamp:','')
n=re.sub(r'\{[^}]*\}','kulvesben',n)
n=n.replace('[','').replace(']','')
n=''.join(c for c in unicodedata.normalize('NFD',n.lower()) if c.isalpha()).replace('p','h')
n=n.replace('w','')
print(len(lit),'signs(letters) ledger;',len(n),'normalized')
for op,a,b,c,e in difflib.SequenceMatcher(None,lit,n,autojunk=False).get_opcodes():
    if op!='equal': print(op,repr(lit[max(0,a-8):a]),'|',repr(lit[a:b]),'->',repr(n[c:e]),'|',repr(lit[b:b+8]))
hid=sum(t.startswith('[') for r in rows for t in r[1:]); tot=sum(len(r)-1 for r in rows)
print('tokens',tot,'hidden',hid,round(100*hid/tot,1),'%')
