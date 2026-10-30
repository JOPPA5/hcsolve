import sys
M={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..'}
R={v:k for k,v in M.items()}
out=[];n=0;bad=[]
for ln in open(sys.argv[1]):
    if ln.startswith('#') or ':' not in ln: continue
    lab,body=ln.split(':',1); s=''
    for tok in body.split():
        if tok=='/': s+=' '
        elif tok=='&': s+='&'
        elif tok in R: s+=R[tok]; n+=1
        else: s+='?'; bad.append((lab,tok))
    out.append(f'{lab}: {s}')
print('\n'.join(out)); print(n,'letters; invalid',bad)
