# Re-key the three rows I re-read from the pixels (own strings, family values) and test claims of SOLUTION.md.
import re,unicodedata,subprocess
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1246/'
L=[l.split() for l in open(base+'work/ledger.txt',encoding='utf8') if l.strip() and not l.startswith('#')]
row={l[0]:''.join(t.strip('[]:').lower() for t in l[1:] if t!='.') for l in L}
full=''.join(row.values())
for w,n in [('hogy',9),('edesem',4),('nem',7),('ijesmit',2),('merttudom',2)]:
    print(w,'claimed',n,'found',full.count(w))
out=subprocess.run(['python3','-I',base+'work/decode.py'],capture_output=True,text=True).stdout
sol=open(base+'SOLUTION.md',encoding='utf8').read()
miss=[]
for lab,t in re.findall(r'^\s*(\d\d|S\d) (\S+)$',out,re.M):
    if t not in sol and lab[0]!='S': miss.append(lab)
print('output rows absent from SOLUTION.md literal block:',miss)
mine={'12':'esnemhiszelijesmittanacso','27':'nekelmondanommaganakhogymegegylahjatsemolvas','28':'taavatatlakezcsakenistenveleedesemaboldogvi'}
for k,v in mine.items():
    print(k,'ledger',row[k]);print(k,'mine  ',v)
