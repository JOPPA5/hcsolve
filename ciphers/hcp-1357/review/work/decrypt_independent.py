# Independent decode of the reviewer's own sign-by-sign transcription (made from review crops, not from work/transcription.json)
own=["Nz. pxo. Efbsftu Cpz.","Uijt- Xjmm. nblf. uif","qbjs gps bmcvn","gspn. Zpvs. Hjsm"]
tab=str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","ZABCDEFGHIJKLMNOPQRSTUVWXYzabcdefghijklmnopqrstuvwxy")
n=0
for l in own:
    print(l.ljust(26),l.translate(tab)); n+=sum(c.isalpha() for c in l)
print(n)
# brute force: every shift, count hits of common words
ws=set("my own dearest boy this will make the pair for album from your girl of and to in".split())
s=" ".join(own).lower()
import re
for k in range(26):
    w=[''.join(chr((ord(c)-97-k)%26+97) for c in x) for x in re.findall('[a-z]+',s)]
    print(k,sum(x in ws for x in w),end=' | ')
print()
