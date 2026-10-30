"""hcp-1322: check hashes, print sign statistics, find runs shared with sister Wooster cards. Run: python3 -I ciphers/hcp-1322/work/compare.py"""
import hashlib,re,pathlib,collections
R=pathlib.Path('ciphers')
H={'source/picture-large.jpg':'1ebcbef5fae5dadeba426700b002118549ed6c487e55e827a4d08dd5d9895f93','source/address-large.jpg':'fb88b06e940f5e1c2ed0f62c24e8f43b4864bb7c2302a91123f9f0dad78bdbcb','work/hires/pc_hcp_3_pic.JPG':'87d984b57d93a2da2782bba605918afc00489bcde60a681b985966289f73255f','work/hires/pc_hcp_3_adr.JPG':'bc32a800b0037f6f6b409fcc866656506c951be35b6f197dbf9eed00c2152d31'}
for f,h in H.items():
    assert hashlib.sha256((R/'hcp-1322'/f).read_bytes()).hexdigest()==h,f
print('hashes ok')
def load(n):
    t=[l for l in (R/f'hcp-{n}/work/transcription.txt').read_text().splitlines() if not l.startswith('#')]
    t=re.sub(r'\[.*?\]',' ',' '.join(t)); return ''.join(re.findall(r'\b[A-Z]\b',t))
me=load(1322); print(len(me),me); c=collections.Counter(me); print(c.most_common())
print('E',c['E'],'T',c['T'])
for n in (1334,1335,1336,1337,1338,1339):
    try: s=load(n)
    except Exception as e: print(n,'unavailable'); continue
    runs=sorted({me[i:j] for i in range(len(me)) for j in range(i+3,len(me)+1) if me[i:j] in s},key=len,reverse=True)
    runs=[r for r in runs if not any(r in q and r!=q for q in runs)]
    print(n,len(s),s,'shared',runs)
