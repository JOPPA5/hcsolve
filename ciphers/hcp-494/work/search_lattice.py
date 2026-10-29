"""Unsegmented suffix diagnostic: all letter/syllable replacements at <=2 tokens.

No generated candidate is a decipherment. Model ranking is only a search aid.
Unchanged numerical tokens retain the published table values; replacement
costs are counted by cipher token rather than by plaintext character.
"""
from pathlib import Path
from collections import Counter
import hashlib, heapq, itertools, json, math, re, unicodedata

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
TOKENS = '119 74 26 28 83 117 20 BB 37 104'.split()
BASE = list('undertazin')
ALPHA = list('abcdefghiklmnopqrstuwxyz')
SYLLABLES = 'au eu ei ie ii ou ch ck ct ff ll mm nn pp rr sch ss sp st tt tz'.split()
VALUES = ALPHA + SYLLABLES + ['']

def normalize(s):
    s = s.lower().replace('ſ', 's').replace('ß', 'ss').replace('ꝛ', 'r').replace('ͤ', 'e')
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    return re.sub('[^a-z]+', ' ', s.replace('j', 'i').replace('v', 'u')).strip()

sources = sorted((REPO / 'ciphers/hcp-517/source/dta').glob('*.txt'))
texts = [normalize(p.read_text().replace('¬\n', '')) for p in sources]
words = Counter(' '.join(texts).split())
training = ''.join(texts).replace(' ', '')
counts = {n: Counter(training[i:i+n] for i in range(len(training)-n+1)) for n in (3,4,5)}
logs = {n: {k: math.log(v + .1) for k, v in d.items()} for n, d in counts.items()}
floor = math.log(.1)

def score(s):
    # Fixed context, no speculative words inside the variable region.
    # TOKENS already includes the last 37 104 = in.
    t = 'disgustirt' + s + 'holstein'
    return sum(sum(logs[n].get(t[i:i+n],floor) for i in range(len(t)-n+1)) /
               (len(t)-n+1) for n in (3,4,5))

def segment(s):
    # Exact corpus words only, at most four words. This may return nonsense;
    # it never silently inserts or deletes letters from a candidate.
    states = {0: [(0., [])]}
    for i in range(len(s)):
        for sc, parts in states.get(i, []):
            if len(parts) == 4:
                continue
            for j in range(i+1, len(s)+1):
                w = s[i:j]
                if words[w] and (len(w)>1 or w in ('a','i')):
                    value = sc + math.log(words[w] / sum_words)
                    states.setdefault(j, []).append((value, parts + [w]))
        for j in list(states):
            if j > i:
                states[j] = sorted(states[j], reverse=True)[:5]
    return [{'text':' '.join(p), 'score':round(v,4)} for v,p in sorted(states.get(len(s), []), reverse=True)[:3]]

sum_words = sum(words.values())
seen = {}
for n in (0,1,2):
    for positions in itertools.combinations(range(len(BASE)), n):
        for replacements in itertools.product(VALUES, repeat=n):
            vals = BASE[:]
            for p,v in zip(positions,replacements): vals[p] = v
            changes = [(i,v) for i,v in enumerate(vals) if v != BASE[i]]
            s = ''.join(vals)
            if s not in seen or len(changes) < len(seen[s]): seen[s] = changes

best = heapq.nlargest(250, seen, key=score)
ranked = []
for s in best:
    ranked.append({'text':s, 'score':round(score(s),5),
                   'changes':[{'position':i+1,'token':TOKENS[i], 'old':BASE[i], 'new':v} for i,v in seen[s]],
                   'exact_word_segmentations':segment(s)})

# Separate all candidates that segment exactly into corpus words. Rank by
# changes, then the same score; do not require the selected top-250 cutoff.
lexical = []
for s, changes in seen.items():
    # Fast DP feasibility with a minimum two-character word except a/i.
    reach = {0:0}
    for i in range(len(s)):
        if i not in reach or reach[i] >= 4: continue
        for j in range(i+1,len(s)+1):
            w = s[i:j]
            if words[w] and (len(w)>1 or w in ('a','i')):
                reach[j] = min(reach.get(j,9),reach[i]+1)
    if len(s) in reach: lexical.append((len(changes),-score(s),s))
lexical.sort()
output = {'tokens':TOKENS, 'baseline':''.join(BASE), 'alphabet':ALPHA,
          'syllables':SYLLABLES, 'also_allow_empty':True, 'max_changed_tokens':2,
          'candidate_count':len(seen), 'model':'space-free character 3/4/5-grams from eight later DTA texts',
          'sources':[{'path':str(p.relative_to(REPO)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources],
          'best_by_language':ranked,
          'lexical_count':len(lexical),
          'lexical_best':[{'text':s,'changed_tokens':n,'score':-sc,'segmentation':segment(s)} for n,sc,s in lexical[:100]],
          'accepted':None}
(ROOT/'work/lattice-results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidate_count':len(seen),'top':ranked[:30], 'lexical_best':output['lexical_best'][:35]},ensure_ascii=False,indent=2))
