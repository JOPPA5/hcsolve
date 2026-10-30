# independent: own transcription, own table, no import of solver files
import string
a=string.ascii_lowercase
t=str.maketrans(a+a.upper(),a[-1]+a[:-1]+a[-1].upper()+a[:-1].upper())
for row in ["Nz Pxo Mpwjoh Cpz","J Gffm wfsz","Ejtbqqpjoufe up","Ebz Op Mfuufs","Zpvs","Hjsm"]:
    print(row,'->',row.translate(t))
print('alt Mpwf',"Mpwf".translate(t), sum(c.isalpha() for c in "NzPxoMpwjohCpzJGffmwfszEjtbqqpjoufeupEbzOpMfuufsZpvsHjsm"))
import datetime;print(datetime.date(1907,7,3).strftime('%A'))
