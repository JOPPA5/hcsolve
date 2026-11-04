"""Reviewer's independent decoder for hcp-1183. Key written by the reviewer from own reading of the hi-res scan.
Usage: python3 -I review/work/indep_decode.py ciphers/hcp-1183/work/transcription.txt"""
import sys, collections
K = dict(SL='A', BS='B', X='C', XH='D', XV='E', O='F', OD='G', OH='H', OV='I', PL='L', HH='M', NN='N',
         Q='O', TL='P', BR='R', CUP='S', SQ='T', SQD='U', CAP='V', CAPD='W', Y='Y')
P = {'.': '.', ',': ',', "'": "'"}
assert len(set(K.values())) == len(K)
n = 0; cnt = collections.Counter()
for ln in open(sys.argv[1], encoding='utf-8'):
    ln = ln.strip()
    if not ln or ln.startswith('#'): continue
    out = []
    for w in ln.split(' / '):
        s = ''
        for t in w.split():
            if t in K: s += K[t]; n += 1; cnt[t] += 1
            elif t in P: s += P[t]
            else: sys.exit('UNKNOWN ' + t)
        out.append(s)
    print(' '.join(out))
print('cipher signs:', n, 'distinct:', len(cnt))
print(sorted(cnt.items(), key=lambda x: -x[1]))
