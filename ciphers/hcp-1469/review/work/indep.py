# Independent reviewer decoder for hcp-1469: own key table, own parser, word check, sign counts
import sys, collections
K = dict(zip("O3C).FGH:JKLMVQPX72TU>Y", "abcdefghijklmnopqrstuvy"))
t = open(sys.argv[1]).read().splitlines()
out=[]; cnt=collections.Counter()
for ln in t:
    if not ln.strip() or ln.startswith('#'): continue
    lab, rest = ln.split(' ',1)
    ws=[]
    for w in rest.split(' / '):
        s=''
        for tok in w.split():
            cnt[tok]+=1
            s += 'w' if tok=='V=w' else ('r' if tok=='V=r?' else K[tok])
        ws.append(s)
    out.append((lab,' '.join(ws)))
words=set(x.strip().lower() for x in open('/usr/share/dict/words'))
allw=[w for _,l in out for w in l.split()]
print('\n'.join(f'{a} {b}' for a,b in out))
print('signs:',sum(cnt.values()),'words:',len(allw))
print('not in dict:',sorted(set(w for w in allw if w not in words)))
print('sign counts:',dict(sorted(cnt.items(),key=lambda x:-x[1])))
