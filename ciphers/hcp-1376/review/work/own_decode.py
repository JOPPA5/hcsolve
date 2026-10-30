# independent transcription, typed from review crops; own shift loop
lines=["Nz Px","Jt xbt qptufe","Cfgpsf","dmfbsjoh","Jut b Nztufsz","Nz gspn Zpvs","Hjsm"]
n=0
for l in lines:
    o=''
    for c in l:
        if c.isalpha():
            b=65 if c.isupper() else 97; o+=chr((ord(c)-b-1)%26+b); n+=1
        else:o+=c
    print(l,'->',o)
print(n)
