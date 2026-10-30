# Independent decode: my own sign-by-sign reading typed from review/work/r*.jpg, not from work/transcription.json
mine = ["Nz","Pxo","Cpz","J","bn","Tpssz","Nz","Mfuufs","xbt","mbuf","Nz","Gspn","zpvs","Pxo","Hjsm"]
dec=lambda w:''.join(chr((ord(c.lower())-97-1)%26+97) for c in w)
print(' '.join(dec(w) for w in mine)); print('letters',sum(map(len,mine)))
print('alt bo ->',dec('bo'))
# all 26 shifts: only -1 should give English on the fixed words
for s in range(26):
    print(s,' '.join(''.join(chr((ord(c.lower())-97-s)%26+97) for c in w) for w in mine[3:10]))
