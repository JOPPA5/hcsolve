# Independent decoder: own ciphertext re-keyed by the reviewer from the crops, not read from transcription.json
import string
ct="Nz Pxo Cpz J bn Tpssz up ifbs zpv bsf Opu xfmm Nboz uibolt gps dbse gpsfwfs zpvs Pxo Hjsm"
words=set("""my own boy i am sorry to hear you are not well many thanks for card forever your girl""".split())
a=string.ascii_lowercase
for k in range(26):
    tr=str.maketrans(a,a[-k:]+a[:-k]) if k else None
    p=ct.lower().translate(tr) if k else ct.lower()
    print(k,sum(w in words for w in p.split()),len(p.split()),p if k in(0,1,25) else '')
print('letters',sum(c.isalpha() for c in ct))
