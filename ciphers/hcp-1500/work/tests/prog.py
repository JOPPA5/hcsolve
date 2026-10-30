toks=['abc','ly','xuder','comde','13guf','h','lz','kncv','13g4hs','pne','pnvvx','cn']
def sh(c,k): return chr((ord(c)-97+k)%26+97) if c.isalpha() else c
for mode in ('cont','word'):
  for sgn in (1,-1):
    for st in range(26):
      out=[];i=0
      for t in toks:
        if mode=='word': i=0
        s=''
        for c in t:
          s+=sh(c,sgn*(st+i)); i+=1
        out.append(s)
      print(mode,sgn,st,' '.join(out))
