# Independent Caesar -1 decode; words typed from the reviewer's own reading of msg.png, not from transcription.json
import re
T="""Nz Pxo Cpz kvtu dpnf cbdl J gpvoe mfuufst Xbjujoh ifsf gps pof xffl pomz gspn zpvs Pxo Hjsm""".split()
d=lambda w:''.join(chr((ord(c.upper())-65-1)%26+65) for c in w)
print(len(T),sum(map(len,T)));print(' '.join(d(w) for w in T))
