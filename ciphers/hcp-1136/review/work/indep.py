# independent decoder: own key typed from hcp-1174 table + 3 new signs, no reading comparison
K=dict(zip("0 0, 1 1. 1: 1' :1 1, 2, 2. 3 3, 3. 4, 5 5, 6, 7 7, 7. 8 8, 9 9,".split(),
 "o ö i a e á ü b cs é d r v g h l n k s sz m t p z".split()))
K.update({'4':'f?','6':'j*','6.':'ny*','4.':'gy*'})
for l in open('../../work/transcription.txt',encoding='utf8'):
    if l[0]=='#' or not l.strip(): continue
    ct=l.split('|')[0]
    print(' '.join(''.join((t[1:].upper() if t[0]=='=' else K.get(t.strip('[]'),'#'+t)) for t in w.split()) for w in ct.split('/')))
