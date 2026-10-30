#!/usr/bin/env python3
# Independent American Morse decoder (reviewer). Table typed from standard
# American (railroad) Morse; "=" = long dash L, "_" would be zero (unused).
import json, sys
from pathlib import Path
AM = {'.-':'A','-...':'B','.. .':'C','-..':'D','.':'E','.-.':'F','--.':'G',
'....':'H','..':'I','-.-.':'J','-.-':'K','=':'L','--':'M','-.':'N','. .':'O',
'.....':'P','..-.':'Q','. ..':'R','...':'S','-':'T','..-':'U','...-':'V',
'.--':'W','.-..':'X','.. ..':'Y','... .':'Z'}
t = json.loads(Path(sys.argv[1]).read_text())
out=[]
for col in t['columns']:
    out.append(' '.join(''.join(AM[c] for c in b.split(' / ')) for b in col))
print('\n'.join(out))
print(sum(len(w) for l in out for w in l.split()))
