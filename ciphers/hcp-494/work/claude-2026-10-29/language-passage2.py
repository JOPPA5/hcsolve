#!/usr/bin/env python3
"""Language check for HCP 494 passage 2: "Gott geb das all wol ablauff" vs "ablauu".

Searches the local period corpus (nine DTA texts 1647-1669) for
  (1) forms of ablaufen used in the sense 'turn out' / subjunctive ablauff(e),
  (2) apocope of final -e in 3sg present subjunctive (geb/gebe, lauff/lauffe, ...),
  (3) any attestation of the letter strings ablauu / ablau u / blau u / lauu,
  (4) "all" vs "alles" before wol / in Gott-geb formulas.
Writes language-passage2.json next to this script. No Pillow, stdlib only.
"""
import glob, json, os, re, sys, unicodedata
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "..", "period-text")

def normalise(t):
    # long s, round-r, ligatures, combining diacritics (ſ, aͤ oͤ uͤ, å, é)
    t = t.replace("ſ", "s").replace("ꝛ", "r")
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = unicodedata.normalize("NFC", t)
    t = t.replace("ß", "ss").replace("ä", "a").replace("ö", "o").replace("ü", "u")
    t = re.sub(r"\s+", " ", t)
    return t.lower()

texts = {}
for p in sorted(glob.glob(os.path.join(CORPUS, "*.txt"))):
    with open(p, encoding="utf-8", errors="replace") as f:
        texts[os.path.basename(p).split(".")[0]] = normalise(f.read())
total = sum(len(t) for t in texts.values())

def kwic(pattern, width=70, maxhits=40, flags=re.I):
    rx = re.compile(pattern, flags)
    hits = []
    n = 0
    for name, t in texts.items():
        for m in rx.finditer(t):
            n += 1
            if len(hits) < maxhits:
                s, e = m.start(), m.end()
                hits.append({"text": name, "pos": s,
                             "kwic": t[max(0, s-width):s] + "[[" + t[s:e] + "]]" + t[e:e+width]})
    return {"pattern": pattern, "count": n, "examples": hits}

def count(pattern, flags=re.I):
    rx = re.compile(pattern, flags)
    return {name: len(rx.findall(t)) for name, t in texts.items()}

out = {"corpus_chars": total, "texts": list(texts)}

# (1) ablaufen family: all word forms
forms = Counter()
for t in texts.values():
    for m in re.finditer(r"\b(ab ?ge?l[aä]u?ff?[a-z]*|abl[aä]u?ff?[a-z]*)\b", t):
        forms[m.group(0)] += 1
out["ablaufen_wordforms"] = forms.most_common()
out["ablauff_kwic"] = kwic(r"\babl[aä]uff?e?n?\b", maxhits=60)
out["abgelauffen_kwic"] = kwic(r"\babgelauff?en\b", maxhits=30)
out["ablauff_sense_turnout"] = kwic(r"(wol|wohl|gut|ubel|ungluck|gluck)[a-z]* abl[aä]uff?e?n?\b|abl[aä]uff?e?n? (wol|wohl|gut|ubel)", maxhits=30)

# (2) apocope: 3sg subjunctive "gott geb" vs "gott gebe", "lauff"/"lauffe" etc.
out["gott_geb_vs_gebe"] = {
    "gott geb (apocopated)": kwic(r"\bgott geb\b(?!e)", maxhits=40),
    "gott gebe": kwic(r"\bgott gebe\b", maxhits=20),
    "gott gebs/gebe es": kwic(r"\bgott gebs?\b|\bgott geb es\b", maxhits=20),
    "der herr geb": kwic(r"\bherr geb\b(?!e)", maxhits=10),
    "geb(e) gott": kwic(r"\bgebe? gott\b", maxhits=20),
    "gott woll (apocop.)": kwic(r"\bgott woll\b", maxhits=20),
    "gott wolle": kwic(r"\bgott wolle\b", maxhits=10),
    "gott helff (apocop.)": kwic(r"\bgott helff\b", maxhits=20),
    "gott helffe": kwic(r"\bgott helffe\b", maxhits=10),
    "gott verleih (apocop.)": kwic(r"\bgott verleih\b", maxhits=10),
    "gott verleihe": kwic(r"\bgott verleihe\b", maxhits=10),
}
out["subj_apocope_counts"] = {
    "geb_apoc": count(r"\bgeb\b"), "gebe": count(r"\bgebe\b"),
    "woll_apoc": count(r"\bwoll\b"), "wolle": count(r"\bwolle\b"),
    "helff_apoc": count(r"\bhelff\b"), "helffe": count(r"\bhelffe\b"),
    "lauff_apoc": count(r"\blauff\b"), "lauffe": count(r"\blauffe\b"),
    "verleih_apoc": count(r"\bverleih\b"), "verleihe": count(r"\bverleihe\b"),
}
out["wol_ablauff_formula"] = kwic(r"wol[a-z]* (ab|aus|hin)?(l[aä]uff?e?n?|gehe?n?|gerath[a-z]*|gelinge?n?)\b", maxhits=40)
out["gott_geb_dass"] = kwic(r"\bgott gebe? (das|dass|daß)\b", maxhits=40)

