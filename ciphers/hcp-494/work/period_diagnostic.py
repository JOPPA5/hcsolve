"""Period-corpus and explicit copying-error diagnostics. No accepted plaintext.

This does not alter a source or silently choose any correction. Numeric table
columns are independently entered; local shifts are error hypotheses, not keys.
"""
from pathlib import Path
from collections import Counter
import hashlib, heapq, itertools, json, math, re, unicodedata
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
ALPHA='abcdefghiklmnopqrstuwxyz'
BASE='undertazin'
TOKENS='119 74 26 28 83 117 20 BB 37 104'.split()
TAG='{http://www.tei-c.org/ns/1.0}'

def text_of(e):
    # Exclude running headers, catchwords, signatures and editorial notes.
    if e.tag in {TAG+'fw',TAG+'note'}: return ''
    if e.tag in {TAG+'lb',TAG+'pb'}: return '\n'
    if e.tag==TAG+'choice':
        for tag in ['orig','sic','abbr','reg','corr','expan']:
            chosen=e.find(TAG+tag)
            if chosen is not None:return text_of(chosen)
    return (e.text or '')+''.join(text_of(c)+(c.tail or '') for c in e)

def normalize(t):
    t=t.lower().replace('ſ','s').replace('ß','ss').replace('ꝛ','r')
    t=''.join(c for c in unicodedata.normalize('NFD',t) if unicodedata.category(c)!='Mn')
    return re.sub('[^a-z]+',' ',t.replace('j','i').replace('v','u')).strip()

corpus=[];sources=[];concordance=[]
outdir=ROOT/'work/period-text';outdir.mkdir(exist_ok=True)
for p in sorted((ROOT/'source/dta-period').glob('*.xml')):
    root=ET.parse(p).getroot();body=root.find('.//'+TAG+'body')
    assert body is not None
    raw=text_of(body)
    raw=re.sub(r'[-¬⸗]\s*\n\s*','',raw)
    raw=re.sub(r'\s+',' ',raw)
    t=normalize(raw);corpus.append(t)
    (outdir/(p.name+'.txt')).write_text(raw+'\n')
    sources.append({'file':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                    'normalized_characters':len(t)})
    for m in re.finditer(r'\bdi[sſ]gu\w+',raw,re.I):
        concordance.append({'file':p.name,'form':m.group(),'context':raw[max(0,m.start()-180):m.end()+200]})
words=Counter(' '.join(corpus).split());training=''.join(corpus).replace(' ','')
counts={n:Counter(training[i:i+n] for i in range(len(training)-n+1)) for n in (3,4,5)}
logs={n:{s:math.log(v+.1) for s,v in d.items()} for n,d in counts.items()};floor=math.log(.1)
def score(s):
    t='disgustirt'+s+'holstein'
    return sum(sum(logs[n].get(t[i:i+n],floor) for i in range(len(t)-n+1))/(len(t)-n+1) for n in (3,4,5))

def distance(a,b):
    # Optimal string alignment: insertion, deletion, substitution, adjacent swap.
    d=[list(range(len(b)+1))]
    for i,x in enumerate(a,1):
        d.append([i]+[0]*len(b))
        for j,y in enumerate(b,1):
            d[i][j]=min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+(x!=y))
            if i>1 and j>1 and x==b[j-2] and a[i-2]==y:
                d[i][j]=min(d[i][j],d[i-2][j-2]+1)
    return d[-1][-1]

neighbors=[]
for w,c in words.items():
    if c>=2 and 3<=len(w)<=8:
        dist=distance('ertaz',w)
        if dist<=3:
            neighbors.append({'word':w,'distance':dist,'occurrences':c})
neighbors.sort(key=lambda r:(r['distance'],-r['occurrences'],r['word']))

# A single displaced table header or a local column-lookup slip across a span.
# No wraparound: the physical table has edges. Vertical shifts do not change
# the plaintext column in a homophonic alphabet, so are intentionally omitted.
shifts={}
for i in range(len(BASE)):
    for j in range(i+1,len(BASE)+1):
        for delta in range(-23,24):
            if delta==0:continue
            indices=[ALPHA.index(c)+delta for c in BASE[i:j]]
            if any(k<0 or k>=len(ALPHA) for k in indices):continue
            s=BASE[:i]+''.join(ALPHA[k] for k in indices)+BASE[j:]
            shifts.setdefault(s,[]).append({'first_token':i+1,'last_token':j,'column_delta':delta})

# One omitted/extra/reordered character, optionally one substitution elsewhere.
# This deliberately adds mechanisms absent from the previous replacement-only
# lattice. Not all of these alternatives are palaeographically likely.
structural={}
def add(s,event):structural.setdefault(s,event)
for i in range(len(BASE)+1):
    for c in ALPHA:add(BASE[:i]+c+BASE[i:],{'operation':'insert','at':i,'letter':c})
for i in range(len(BASE)):
    add(BASE[:i]+BASE[i+1:],{'operation':'delete','at':i,'letter':BASE[i]})
for i in range(len(BASE)-1):
    add(BASE[:i]+BASE[i+1]+BASE[i]+BASE[i+2:],{'operation':'adjacent_swap','at':i})
edits={s:[event] for s,event in structural.items()}
for s,event in structural.items():
    for i in range(len(s)):
        for c in ALPHA:
            if s[i]!=c:edits.setdefault(s[:i]+c+s[i+1:],[event,{'operation':'substitute','at_after_first_edit':i,'letter':c}])

def ranked(candidates,kind):
    best=heapq.nlargest(100,candidates,key=score)
    return [{'text':s,'score':round(score(s),5),kind:candidates[s]} for s in best]

result={'accepted':None,'corpus_selection':'nine DTA texts, 1647-1669: letters, statecraft, history, travel, fiction',
        'sources':sources,'normalized_characters':sum(len(t) for t in corpus),
        'normalized_characters_include_spaces':True,'training_letters':len(training),
        'word_types':len(words),'disgust_concordance':concordance,
        'dictionary_neighbors':neighbors,
        'column_shift_count':len(shifts),'column_shift_top':ranked(shifts,'mechanisms'),
        'structural_edit_count':len(edits),'structural_edit_top':ranked(edits,'operations'),
        'limits':'Rankings are linguistic hints only. Local shifts and edits are not evidence of an actual error or a consistent alternative key. At most 100 candidates per family are retained, not a manual adjudication of every generated string. Word counts include imperfectly normalized fragments; negative results are limited to this sample.'}
(ROOT/'work/period-diagnostic.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['accepted','normalized_characters','word_types','column_shift_count','structural_edit_count','disgust_concordance']},ensure_ascii=False,indent=2))
print('NEIGHBORS',json.dumps(neighbors[:35],ensure_ascii=False))
print('SHIFTS',json.dumps(result['column_shift_top'][:15],ensure_ascii=False))
print('EDITS',json.dumps(result['structural_edit_top'][:25],ensure_ascii=False))
