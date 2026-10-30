# independent decoder: retyped from reviewer's own reading of crops, not from transcription.json
A="abcdefghijklmnopqrstuvwxyz"
rows=["Nz Pxo","Cpz","J bn hpjoh po","odjfmz bcpvu","Nz Sppn usz Vtvbm","gps Nz","Gspn Zpvs Pxo","Hjsm"]
n=0
for r in rows:
    o=''
    for c in r:
        if c.lower() in A: o+=A[(A.index(c.lower())-1)%26].upper(); n+=1
        else: o+=c
    print(r,'->',o)
print(n)
