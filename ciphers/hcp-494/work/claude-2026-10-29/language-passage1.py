#!/usr/bin/env python3
"""Language checks for HCP 494 passage 1 ("Totaliter disgustirt undertanin <634>").

Corpus: nine DTA texts 1647-1669 in ../period-text/*.txt (plain text).
Outputs language-passage1.json next to this script.

Questions:
 1. Unterthan/Underthan without -en used as plural/collective?
 2. disgustirt + persons attested?
 3. Segmentations of the 10 letters u n d e r t a ? i n (? = any letter or syllable sign)
    scored against the corpus vocabulary.
 4. Adel / Buerger / Bauern triad.
"""
import glob, json, math, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = sorted(glob.glob(os.path.join(HERE, '..', 'period-text', '*.txt')))
OUT = os.path.join(HERE, 'language-passage1.json')

texts = {}
for p in CORPUS:
    with open(p, encoding='utf-8', errors='replace') as f:
        texts[os.path.basename(p)] = f.read()

def norm(s):
    s = s.lower()
    s = (s.replace('ſ', 's').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
           .replace('ß', 'ss').replace('aͤ', 'ae').replace('oͤ', 'oe').replace('uͤ', 'ue'))
    s = re.sub(r'[ͤ̈]', 'e', s)  # combining e / diaeresis -> e (umlaut)
    s = s.replace('v', 'u').replace('w', 'w')
    return s

# ---- tokenisation / vocabulary -------------------------------------------
WORD = re.compile(r"[A-Za-zÄÖÜäöüßſͤ]+")
vocab = collections.Counter()
vocab_raw = collections.Counter()
for name, t in texts.items():
    for m in WORD.finditer(t):
        w = m.group(0)
        vocab_raw[w.lower()] += 1
        vocab[norm(w)] += 1
NTOK = sum(vocab.values())

def kwic(pattern, width=90, flags=re.I, limit=400):
    out = []
    rx = re.compile(pattern, flags)
    for name, t in texts.items():
        for m in rx.finditer(t):
            a, b = max(0, m.start()-width), min(len(t), m.end()+width)
            ctx = re.sub(r'\s+', ' ', t[a:b])
            out.append({'file': name, 'match': m.group(0), 'ctx': ctx})
            if len(out) >= limit:
                return out
    return out

result = {'corpus_files': [os.path.basename(p) for p in CORPUS], 'tokens': NTOK}

# ---- Q1: Unterthan forms -------------------------------------------------
forms = collections.Counter()
for name, t in texts.items():
    for m in re.finditer(r"\b[uv]n[dt]er[dt]h?[aä]n\w*", t, re.I):
        forms[norm(m.group(0))] += 1
result['q1_unterthan_forms'] = forms.most_common()
# singular-looking forms (no -en/-s ending) with their contexts, to judge number
sing = kwic(r"\b[uv]n[dt]er[dt]h?[aä]n(?![a-zäöüſ])", width=110)
result['q1_unterthan_no_suffix_contexts'] = sing
# determiners before the bare form: plural markers (die/der(gen.pl.)/seine/ihre/alle/viel...)
det = collections.Counter()
for s in sing:
    pre = s['ctx'][:110].split()
    det[' '.join(pre[-2:]).lower()] += 1
result['q1_preceding_words_before_bare_form'] = det.most_common()
# also the adjective/predicate use "unterthan sein/seyn"
result['q1_unterthan_predicative'] = kwic(r"\b[uv]n[dt]er[dt]h?[aä]n\s+(seyn|sein|sind|seynd|ist|gewesen|wer[dt]en|w[eä]re|wird|bleiben|zu\s+seyn|zu\s+sein|und|vnd|gemacht)\b", width=100)

# ---- Q2: disgust* -----------------------------------------------------------
result['q2_disgust'] = kwic(r"\bdisgust\w*|\bdegout\w*|\bdisgousti\w*", width=120)
result['q2_disgust_forms'] = collections.Counter(norm(k['match']) for k in result['q2_disgust']).most_common()

# ---- Q3: segmentation of u n d e r t a ? i n -------------------------------
LETTERS = 'abcdefghiklmnopqrstuwxyz'
SYLL = ['au','eu','ei','ie','ii','ou','ch','ck','ct','ff','ll','mm','nn','pp','rr','sch','ss','sp','st','tt','tz']
# allow the spelling variants the vocabulary normalisation produces (u=v, th/t, d/t)
def variants(w):
    """candidate normalised corpus spellings for a plaintext chunk w"""
    vs = {w}
    vs |= {w.replace('t', 'th')} if 't' in w else set()
    vs |= {re.sub(r'(?<=r)t', 'th', w)}
    vs |= {w.replace('under', 'unter'), w.replace('under', 'vnter'), w.replace('under','unther')}
    vs |= {v.replace('tan','than') for v in list(vs)}
    vs |= {v.replace('tan','than') for v in list(vs)}
    vs |= {v.replace('taz','tatz') for v in list(vs)}
    return {norm(v) for v in vs}

