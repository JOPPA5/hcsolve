"""Reviewer's independent decode. Transcribed by the reviewer from review/work/crops/ as SHAPE names,
key values copied from the table in ciphers/hcp-1216/SOLUTION.md, not from the solver's ledger."""
import re,sys
K={'2bar':'a','six':'b','bowls':'cs','tick+long':'d','3bar':'e','loopdesc':'g','tall+tick':'h','cross':'i','invT':'j',
'sect':'k','wave':'l','3str':'m','2str':'n','loop':'o','Fsign':'r','rbowl':'s','gamma':'t','X':'u','chev':'v','ydesc':'y','tailX':'z','loop2':'ö','loop1':'ȯ'}
R=['sect 3bar tick+long chev 3bar rbowl invT loop wave 2bar 2str sect 2bar 3str',
'six 3bar bowls 3bar rbowl rbowl loop Fsign 2bar cross gamma sect loop2',
'rbowl tailX loop2 2str 3bar gamma gamma 3bar wave 3str 3bar loopdesc sect 2bar tall+tick',
'gamma 2bar 3str rbowl 2bar invT 2str 2bar wave 2bar gamma 2bar wave loop wave',
'chev 2bar rbowl loop 3str loop wave ydesc rbowl loop sect 2bar gamma',
'tick+long loop wave loopdesc loop wave loopdesc loop tailX cross sect',
'3str cross tick+long 3bar sect chev 2bar wave 2bar wave 2bar 2str 2str ydesc cross',
'3str X 2str sect 2bar gamma loop rbowl tailX 3bar tall+tick loop wave 2bar tick+long loop1 sect',
'chev 3bar gamma wave 3bar tick+long 3bar wave 3str 3bar loopdesc ydesc 3bar sect',
'six 2bar Fsign 2str 2bar loopdesc ydesc loop 2str Fsign loop rbowl tailX cross tick+long loop2',
'chev 2bar 2str bowls 2bar sect tall+tick loop wave 2str 2bar tall+tick Fsign 2bar invT loop',
'cross tick+long loop2 wave 3bar 2str 2str 3bar 2str 2bar invT tick+long rbowl tailX loop',
'chev 2bar wave six loop2 chev 3bar six six 3bar 2str cross rbowl gamma 3bar 2str',
'chev 3bar wave 3bar 2bar chev cross rbowl tailX loop 2str gamma wave 2bar gamma 2bar rbowl',
'Fsign 2bar']
n=0
for i,r in enumerate(R,1):
    t=r.split(); n+=len(t); print('%02d'%i,''.join(K[x] for x in t))
print(n,'signs')