# (3) ablauu / lauu / any "blau u"
out["ablauu_any"] = {
    "ablauu": kwic(r"ablauu"),
    "lauu (any)": kwic(r"lauu"),
    "au u (word boundary)": kwic(r"\bau u\b"),
    "blau u": kwic(r"\bblau u\b"),
    "ablau (as word)": kwic(r"\bablau\b"),
    "abl au": kwic(r"\babl au\b"),
    "a blau": kwic(r"\ba blau\b"),
    "uu inside word": kwic(r"[a-z]uu[a-z]", maxhits=20),
    "words ending -uu": kwic(r"\b[a-z]+uu\b", maxhits=20),
    "word 'uu'/'vu' alone": kwic(r"\b(uu|vu|uv)\b", maxhits=10),
}
# is final -uu/-u-u anything? 'lau' adj (lukewarm) + 'u'?  'blau' + 'u'?
out["blau_word"] = count(r"\bblau\b")
out["lau_word"] = count(r"\blau\b")

# (4) all vs alles in formulas
out["all_vs_alles"] = {
    "das all wol": kwic(r"\b(das|dass|daß) all wol\b"),
    "das alles wol": kwic(r"\b(das|dass|daß) alles wol\b"),
    "all wol": kwic(r"\ball wol[a-z]*\b", maxhits=30),
    "alles wol": kwic(r"\balles wol[a-z]*\b", maxhits=20),
    "all ding": kwic(r"\ball ding\b", maxhits=10),
    "all (standalone, neuter pronoun use sample)": kwic(r"\b(es|das|dass|daß|wie|ob) all (wol|gut|recht|ubel|nach|zu|mit)\b", maxhits=30),
    "counts all/alles": {"all": count(r"\ball\b"), "alles": count(r"\balles\b"), "alls": count(r"\balls\b")},
}
out["segmentation_a_b_l_au_u"] = {
    "note": "Possible splits of a-b-l-au-u as separate words: 'ab lau u', 'a blau u', 'abl au u', 'ablau u'. "
            "Tested word-boundary patterns above; see counts.",
    "ab lau": kwic(r"\bab lau\b"),
    "ab l au": kwic(r"\bab l au\b"),
}


