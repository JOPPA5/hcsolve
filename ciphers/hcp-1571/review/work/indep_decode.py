import json,sys
K={"1":"Y","2":"U","3":"O","4":"I","5":"E","6":"A","8":"L","q":"Z","g":"K","f":"V","h":"R","t":"D","r":"H","c":"S","s":"C","n":"M","m":"N","p":"B","b":"P","d":"T","y":"J","H":"CH"}
d=json.load(open(sys.argv[1]))
bad=0;tot=0
for r in d['rows']:
    out=''.join(K.get(ch,ch) for ch in r['cipher'])
    n=sum(1 for ch in r['cipher'] if ch in K); tot+=n
    ok = out==r['plaintext'] and n==r['active_units']
    unk=[ch for ch in r['cipher'] if not (ch in K or ch in " .,?!-")]
    if not ok or unk: bad+=1
    print(r['id'], 'OK' if ok else 'MISMATCH', n, unk, out)
print('total units',tot,'bad rows',bad)
