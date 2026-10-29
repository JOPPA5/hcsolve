"""Independent audit of a disclosed, borrowed partial reading; not a new decipherment."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
lines=[x.split() for x in (ROOT/'source/bourdeau/ct.txt').read_text().splitlines() if x.strip() and not x.startswith('#')]
# Independently encoded from the visible key255-0013 table, in the manuscript's column order.
cols='abcdefghiklmnopqrstuwxyz'
base=[20,22,24,26,28,21,23,25,27,29,70,72,74,76,78,71,73,75,77,79,120,122,124,126]
key={str(b+10*r):p for p,b in zip(cols,base) for r in range(5)}
# Explicit pairs prevent an omitted alphabet letter from silently shifting values.
key.update(dict(zip('CC DD EE FF GG HH II KK LL MM NN OO PP QQ RR SS TT UU WW XX YY ZZ AA BB'.split(),cols)))
key.update({'[st]':'st','[tt]':'tt','[634]':'<Holstein: borrowed gloss>','[768]':'<Sueco: borrowed gloss>'})
for n in range(1,20):key[str(n)]='∅'
literal=[''.join(key.get(t,'?') for t in row) for row in lines]
# Separate assumptions: these are disclosed in Bourdeau, not evidence supplied by the 1666 numeric table.
reading=dict(key);reading.update({'55':'g','[I]':'ll','8':'au'})
readings=[]
for i,row in enumerate(lines):
 vals=[reading.get(t,'?') for t in row]
 if i==1:vals[-1]='ff' # final XX interpreted as a different, look-alike syllable sign
 readings.append(''.join(vals))
suffix=lines[0][9:-1]
# The apparent und + five-letter word has no source word separators.
raw=''.join(key[t] for t in suffix)
# A boundary stress test, explicitly a construction, not an adopted reconstruction.
target='undertanin'
changes=[{'token':t,'literal':key[t],'required':p} for t,p in zip(suffix,target) if key[t]!=p]
result={'status':'PARTIAL; no new decipherment','letter_token_count':sum(not t.startswith('[6') and t!='[768]' for row in lines for t in row), 'literal':literal,'borrowed_reading_with_disclosed_assumptions':readings,'boundary_test':{'literal_suffix':raw,'constructed_target':target,'changes':changes,'accepted':False,'reason':'Requires BB=z -> n; no independent support for changing the key or reading BB as PP. Sentence grammar also unresolved.'},'gap_tokens':lines[0][12:17], 'conclusion':'The borrowed key reproduces the opaque gap. No new key, unique plaintext, or accepted gap reconstruction.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