# ---------------------------------------------------------------------------
# External attestations gathered 2026-10-29 with WebFetch from the Deutsches
# Textarchiv (DDC search, exact-token queries marked with @) and dictionaries.
# These are transcribed from the search-result snippets; verify before citing.
EXTERNAL = {
 "method": "DTA search https://www.deutschestextarchiv.de/search?q=... (lemma search unless @token). "
           "Snippets read via WebFetch; counts are the page's 'Treffer' totals.",
 "Q1_ablauffe_subjunctive_turn_out": {
  "query": "@ablauffe (exact token)", "total_hits": 26,
  "turn_out_sense_1640_1700": [
   "Birken, Die Fried-erfreuete Teutonje, 1652: 'wie übel es mit dem Leibe eines Staates oder Reiches ablauffe'",
   "Wartmann, De Statu Perturbato Germaniae et Franciae, 1652: 'biss man sehe ... wie das Teutsche Wesen ablauffe' (also in local corpus)",
   "Glauber, Opera Chymica 1, 1658: 'auff daß das Werck desto glücklicher ablauffe'",
   "Lütkemann, Harpffe von zehen Seyten, 1674: 'wie das ablauffe'",
   "Abraham a Santa Clara, Mercks Wienn, 1680: '... ungültig ablauffe'",
   "Becher, Psychosophia, 1683: 'die Trennung oder Freyheit ohne Feindschafft ablauffe'",
   "Siegemund, Hoff-Wehe-Mutter, 1690: 'wie es ablauffe'",
   "Spener, Theologische Bedencken 3, 1702: 'wie es ablauffe'",
   "Heinnitz, Mortis Praecipitium, 1628: 'daß es ohn Nucz nicht ablauffe'"],
  "wol_ablauffen_1640_1700_examples": [
   "Lütkemann, Apostolische Auffmunterung, 1652: 'es soll doch noch wol ablauffen'",
   "Wartmann 1650 (local corpus): 'nicht wohl ablauffen kondte'",
   "Wartmann 1653 (local corpus): 'die belagerung valence wurde wohl ablauffen'",
   "Bucholtz, Herkules, 1659: 'dürffte es nicht wol ablauffen'; 'alles ... wol abgelauffen'",
   "Ordinari Postzeitung Nr. 23, 1668: 'Tractaten zu Turin wol ablauffen werden'",
   "Nordischer Mercurius (Hamburg), 1673: 'der Reußische Land-Tag ... wol abgelauffen sey'",
   "Hohberg, Georgica Curiosa, 1682: 'sondern wol ablauffen möge'",
   "Happel, Academischer Roman, 1690: 'wann der Actus wol ablauffet'; 'nicht wol ablauffen würde'",
   "Weise, Der freymüthige und höfliche Redner, 1693: 'daß sie wol abläufft'"],
  "exact_formula_gott_geb_dass_wol_ablauff": "NOT FOUND. DTA NEAR(geb*,ablauff*,10): 9 hits, none a wish formula. "
     "Web search (Google) for 'Gott geb(e)' + 'wol ablauffe/ablauffen möge': nothing. "
     "Closest: 'Gott geb daß es wol gehalten werde' (Relation 1609); 'Gott gebe daß alles gereiche zu vnserem Trost' (Zwinger 1633); "
     "'GOtt gebe daß es nach Wunsch aller Interessirenden Partheyen abgehen möge' (Rigische Novellen 1699); "
     "'es soll doch noch wol ablauffen' (Lütkemann 1652); 'wol ablauffen möge' (Hohberg 1682).",
  "apocopated_ablauff_as_verb": "DTA @ablauff: 18 hits, ALL the noun 'der Ablauff'. '\"wol @ablauff\" || \"wohl @ablauff\"': 0 hits. "
     "So the apocopated 3sg subjunctive 'ablauff' is itself unattested in DTA; only 'ablauffe' is.",
  "dictionaries": "Grimm DWB 'ablaufen' (via dwds.de/wb/dwb/ablaufen): sense 'turn out' only with Goethe/Klopstock quotations ('es ist wol oder übel damit abgelaufen'). "
     "FWB 'ablaufen' (fwb-online.de/lemma/ablaufen.s.3vu): sense 8 'ablaufen, verlaufen, vonstatten gehen' (Amadis 1571; steir. Taidinge 1680); no 'wol/übel ablaufen' phrase."
 },
 "Q2_apocope": {
  "gott_geb_exact": "DTA '\"Gott @geb\"': 209 hits total; dozens 1600-1720 (Dannhauer 1653-1673 sermons, Grimmelshausen 1669, Albertinus 1615, Crüger 1631 'Gott geb das meine beysorge fehle', Wülfer 1656, Scheuchzer 1707 ...). Mostly sermons, novels, verse; one letter (Marperger 1715); no chancery text seen.",
  "gott_gebe_dass": "DTA '\"Gott geb daß\"' (lemma): 36 hits, 27 'gebe', 3 'geb' (Relation 1609, Dannhauer 1653, Grimmelshausen 1669).",
  "local_corpus": "geb 11 vs gebe 110; woll 20 vs wolle 190; helff 2 vs helffe 8. Apocopated 'gott geb' 7x (Grimmelshausen 1669), 'geb gott/ dass' 1x (Wartmann 1652).",
  "other_verbs_es_geh_komm_bleib": "DTA 74 hits; 1640-1720 overwhelmingly verse/hymn; prose: Arnold 1700 'es komm für Obrigkeit', Morhof 1682, Schupp 1663 'es geh viel auf sein Pferd', Lütkemann 1652 'Es bleib aber dabey', Bauller 1681.",
  "es_lauff_exact": "DTA '\"es @lauff\" || \"wol @lauff\" || \"wohl @lauff\"': 1 hit, Etschenreutter 1571 'ettlich es lauff uber bley' (3sg subj., prose).",
  "internal_evidence": "In the cipher sentence itself 63 38 22 = g e b (no -e): the writer apocopates the subjunctive of geben in this very clause, so an apocopated 'ablauff' would be consistent with his own usage."
 },
 "Q3_ablauu": {
  "dta_exact_tokens": "@ablau, @ablauu, @ablauw: 0 hits; @lauu, @ablaw, @blauu: 0 hits.",
  "local_corpus": "ablauu 0; 'lauu' 0; word-final -uu 0; 'au u' 0; 'blau u' 0; 'ab lau' 0.",
  "manuscript_context": "Unretouched crop (work/ending-alternative-p2-terminal-2026-10-28.png): the disputed pair is followed by two dots, a gap, then cleartext in the main hand; the enciphered word ends there, so 'ablauu' would have to be a complete word.",
  "segmentations_considered": "'ablau u', 'a blau u', 'ab lau u', 'abl au u', 'ablau v/w' (u-v-w interchange): none is a word or phrase in period German; 'u.' as abbreviation for 'und' is a manuscript convention for cleartext, not for an enciphered homophone XX."
 },
 "Q4_all_vs_alles": {
  "dta_exact": "'\"@all @wol\"': 10 hits all centuries, pronominal 'all'=alles only Scriver 1672 (Magdeburg) 'GOtt Lob all wol / nur daß ich matt bin', Sattler 1608 'er siehe all wol', Musäus 1779. '\"@alles @wol\"': 1211 hits.",
  "local_corpus": "'all' 128 tokens, essentially all attributive (all sein, all jhr, all zu); pronominal 'all'+'wol' 0; 'alles wol' 12; 'das all wol' 0; 'das alles wol' 0.",
  "grimm": "DWB 'all': uninflected 'all' before article ('all das leid'); 'alle wol, ganz wol' only as adverb (Ettner); no 17th-c. pronominal 'all'=alles example quoted.",
  "note": "Pronominal 'all' for 'alles' is rare in High German prose (c. 1:100 vs 'alles wol') but attested, incl. a 1672 northern text; it is normal in Low German ('all'), relevant for a writer in Hamburg. The annotator's gloss reads 'amm', not 'all'."
 }
}
out["external_attestations"] = EXTERNAL

