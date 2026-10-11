from pathlib import Path
import random,json,unicodedata
p=Path(__file__).parent
# Invented control, NOT historical plaintext or a crib for the target.
raw='Ministerstvo zahraničných vecí žiada vyslanectvo aby bezodkladne oznámilo výsledok rokovania s príslušnými úradmi. Prosíme o preverenie platnosti cestovných dokladov a o zaslanie presného zoznamu osôb ktoré požiadali o návrat do vlasti. Správu zašlite ešte dnes.'
raw=''.join(c for c in unicodedata.normalize('NFD',raw.lower()) if 'a'<=c<='z')
def enc(s,k):return ''.join(s[c::len(k)] for c in k)
def dec(s,k):
 n=len(s);w=len(k);out=['']*n;at=0
 for c in k:
  for r in range(n//w+(c<n%w)):out[r*w+c]=s[at];at+=1
 return ''.join(out)
for n in [240,245]:
 s=(raw*2)[:n];(p/f'control-{n}-plain.txt').write_text(s)
 for widths in [[19],[19,17],[19,17,22]]:
  rng=random.Random(399+n);keys=[];ct=s
  for w in widths:
   k=list(range(w));rng.shuffle(k);keys.append(k);ct=enc(ct,k)
  back=ct
  for k in reversed(keys):back=dec(back,k)
  assert back==s
  name=f'control-{n}-{len(keys)}stage'
  (p/f'{name}.txt').write_text(ct)
  (p/f'{name}-key.json').write_text(json.dumps(keys))
print('6 planted encryption/decryption round trips PASS')
