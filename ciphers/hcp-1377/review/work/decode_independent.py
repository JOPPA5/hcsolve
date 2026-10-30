# independent re-keying from reviewer's own reading of the card
rows=["J bn hpjoh up","Cjlf up","up npsspx","Nz Gspn Zpvs","Pxo Hjsm"]
t=str.maketrans("abcdefghijklmnopqrstuvwxyz","zabcdefghijklmnopqrstuvwxy")
n=0
for r in rows:
    print(r,'=>',r.lower().translate(t).upper()); n+=sum(c.isalpha() for c in r)
print(n)