def freq(w):
    return max(vocab.get(v, 0) for v in variants(w))

def best_spelling(w):
    return max(((vocab.get(v,0), v) for v in variants(w)))[1]

MINF = 1
PENALTY = 10.0   # log-cost per extra word, favours fewer longer words
def segmentations(s):
    n = len(s)
    res = []
    def rec(i, acc):
        if i == n:
            res.append(list(acc)); return
        for j in range(i+1, n+1):
            acc.append(s[i:j]); rec(j, acc); acc.pop()
    rec(0, [])
    return res

cands = []
for q in list(LETTERS) + SYLL:
    s = 'underta' + q + 'in'
    for seg in segmentations(s):
        if len(seg) > 4: continue
        fs = [freq(w) for w in seg]
        if min(fs) < MINF: continue
        # score: sum log p(word) - penalty per word
        score = sum(math.log(f / NTOK) for f in fs) - PENALTY * (len(seg) - 1)
        cands.append({'q': q, 'string': s, 'seg': ' | '.join(seg), 'freqs': fs,
                      'spellings': [best_spelling(w) for w in seg], 'score': round(score, 2)})
cands.sort(key=lambda c: -c['score'])
result['q3_all_candidates_count'] = len(cands)
result['q3_top_candidates'] = cands[:60]
# per-? best candidate
best_by_q = {}
for c in cands:
    best_by_q.setdefault(c['q'], c)
result['q3_best_per_unknown'] = best_by_q
# frequencies of the specific words at issue
words = ['undertan','underthan','unterthan','unterthanen','underthanen','undertanin','unterthanin','und','er','erta','ertan','tan','tanin','in','underta','ertaz','taz','tazin','erthan','ertahn']
result['q3_key_word_freqs'] = {w: {'freq': freq(w), 'spelling': best_spelling(w)} for w in words}
result['q3_in_holstein_like'] = kwic(r"\bin\s+(Holstein|Dennemarck|Dänemark|D[aä]nnemark|Teutschland|Franckreich|Schweden)\b", width=80, limit=30)

# ---- Q4: Adel / Buerger / Bauern ---------------------------------------
tri = kwic(r"\b(Adel\w*|Ritterschafft\w*|Ritterschaft\w*)\b[^.;:]{0,60}\b(B[uü]rger\w*)\b[^.;:]{0,40}\b(Bau[er]+\w*|Baw[er]+\w*)\b", width=120)
result['q4_adel_buerger_bauern'] = tri
tri2 = kwic(r"\b(B[uü]rger\w*)\b[^.;:]{0,40}\b(Bau[er]+n|Baw[er]+n)\b", width=100, limit=60)
result['q4_buerger_bauern_pairs_count'] = len(tri2)
result['q4_buerger_bauern_pairs_sample'] = tri2[:25]
result['q4_adel_bauern_any_order'] = kwic(r"\b(Adel|Bau[er]+n|B[uü]rger)\b[^.;:]{0,40}\b(Adel|Bau[er]+n|B[uü]rger)\b[^.;:]{0,40}\b(Adel|Bau[er]+n|B[uü]rger)\b", width=100, limit=60)
# plainte(n) / combinir(t)
result['q4_plainte_combinir'] = kwic(r"\bplaint\w*|\bcombini\w*|\bcombinir\w*", width=100, limit=40)
result['q4_sowohl_als'] = kwic(r"\bnun\s+so\s*wo[h]?l\s+als\b", width=100, limit=20)


