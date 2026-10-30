#!/usr/bin/env python3
"""Reviewer's independent decoder for hcp-1787. Own transcription from own crops of work/hires/.
Token = sign + vowel mark: e dash, E hooked dash, i dot, u two dots, o slash, a heavy stroke; ^ caron, r ring.
? = unread sign. A reading matches only if consonants and written vowels match in order; the ONLY thing
it may add is an unwritten a/a-acute (and written-vs-unwritten carons are folded). Stricter than the
solver's subsequence test, which accepts any inserted letters."""
import re, unicodedata
C = dict(zip('0123456','ltnmrsp'))|{'8':'h','9':'k','v':'v','x':'z','j':'j','c':'c','S':'s'}
V = {'e':'e','E':'e','i':'i','u':'u','o':'o','a':'a'}
def fold(s):
    s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if not unicodedata.combining(c))
    return s.replace('ch','h').replace('d','t').replace('b','p').replace('y','i')
def lit(w):
    out=''
    for t in w.split('.'):
        if t[0] in 'AOU' and len(t)==1: out+=t.lower(); continue
        out+=C[t[0]]+''.join(V.get(c,'') for c in t[1:])
    return out
def fits(w,reading):
    if reading.startswith('['): return None
    rx='^'+'a?'.join(re.escape(c) for c in lit(w))+'a?$'
    rx=rx.replace(r'\?','.*')
    return bool(re.match(rx,fold(reading)))
T = """
je.5.1 jest|2e.1e.0e neděle|4a.2o ráno
O.1e.5e.0 odešel|j.5e.3 jsem|x z|9a.5a.4e.2 kasáren
1o do|6a.4.9u parku|vo.1.4a.2.1i Vodranty|ja.9 jak|9.4a.5a krása
x.1e zde|xa za|1a.9 tak|9.4a.5.2e.8o krásného|3a.jo.ve.8o májového
ji.1.4a jitra|v.x.6o.3i.2a.3 vzpomínám|5i si|2a na|va.5 vás|3i.0o.v.2a milovaná
3a.4e.2.9o Mařenko|A a|2a na|1.4a.8i drahý|1o.3o.v domov
ja.9 jak|4a.1 rád|6i.8 bych|5e se|6i.0 byl|6o.1i.va.0 podíval|1o.3u domů
A.0e ale|2a.5 náš|8.j.1.3a.2 hejtman|6.4o.9.0e.1i prokletý|3a.1.4 Maďar
2e.1o.8o.0i.0 nedoholil?|A.2i ani|je.1.2o.8o jednoho|xe že|ja.5.3e jsme
5e.3 sem|6.4i.5.0i přišli|2a na|1.4i tři|2e.1E.0e neděle|A a|9.1i.x když
2a.3 nám|1a dá|je.1.2ou jednou|A.x až|x za|1i.1e.2 týden|1oe to
1o.8o toho|3a.3e máme|1o.5.1i dosti|1a.9 tak|5e se|1E.5i.3 těším
x.1a.0i zdali|6i.8o.3 bychom|5e se|3o.8.0u mohlu?|vi.1aE.1 vidět?|2e.8o.1i.1e nechodíte
2a na|6o.2.v.0i.2.9 ponavlink|v.4o.x.1E.4i vrozděři|j.5.1e jste|1a.9e také
2e.6i.0a nebyla|je.5.1e ještě|0e.1o.5 letos
5e.1i.3 sedím|2a na|0a.v.ce lavce|A a|6i.5u píšu|6.4i.je.1.1e přijeďte|5e.3 sem|ve ve|5.1E.1u stědu?|9.1e.1i.ce ktetice
ja.9 jak|5.1a.5.1e.2 šťasten|6i.8 bych|6i.0 byl|9.1i.6i.8 kdybych
va.5 vás|vi.1e.0 viděl|6o po|6o.9u boku|5.vi.3 svým
U u|1o.8o.1o tohoto|xa.3.9u zámku|je je|ce.0i celý|?.9 [?]|1aE.0a.3e děláme?|9a.x.1i každý|1e.2 den|ve.0.9e velké|3a.4.5e marše
xe že|9a.x.1i každý|5i si|2a na|4i.9a říká|x že|8o ho|6o.0e.ji bolejí|2o.8i nohy|?.e.6e [?]|A.x až|6u.1e bude|?.1a.0.v.4.1a [?]|2e.1E.0e neděle
S.4.1e.c.2E srdečně|va.5 vás|x.1.4a.vi zdraví|6a.c pac|A a|6u.5u pusu|6o.5i.0a posílá|va.5 váš
"""
bad=[]; n=0; out=[]
for line in T.strip().splitlines():
    for it in line.split('|'):
        w,r=it.split(' ',1); n+=1; out.append(r)
        f=None if '?' in w.split('.')[0] else fits(w.replace('?',''),r.rstrip('?'))
        if f is False: bad.append((w,lit(w.replace('?','')),r))
print(n,'words;',len(bad),'do not fit under the strict test:')
for b in bad: print('  ',b)
print(' '.join(out))
