from pathlib import Path
P=Path(__file__).resolve().parent;OLD=P.parent/'quagmire-keywords-12-sol61'
s=(OLD/'search.cpp').read_text().replace("kind==1?x.slots[(c-r+26)%26]-'a':(x.A[c]-r+26)%26","kind==1?x.slots[(c-r+26)%26]-'a':kind==2?(x.A[c]-r+26)%26:x.slots[(x.A[c]-r+26)%26]-'a'")
(P/'search.cpp').write_text(s);(P/'alphabets.tsv').write_bytes((OLD/'alphabets.tsv').read_bytes())
base=(OLD/'run.py').read_text().split('for k in [1,2]:')[0]
base=base.replace("else s[(ord(c)-97+r[i%len(r)])%26]","else s[((ord(c)-97 if k==2 else a[c])+r[i%len(r)])%26]")
base=base.replace("else chr(97+(a[c]-r[i%len(r)])%26)","else (chr(97+(a[c]-r[i%len(r)])%26) if k==2 else s[(a[c]-r[i%len(r)])%26])")
(P/'base.py').write_text(base)
