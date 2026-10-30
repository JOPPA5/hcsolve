# Independent reviewer decoder for hcp-1503 (own Morse table, own parser).
import sys, re, datetime
T = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()))
R = {v:k for k,v in T.items()}
txt = open(sys.argv[1]).read()
out=[]; n_el=0; n_let=0
for line in txt.splitlines():
    if not line.strip() or line.lstrip().startswith('#'): continue
    lab, body = line.split(':',1)
    ws=[]
    for w in body.split('/'):
        s=''
        for t in w.split():
            if t=='(.)': s+='[.]'; continue
            if t=='~': s+='--'; continue
            assert re.fullmatch(r'[.-]+',t), t
            n_el+=len(t); n_let+=1; s+=R[t]
        ws.append(s)
    out.append(' '.join(ws))
print('\n'.join(out)); print('elements',n_el,'letters',n_let)
print('1905-06-20 is', datetime.date(1905,6,20).strftime('%A'))
