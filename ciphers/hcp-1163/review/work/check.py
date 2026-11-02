import re,collections
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1163/'
K=dict(zip("0 0, 1 1. 1: 1' :1 .1 1, 2 2, 2. 3 3, 3. 4 4, 4. 5 5, 6 6, 6. 7 7, 7. 8 8, 9 9,".split(),
 "o ö i a e á ü u b c cs é d r v f g gy h l j n ny k s sz m t p z".split()))
mine=[[*l.split()] for l in open(D+'review/work/my_transcription.txt') if l.strip() and l[0]!='#']
sol=[]
for l in open(D+'work/transcription.txt'):
    if l[0]=='#' or not l.strip(): continue
    sol.append([t for t in l.split(':',1)[1].replace('/',' ').split() if t not in '()'])
print('rows',len(mine),len(sol))
n=0;d=[]
for r,(a,b) in enumerate(zip(mine,sol)):
    if len(a)!=len(b): print('LEN',r,len(a),len(b))
    for i,(x,y) in enumerate(zip(a,b)):
        n+=1
        if x!=y: d.append((r,i,x,y))
print('compared',n,'diffs',len(d));print(d)
for a in mine: print(''.join(K[t] for t in a))
c=collections.Counter(t for a in mine for t in a); print(len(c),sum(c.values()));print(sorted(c.items(),key=lambda x:-x[1]))
s=' '.join(' '.join(a) for a in sol)
print('hogy count',s.count('5 0 4.'),'; 4. :',c['4.'],'; 2:',c['2'],'; 6:',c['6'],'; 6.:',c['6.'],'; 4:',c['4'])
