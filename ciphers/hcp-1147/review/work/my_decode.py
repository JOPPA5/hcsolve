import re,collections,sys
ROOT='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1147/'
T=lambda s,lets:dict(zip(s.split(),lets.split()))
K=T("0 0, 1 1. 1: 1' ·1 :1 1, 9","o ö i a e á u ü b p")
K|=T("2, 2. 3 3, 3. 4 4, 4. 5 5, 6 6, 6. 7 7, 7. 8 8, 8. 9,","cs é d r v f g gy h l j n ny k s sz m t ty z")
mine={};cnt=collections.Counter()
for l in open(ROOT+'review/work/my_reading.txt',encoding='utf8'):
    if l[0]=='#':continue
    lab,*toks=l.split()
    mine[lab]=toks; cnt.update(t for t in toks if not t.endswith('!'))
    print(lab.ljust(4),''.join(t[:-1] if t.endswith('!') else '['+'?'+']' if t=='?' else K[t] for t in toks))
print('my tokens',sum(cnt.values()),'distinct',len(cnt))
print(sorted(cnt.items(),key=lambda x:-x[1]))
# solver transcription, stripped of words/annotations
diffs=0;tot=0
for l in open(ROOT+'work/transcription.txt',encoding='utf8'):
    if l[0]=='#' or not l.strip():continue
    lab,body=l.split(None,1)
    s=[]
    for t in body.replace('|',' ').split():
        if t=='=':continue
        if t[0]=='{': s.append(t[1:-1]+'!');continue
        s.append(t)
    m=mine[lab]
    if len(s)!=len(m): print('LEN',lab,len(s),len(m))
    for i,(a,b) in enumerate(zip(s,m)):
        tot+=1
        if a!=b: diffs+=1; print('DIFF',lab,i,'solver',a,'me',b)
print('compared',tot,'diffs',diffs)
