"""Reviewer's independent Pigpen decoder for HCP 1017 (does not use solver files).
Notation (my own, read from the scan): grid cells by keypad position 1..9 in the
standard tic-tac-toe grid (1=top-left cell drawn as ┘ ... 9=bottom-right drawn as ┌);
a trailing '.' = dot. X wedges: n=∨ (top), w=> (left), e=< (right), s=∧ (bottom).
D = closed diamond (observed for W). # = cancelled/crossed ink. Words separated by '/'.
Standard key: grid A-I, dotted grid J-R, X S T U V, dotted X W X Y Z."""
import sys
grid='ABCDEFGHI'; dgrid='JKLMNOPQR'
key={str(i+1):grid[i] for i in range(9)}
key.update({str(i+1)+'.':dgrid[i] for i in range(9)})
key.update({'n':'S','w':'T','e':'U','s':'V','n.':'W','w.':'X','e.':'Y','s.':'Z','D':'W','#':'{#}','?':'?'})
rows={
'L1':"3. 9 5 2 n w 5 / 5 9. 5. 1 / D 9 5 / 7 5 w / 5 n / 4 9 9. / 8 5 e w 5",
'L2':"8 1 n w / 8 6. 6 6 5 5. w 3. 9 3 8 / 2. 5 # 9 5. 5 / 1 e n n 3 8 1 5 3. w 5",
'L3':"7 5 2 9. 9 5 7 w / D 5 9 3. / 4 e / n 6. / n 7. 1 5 w / 8 9 5. 1 e 6 2. 1 4. n w",
'L4':"4 e / 2. 6. 4. 4. n w / 1 3. n 6. / 4. 6. 9. 7 5 5. / 4 6. 5. 5. 5 9. n w 1 7 / 1 2 5 5. 4",
'L5':"e 5. 4 / 8 6. 3. 5 n w / 4. 9 3 8 / n 5 9 / 2 9 n / 4 1 5. / 1 e 6. / 4 1 n",
'L6':"8 5 9. s 3. 9 3 8 n w 5 / 7 5 7 9. e 5 n w / w 6. 5. / 4 5 9 5. 5 4.",
'L7':"5 1. 5. 1 9.",
'margin(rot180)':"w 1 e n 5 5. 4 / w 1 e n 5 5. 4 / 7 3. e 5 8 5 5. 4 5 / 2 e 5 n n 5",
}
n=0
for k,r in rows.items():
    words=[''.join(key[t] for t in w.split()) for w in r.split('/')]
    n+=sum(len(w.split()) for w in r.split('/'))
    print(f'{k:15s}', ' '.join(words))
print('glyph positions:',n)
