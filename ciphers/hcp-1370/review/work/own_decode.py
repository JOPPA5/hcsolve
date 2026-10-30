# Independent reviewer decode: words typed from my own reading of hires crops, not from transcription.json
words = "Nz Pxo Cpz kvtu dpnf Cbdl gspn ibwjoh b Mjuumf Tqjo Nz gspn zpvs Pxo Hjsm".split()
abc = "abcdefghijklmnopqrstuvwxyz"
pt = ["".join(abc[(abc.index(c.lower())+25)%26] for c in w) for w in words]
print(" ".join(pt).upper()); print(len(words), "words", sum(map(len,words)), "letters")
for a,b in [(1907,9),(1907,7)]:
    import datetime; print(a,b,datetime.date(a,b,30).strftime("%A"))
