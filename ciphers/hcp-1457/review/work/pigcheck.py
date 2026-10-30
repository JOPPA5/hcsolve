# Encode the claimed English with "onset to end + a" and compare with reviewer's literal reading of the margin.
import re
plain = "many thanks for P.C. this morning have you seen that view be fore very pretty".split()
seen  = "anyma ankstha orfa P.C. istha orningma aveha ou?a eensa attha iewva eba orefa eryva ettypra".split()
def enc(w):
    if w == 'P.C.': return w
    m = re.match(r'([^aeiou]*)(.*)', w); return m.group(2)+m.group(1)+'a'
for p, s in zip(plain, seen):
    e = enc(p); ok = all(a==b or b=='?' for a,b in zip(e,s)) and len(e)==len(s)
    print(f'{p:8} -> {e:10} seen {s:10} {"OK" if ok else "DIFF"}')
