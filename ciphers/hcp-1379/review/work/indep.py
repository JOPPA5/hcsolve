# independent decode: my own transcription, typed from my crops; table built by hand from str.translate
import string
cipher=string.ascii_lowercase
plain=cipher[-1]+cipher[:-1]
t=str.maketrans(cipher,plain)
mine="nz efbsftu j ipqf zpv bsf gffmjoh cfuufs mpwf gspn zpvs pxo hjsm"
print(mine.translate(t)); print(sum(c.isalpha() for c in mine))
for k in range(1,26):
    tt=str.maketrans(cipher,cipher[k:]+cipher[:k])
    print(k,mine.translate(tt)[:40])
