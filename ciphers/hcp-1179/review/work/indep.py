# independent decode from reviewer's own sign reading (typed from review crops), key from hcp-1174 SOLUTION table
K={'1':'i','1.':'a','1:':'e','1,':'b',':1':'ü','0':'o','0,':'ö','2.':'é','2,':'cs','3':'d','3,':'r','3.':'v','4,':'g','5':'h','5,':'l','6,':'n','7':'k','7,':'s','7.':'sz','8':'m','8,':'t'}
R="""8 1 6, 3 1: 6, 8,
8 1: 4, 8, 1: 6, 6, 2. ?blot
2. 6,
2. 3, 8, 1: 3
1. 5. 1: 4, 7. 1: 1,
7 1. 3, 8. 1 8
7 :1 5, 3 0, 8
6, 2, 7 1: 3"""
for l in R.split('\n'): print(f"{l:34}", ''.join(K.get(t,'['+t+']') for t in l.split()))