with open(os.path.join(HERE, "language-passage2.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

# console summary
print("corpus chars", total)
print("ablaufen word forms:", forms.most_common(30))
for k in ("ablauff_kwic", "ablauff_sense_turnout", "wol_ablauff_formula", "gott_geb_dass"):
    print("\n==", k, out[k]["count"])
    for h in out[k]["examples"][:25]:
        print("  ", h["text"], "|", h["kwic"])
print("\n== gott geb vs gebe")
for k, v in out["gott_geb_vs_gebe"].items():
    print("  ", k, v["count"])
    for h in v["examples"][:6]:
        print("      ", h["text"], "|", h["kwic"])
print("\n== subj apocope counts (sum)")
for k, v in out["subj_apocope_counts"].items():
    print("  ", k, sum(v.values()))
print("\n== ablauu")
for k, v in out["ablauu_any"].items():
    print("  ", k, v["count"])
    for h in v["examples"][:5]:
        print("      ", h["text"], "|", h["kwic"])
print("blau", sum(out["blau_word"].values()), "lau", sum(out["lau_word"].values()))
print("\n== all vs alles")
for k, v in out["all_vs_alles"].items():
    if "count" in v:
        print("  ", k, v["count"])
        for h in v["examples"][:8]:
            print("      ", h["text"], "|", h["kwic"])
    else:
        print("  ", k, {kk: sum(vv.values()) for kk, vv in v.items()})
