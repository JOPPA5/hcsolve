# Independent reviewer decode of hcp-1386 (own transcription from review/work/L*.png crops)
rows = ["Nz. Pxo. [E. L.] Cpz.", "uibolt-wfsz.", "nvdi gps. mfuufs", "Up-Ebz. Nz.",
        "[N. & L.] gspn. zpvs.", "Pxo. [E. L.] Hjsm", '"wfsz. wjsfe."']
def dec(s):
    out=[];lit=False;n=0
    for ch in s:
        if ch=='[':lit=True
        if ch==']':lit=False
        if ch.isalpha() and not lit:
            out.append(chr((ord(ch.upper())-65-1)%26+65));n+=1
        else: out.append(ch)
    return ''.join(out),n
tot=0
for r in rows:
    p,n=dec(r);tot+=n;print(f"{r:28s} -> {p}")
print("enciphered letters:",tot)
print("alt last word ujsfe ->",dec("ujsfe")[0])
