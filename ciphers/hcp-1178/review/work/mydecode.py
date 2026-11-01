# Reviewer's independent decode. Values taken only from hcp-1174's own sign table (not 1178's key).
T="2, 0 7 0 5, 5. 1. 7 8, 2. 4, 1: 3".split()   # my pixel reading, review/work/d1-d3
K={'0':'o','1.':'a','1:':'e','2,':'cs','2.':'é','3':'d','4,':'g','5,':'l','7':'k','8,':'t'}
print(''.join(K.get(t,'['+t+']') for t in T))
for v in ('l','j'): print(v,''.join((K.get(t) or v) for t in T))