# ---- external attestations gathered by hand on 2026-10-29 (DTA web search, DWDS/Grimm DWB) ----
result['web_attestations'] = {
 'grimm_dwb_unterthan_noun (dwds.de/wb/dwb/unterthan, read 2026-10-29)': [
   'nom. pl.: "seine unterthane" (Luther) obsolete, otherwise "wie heute allgemein: unterthanen"; gen. pl. "durchweg unterthanen" (Reichstagsabschied 1518)',
   'consonant-merged forms "unterthan", "undertann", "untherthan" occur in DATIVE and ACCUSATIVE plural (A. v. Eyb 1511; Seuse; Nomenclator Hamburgensis 1634); "die n. spr. kennt nur den pl. unterthanen"',
   'collective singular noted: H. Sachs "da wirdt der undterthan auch murrisch"; Gryphius Trauersp. 205; Goethe 16,22',
   'adjective unterthan: rarely attributive, otherwise predicative ("du bleibest zwar dem koenig unterthan", Gryphius 1663)'],
 'dta_exact_Unterthan_after_plural_marker': [
   'query "$w=/^(die|alle|seine|ihre|...)$/ @Unterthan": 4 hits, all SINGULAR: Hohberg Georgica 1682 "der arme Unterthan nicht uebertrieben" (collective sg.), Moeser 1775, Jean Paul 1795, Ideler 1847 (predicative adj.)',
   'same with Underthan/Vnderthan: 4 hits, all singular: Abraham a S. Clara 1686 "armen Vnderthan" (collective sg.), 1689; Obrecht 1617; Mollenfeld 1616',
   'no nominative plural "die Unterthan" found in DTA'],
 'dta_disgustirt': [
   '13 hits total; 17th c.: Theatrum Europaeum 1635 "Nicht wenig seynd zwar die Catholischen Staende disgustirt worden"; Grimmelshausen 1669 "so sich seines Verhaltens halber disgustirt befinden wolten"; Abraham a S. Clara 1692 "hat er den Herrn disgustirt"; later Puetter 1787 "dergestalt disgustirt werden", Bismarck 1898 "sehr disgustirt sind", NRhZ 1849 "die ... Serben, die ... sehr disgustirt sind"'],
 'dta_adel_buerger_bauern': [
   'query "Adel /^B[uü]rger.*/ und /^Ba[wu]w?e?r.*/": 1 hit, Theatrum Europaeum 1635 "dasz Adel Buerger vnnd Bawren sich also gefast hielten" (levy on both banks of the Oder)',
   'local corpus: Wartmann 1650 "neben vnnd vber den Burger- vnnd Bawern stand", "deß dritten Stands oder der Burger vnd Bawrn"; no Adel+Buerger+Bauern triad in the 8.7 MB local sample'],
}
result['assessment'] = {
 'q1': 'Bare "Unterthan/Underthan" as NOMINATIVE plural is not attested in the local corpus (28 bare forms, all singular or predicative adjective), in DTA (0 hits), or in Grimm (nom. pl. only unterthane/unterthanen; bare "unterthan" only as dat./acc. pl. in 16th-c. and in Nomenclator Hamburgensis 1634). A collective singular "der (arme) Unterthan" IS attested (H. Sachs; Hohberg 1682; Abraham a S. Clara 1686), but always with an article.',
 'q2': '"disgustirt" + persons is well attested in the period: estates (Theatrum Europaeum 1635), individuals (Grimmelshausen 1669, Abraham 1692). Local corpus also has "Disgoustierte" (persons) and "disgusti/disgusten" (noun).',
 'q3': 'Over 24 letters + 21 syllable signs for ?, and all segmentations into <=4 words, the only candidates whose every piece is a real period word are: ?=n "undertan | in" (15 x 18243) and "undertanin" (fem. Unterthanin, 1 hit, semantically impossible); ?=g "under | tag | in" (Unter-tag? not a word, only chunks); ?=l "under tal in"; ?=x "under tax in" — all three are chunk coincidences, not German. "und | er | ta? | in" never yields a word for ta?. So "undertan in" is the only linguistically viable reading, and it requires ?=n.',
 'q4': '"Adel, Buerger und Bauern" is a conventional generic social triad (TE 1635), not the formal Holstein Landtag formula (Praelaten, Ritterschaft, Staedte). In the letter the triad is clear text after "in 601 Dennemarck" and is not itself at issue.',
}

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)

# ---- console summary ----
print('tokens', NTOK)
print('\nQ1 forms:', forms.most_common())
print('Q1 bare-form contexts:', len(sing))
for s in sing: print('  ', s['file'][:12], '|', s['ctx'])
print('\nQ1 predicative:', len(result['q1_unterthan_predicative']))
for s in result['q1_unterthan_predicative'][:15]: print('  ', s['file'][:12], '|', s['ctx'])
print('\nQ2 disgust forms:', result['q2_disgust_forms'])
for s in result['q2_disgust']: print('  ', s['file'][:12], '|', s['ctx'])
print('\nQ3 key word freqs:'); 
for w,v in result['q3_key_word_freqs'].items(): print('  ', w, v)
print('\nQ3 top candidates:')
for c in cands[:40]: print('  ', c['q'], c['seg'], c['freqs'], c['score'])
print('\nQ3 best per ?:')
for q,c in best_by_q.items(): print('  ', q, c['seg'], c['freqs'], c['score'])
print('\nQ4 triad:', len(tri))
for s in tri: print('  ', s['file'][:12], '|', s['ctx'])
print('\nQ4 Buerger..Bauern pairs:', len(tri2))
for s in tri2[:12]: print('  ', s['file'][:12], '|', s['ctx'])
print('\nQ4 plainte/combinir:', len(result['q4_plainte_combinir']))
for s in result['q4_plainte_combinir'][:12]: print('  ', s['file'][:12], '|', s['ctx'])
print('\nQ4 nun sowohl als:', len(result['q4_sowohl_als']))
