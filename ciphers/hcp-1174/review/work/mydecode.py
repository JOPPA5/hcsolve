#!/usr/bin/env python3
"""Reviewer's independent decode of hcp-1174: my own sign reading from 2-5x crops of the hires scan,
sign classes grouped by digit. Prints literal key output; '?' marks where the sign as seen has no key value
or where the shape disagrees with sense (see REVIEW1)."""
V={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á',':1':'ü','2.':'é','2,':'cs','3':'d','3,':'r','3.':'v',
   '4,':'g','5':'h','5,':'l','6,':'n','7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z'}
L=["2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1' 8",                     # salutation
   "0, 5, 1: 5, 5 1: 8, 5, 1: 7 2. 6,",                      # Ha ... teged
   "7. 1 3. 1: 8 2. 5, 1: 3",                                # Arcom derul ...
   "7. 1: 3, 1: 8, 1: 8",                                    # Mondd, hogy ...
   "7. 1 8 8, 1. 5, 1. 6, 7. 0 3, :1 3 3. 9 9, 9 5, 5, 1: 7", # bottom 1 (raw shapes)
   "2, 0 7 0 5, 5, 1. 7",                                    # bottom 2
   "7 1: 3, 1: 8, 0, 7 1: 3 3. 1: 7, 1: 3",                  # in parentheses; first sign shows no dot
   "1' 3, 9 1' 3"]                                           # signature in parentheses
n=0
for l in L:
    s=l.split(); n+=len(s); print(''.join(V.get(x,'?') for x in s), '   [%d]'%len(s))
print('signs',n,'distinct',len({x for l in L for x in l.split()}))
