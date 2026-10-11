from pathlib import Path
import re,json,hashlib,unicodedata
from collections import Counter
B=Path(__file__).resolve().parent
groups=(B/'ciphertext-groups.txt').read_text().split()
groups=[x.lower() for x in groups if re.fullmatch('[a-zA-Z]{5}',x)]
# Pixel reinspection, not plaintext/key-selected corrections.
groups[46]='xxazt'
groups[53]='hveje'
assert len(groups)==130 and all(len(x)==5 for x in groups)
ct=''.join(groups)
(B/'ciphertext650.txt').write_text(ct+'\n')
(B/'groups-indexed.tsv').write_text('group\tstart_1based\tend_1based\treading\n'+''.join(f'{i+1}\t{i*5+1}\t{i*5+5}\t{g}\n' for i,g in enumerate(groups)))
branches=[(11,'cdlvw',['cdivw'],'third L favoured; overlying handwriting',None),(18,'eldne',['eldna'],'E favoured, watermark',[426,386,502,427]),(26,'pmowj',['lmowj'],'P favoured under watermark',None),(31,'hdeui',[],'E favoured under handwritten stroke',None),(47,'xxazt',['xxezt'],'A favoured in broad context; uncertain counters',[864,500,943,541]),(54,'hveje',['hvaje','hvaja'],'enlargement favours two E glyphs; watermark ambiguity',[750,540,839,580]),(96,'cdfbs',['cdirs','cdfrs'],'F/B favoured; watermark overlaps',[808,844,894,888]),(101,'imves',['imvas'],'E favoured in enlargement',[585,882,666,924])]
(B/'glyph-branches.json').write_text(json.dumps([dict(group=g,positions_1based=[5*g-4,5*g],preferred=p,alternatives=a,evidence=e,source_box_xyxy=box) for g,p,a,e,box in branches],indent=2)+'\n')
pt=(B/'plaintext-typed.txt').read_text()
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if c in 'abcdefghijklmnopqrstuvwxyz')
words=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
prepared=norm(re.sub(r'\d',lambda m:words[int(m[0])],pt))
assert len(norm(pt))==536 and len(prepared)==640
(B/'plaintext-digitwise640.txt').write_text(prepared+'\n')
results={'ciphertext_length':len(ct),'groups':len(groups),'first_group':groups[0],'last15groups':groups[-15:],'plaintext_alpha_excluding_numbers':len(norm(pt)),'digit_count':len(re.findall(r'\d',pt)),'number_tokens':re.findall(r'\d[\d.]*\d',pt),'digitwise_DVA_length':len(prepared),'digitwise_DVE_length':len(prepared),'sentence_fullstops_excluding_numeric_separators':4,'conditional_length_example':{'digitwise_body':640,'four_sentence_J':4,'unknown_initial_five':5,'one_filler':1,'total':650},'cipher_inventory':dict(sorted(Counter(ct).items())),'plaintext_digitwise_inventory':dict(sorted(Counter(prepared).items()))}
(B/'counts.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
sources=Path('batches/solved-context-main/373')
(B/'manifest.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [sources/'cryptogram.jpg',sources/'plaintext.jpg',sources/'SOURCES.md',B/'ciphertext650.txt',B/'plaintext-typed.txt']},indent=2)+'\n')
print(json.dumps({k:v for k,v in results.items() if 'inventory' not in k},ensure_ascii=False))
