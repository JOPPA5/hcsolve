from pathlib import Path
import re,unicodedata
SOURCE=Path('batches/kryha373-collation-sol61/plaintext-typed.txt')
def norm(t):return ''.join(c for c in unicodedata.normalize('NFD',t.lower())if 'a'<=c<='z')
def prepare(unamended=False,ji=False,extra=1,policy='lexical'):
 raw=SOURCE.read_text().split('6.000')[0];matches=list(re.finditer(r'[^\W\d_]+',raw,re.UNICODE));words=[];indices=[];p='';t=0;boundaries=[]
 for j,match in enumerate(matches):
  w=norm(match.group())
  if unamended and w=='ustredni':w='ustreni'
  if ji:w=w.replace('j','i')
  if j:
   gap=raw[matches[j-1].end():match.start()];press=policy=='lexical'or any(c.isspace()for c in gap)
   if press:t+=extra
   boundaries.append(dict(before_word=j,source_gap=gap,extra_advances=extra if press else 0))
  words.append(w)
  for ch in w:indices.append(t);p+=ch;t+=1
 assert len(p)==(92 if unamended else 93)
 return dict(p=p,press_indices=indices,words=words,boundaries=boundaries,source_raw_prefix=raw,unamended=unamended,natural_j_to_i=ji,extra=extra,policy=policy,emitted_space_letters=False)
