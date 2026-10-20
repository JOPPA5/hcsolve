"""A1Z26; manual source transcription, no OCR or language-model correction."""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
def decode():
 manifest=json.loads((ROOT/'work/source-hashes.json').read_text())
 for name,digest in manifest.items():
  assert hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest()==digest,'source hash mismatch: '+name
 lines=[];tokens=[]
 for row,line in enumerate((ROOT/'work/transcription.txt').read_text().splitlines(),1):
  words=[]
  for col,part in enumerate(line.split('/'),1):
   part=part.strip()
   if part.startswith('{')and part.endswith('}'):
    text=part[1:-1];kind='cleartext';numbers=[]
   else:
    assert re.fullmatch(r'\d+(?:\.\d+)*',part),(row,col,part)
    numbers=list(map(int,part.split('.')));assert all(1<=n<=26 for n in numbers);text=''.join(chr(64+n)for n in numbers);kind='numeric'
   words.append(text);tokens.append({'line':row,'word':col,'source':part,'kind':kind,'plaintext':text,'numbers':numbers})
  lines.append(' '.join(words))
 # These six words wrap across physical source lines. No letters change.
 joins={4,5,8,12,13,14};reflow=lines[0]
 for before,line in enumerate(lines[1:],1):reflow+=(''if before in joins else' ')+line
 return {'key':{str(i):chr(64+i)for i in range(1,27)},'source':'manual transcription of source/picture.jpg','lines':lines,'plaintext':reflow,'tokens':tokens,'word_join_boundaries_after_source_line':sorted(joins)}
if __name__=='__main__':
 result=decode();print(json.dumps(result,indent=2)if'--json'in sys.argv else result['plaintext'])
