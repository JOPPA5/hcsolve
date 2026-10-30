import itertools
voc=set(l.split()[0] for l in open('ciphers/hcp-1500/work/tests/vocab.txt'))|{'a','i'}
for variant in ('skip','consume'):
  toks=['abc','ly','xuder','comde','13guf','h','lz','kncv','13g4hs','pne','pnvvx','cn']
  res=[]
  for L in range(1,5):
    for key in itertools.product(range(26),repeat=L):
      for mode in (0,1):
        i=0;sc=0;ws=[]
        for t in toks:
          o=''
          for c in t:
            if c.isalpha():
              x=ord(c)-97;y=key[i%L]
              o+=chr(((x-y) if mode==0 else (y-x))%26+97); i+=1
            else:
              o+=c
              if variant=='consume': i+=1
          ws.append(o)
          if o in voc: sc+=len(o)
        if sc>=12: res.append((sc,L,key,mode,' '.join(ws)))
  res.sort(reverse=True)
  print(variant)
  for r in res[:10]: print(r)
