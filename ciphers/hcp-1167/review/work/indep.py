# independent decode: own key written from hcp-1174 table, own tokenizer; corrected sign on line 12 via flag
import re,sys
K={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á','1,':'b',':1':'ü','.1':'u','2,':'cs','2.':'é',
'3':'d','3,':'r','3.':'v','4':'f','4,':'g','4.':'gy','5':'h','5,':'l','5.':'l','6':'j','6,':'n','6.':'ny',
'7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z'}
for i,l in enumerate(open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/work/transcription.txt',encoding='utf-8')):
    if l[0]=='#':continue
    print(''.join('/' if t=='|' else t if t in '()!' else (K[t.split('~')[0]]+('*' if '~' in t else '')) for t in l.split()))
