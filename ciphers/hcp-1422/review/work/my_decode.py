import sys, collections, re
# key retyped by reviewer from the solution table (independent of work/key.json)
K = {':':'A','2':'B','//':'C','+':'D','#':'E','~':'F','.':'G','i':'H','!':'I','n':'K','u':'L',
     '=':'M','-.':'N','O':'O','p':'P',',':'R','v':'S','t':'T','\\':'U','^':'V','N':'W','>':'Y'}
P = {'{question}':'?','{punct}':'/','{comma}':',','{stop}':'.'}
cnt = collections.Counter(); out=[]
for line in open(sys.argv[1]).read().splitlines():
    ws=[]
    for w in line.split(' / '):
        s=''
        for t in w.split():
            r = t.strip('[]')
            if t in P: s+=P[t]; continue
            if r not in K: s+='?'; print('UNKNOWN', t); continue
            cnt[r]+=1; s+= K[r].lower() if t.startswith('[') else K[r]
        ws.append(s)
    out.append(' '.join(ws))
print('\n'.join(out)); print(sum(cnt.values()), 'glyphs;', len(cnt), 'classes used; unused:', set(K)-set(cnt))
print(sorted(((K[k],v) for k,v in cnt.items()), key=lambda x:-x[1]))
