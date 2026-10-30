# Independent decode; my own transcription from review/work/r_*.png, not the solver's json.
import re
lines=["Xjui Mpwf boe","jttft gspn x pvst","M p p"]
dec=lambda s,k:''.join(chr((ord(c.lower())-97-k)%26+97) if c.isalpha() else c for c in s)
for k in range(26):
    t=' / '.join(dec(l,k) for l in lines)
    if k in(0,1,25) or 'with' in t: print(k,t)
print('letters',sum(c.isalpha() for l in lines for c in l))
print('variant first sign g:',dec('gttft',1),'| x as z:',dec('zpvst',1),'| N vs M:',dec('Npp',1),dec('Mpp',1))
words=set(w.strip().lower() for w in open('/usr/share/dict/words'))
print('?sses words:',sorted(w for w in words if re.fullmatch(r'[a-z]{1,3}sses',w)), 'kisses in list:', 'kisses' in words)
