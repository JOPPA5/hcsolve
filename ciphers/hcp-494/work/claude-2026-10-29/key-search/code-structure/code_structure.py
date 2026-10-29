#!/usr/bin/env python3 -I
"""Structure of the 1672 Lincker nomenclator as far as the 26 code occurrences allow.

Usage:  python3 -I code_structure.py /path/to/source/bourdeau/codes.txt

Reads only the solver's transcription (page, code, literal gloss, reading, grade) and
prints (1) the occurrence table, (2) tests of candidate ordering models, (3) the
block model with its predictions and (4) a ten-second screening criterion.
Nothing is written. No source file is modified.
"""
import re
import sys
from collections import OrderedDict, Counter

# ---------------------------------------------------------------- input
path = sys.argv[1] if len(sys.argv) > 1 else "codes.txt"
rows = []
with open(path, encoding="utf-8") as fh:
    for line in fh:
        if not line.strip() or line.startswith("#"):
            continue
        m = re.match(r"(\S+)\s+(\d+)\s+(.*?)\s{2,}(\S.*?)\s{2,}([HCMI] .*|[HCMI])\s*$", line.rstrip("\n"))
        if not m:
            raise SystemExit("unparsed line: " + line)
        page, code, gloss, reading, grade = m.groups()
        rows.append(dict(page=page, code=int(code), gloss=gloss, reading=reading, grade=grade))
assert len(rows) == 26, len(rows)

# Preferred transcription (NOTES.md, work/427-vs-447.png): occurrence 21 is 427, not 447.
rows[20]["code_pref"] = 427
rows[20]["note"] = "Bourdeau 447; solver prefers 427 (curved 2); awaits palaeographic review"
for r in rows:
    r.setdefault("code_pref", r["code"])
    r.setdefault("note", "")

# Syntactic use in the clear text (from source/bourdeau/reading.txt), independent of the gloss.
usage = {
    1: "temporal: 'zu der Zeit der <630> gegenwart' -> person",
    2: "'Missverstaendnis zwischen <601> und <651>' -> party",
    3: "'zwischen <601> und <651>' -> party",
    4: "'hat <625> ... dienste gethan' -> person (subject)",
    5: "'das er an <653> hat empfangen' -> party/court",
    6: "'in <829>' -> place (locative)",
    7: "'nach <651> gehet' -> place/court (directional)",
    8: "'<630> abfertigung' -> person (genitive)",
    9: "'<774>' -> party",
    10: "'wan <775>' -> party (plural body)",
    11: "'<601> seinen respect anthut' -> person (sovereign)",
    12: "'dass <576> mit <768> geschlossen' -> power",
    13: "'<576> mit <768> geschlossen' -> power",
    14: "'<601> vorbeygangen' -> power",
    15: "'<625> wird ... zu <829> gehen' -> person (subject)",
    16: "'zu <829> gehen' -> place (directional)",
    17: "'dass <651> in das Foedus ... eingezogen werde' -> party",
    18: "'in <634>' -> territory (locative)",
    19: "'in <601> Adell, Buerger und Bauern' -> country (locative)",
    20: "'insidiosus hostis <768>' (Latin clause) -> power",
    21: "'Der selbige <427> <641>' -> title + name ('Herzog von Ploen')",
    22: "'<427> <641> war auch zu Hamburg' -> name of the duke's house/seat",
    23: "'eine estroite <303> zwischen' -> feminine noun = alliance",
    24: "'zwischen <447> <602> und <834>' -> first party, two codes",
    25: "'zwischen <447> <602> und <834>' -> first party, two codes",
    26: "'und <834> unter Handen' -> second party",
}

# ---------------------------------------------------------------- (1) table
print("=" * 100)
print("(1) The 26 code occurrences, in order (source/bourdeau/codes.txt; preferred code in brackets)")
print("=" * 100)
hdr = f"{'#':>2} {'page':4} {'code':>5} {'blk':>3} {'grade':5} {'literal gloss on the leaf':44} {'syntactic use in the clear text'}"
print(hdr)
print("-" * len(hdr))
for i, r in enumerate(rows, 1):
    code = r["code"] if r["code_pref"] == r["code"] else f"{r['code']}[{r['code_pref']}]"
    blk = r["code_pref"] // 100 * 100
    print(f"{i:>2} {r['page']:4} {code:>5} {blk:>3} {r['grade']:5} {r['gloss'][:44]:44} {usage[i]}")

# ---------------------------------------------------------------- distinct codes
value = OrderedDict([
    (303, ("alliance", "vocabulary", "gloss")),
    (427, ("Herzog (title, with 641)", "title", "gloss (as 447 in codes.txt; 427 preferred)")),
    (447, ("? (pair 447 602 glossed 'Kayser'; 'Hauss Braunschw.' struck)", "title/qualifier?", "unresolved")),
    (576, ("Frankreich", "power", "gloss")),
    (601, ("Dennemarck / Koenig in Dennemarck", "power", "gloss x4")),
    (602, ("? ('Kayser' written where 'Braunschw.' was struck)", "power?", "gloss, allocation open")),
    (625, ("Statthalter [Ahlefeldt]?", "person", "margin gloss, hard to read")),
    (630, ("Blumenthal", "person", "gloss x2")),
    (634, ("Holstein", "territory", "margin gloss")),
    (641, ("Ploen", "territory/seat", "gloss")),
    (651, ("Churbrandenburg", "power", "gloss x3")),
    (653, ("Cur Brandenb.", "power", "gloss")),
    (768, ("Schweden / Sueco", "power", "gloss x2")),
    (774, ("Hollandt", "power", "gloss")),
    (775, ("Gen. Staden (General Staaten)", "power", "gloss")),
    (829, ("Berlin", "place", "gloss x2")),
    (834, ("Rex Daniae ('Rey Danae')", "sovereign", "gloss")),
])
cnt = Counter(r["code_pref"] for r in rows)
print()
print("Distinct codes (preferred transcription):", len(value), "; tokens:", sum(cnt.values()))
for c, (v, cat, src) in value.items():
    print(f"  {c:>4} x{cnt[c]}  {cat:16} {v:58} [{src}]")

# ---------------------------------------------------------------- (2) model tests
print()
print("=" * 100)
print("(2) Ordering models tested against the glossed values")
print("=" * 100)

# (a) one alphabetical dictionary with names interleaved (the 1236 French-dictionary type)
alpha_key = {303: "alliance", 427: "herzog", 576: "frankreich", 601: "dennemarck", 625: "statthalter",
             630: "blumenthal", 634: "holstein", 641: "ploen", 651: "churbrandenburg", 768: "schweden",
             774: "hollandt", 775: "generalstaaten", 829: "berlin", 834: "rexdaniae"}
codes_sorted = sorted(alpha_key)
inv = [(a, b) for i, a in enumerate(codes_sorted) for b in codes_sorted[i + 1:]
       if alpha_key[a][0] > alpha_key[b][0]]
print(f"(a) Single alphabetical list: {len(inv)} inversions among {len(codes_sorted)} glossed codes "
      f"(e.g. {inv[0][0]} {alpha_key[inv[0][0]]} < {inv[0][1]} {alpha_key[inv[0][1]]}).  -> REJECTED")
print("    (unless several glosses are wrong; 834 would be 'koenig'/'rex' and still invert with 829 berlin)")

# (b) key 255 rank order (sovereigns: Kayser, Frankreich, Spanien, Schweden, Dennemarck, Engelland, ...,
#     Hollaender; countries: Teutschland, Reich, Frankreich, Spanien, Portugal, Engelland, Hollandt ...)
order255_sov = ["kayser", "frankreich", "spanien", "schweden", "dennemarck", "engelland", "polen",
                "moscowiter", "cossaggen", "hollaender", "venetianer"]
pairs = [("frankreich", 576), ("dennemarck", 601), ("schweden", 768), ("hollaender", 774)]
viol = [(na, nb) for i, (na, ca) in enumerate(pairs) for (nb, cb) in pairs[i + 1:]
        if (order255_sov.index(na) < order255_sov.index(nb)) != (ca < cb)]
print(f"(b) Key-255 sovereign order applied to the 1672 powers: {len(viol)} violation(s) {viol}  -> REJECTED")
print("    (255 has Schweden 183 before Dennemarck 184; 1672 has Dennemarck 601 before Schweden 768)")

# (c) appendix model: 255 list unchanged (180-407) + supplement numbered above 407
inside = [c for c in value if 180 <= c <= 407]
print(f"(c) '255 unchanged + appendix >407': codes inside 180-407 = {inside}; 303 = Muenster in 255 but the "
      f"clear text needs a feminine noun ('eine estroite 303') = alliance (255: 311).")
print("    Also the writer never used an available 255 code (Frankreich 228, Hollandt 232, Holstein 253, "
      "Dennemarck 184/212 all exist) but always a >407 code.  -> REJECTED (one contradiction + 4/4 avoidance)")

# (d) hundreds as category blocks
blocks = OrderedDict()
for c, (v, cat, src) in value.items():
    blocks.setdefault(c // 100 * 100, []).append((c, v.split(" (")[0], cat))
print("(d) Hundreds blocks and their glossed content:")
for b, items in blocks.items():
    toks = sum(cnt[c] for c, _, _ in items)
    print(f"    {b}-{b+99}: {toks:2} tokens, {len(items)} codes: " + "; ".join(f"{c} {v}" for c, v, _ in items))
print("    Within 600-653 every referent belongs to the Danish-Brandenburg negotiation of spring 1672"
      " (Denmark, [Emperor], Statthalter, Blumenthal, Holstein, Ploen, Brandenburg x2):")
print("    15 of 26 tokens fall in this one block. No proper-name block is alphabetical "
      "(600: D K S B H P C; 700: S H G).  -> BEST SUPPORTED: purpose-built topical blocks")

# ---------------------------------------------------------------- (3) predictions
print()
print("=" * 100)
print("(3) Block model and predictions")
print("=" * 100)
print("""
  300-3xx  vocabulary, alphabetical (303 = alliance; key 255 has Action 309, Allijrte 310, Alliance 311,
           i.e. the same A-words at the head of its vocabulary block; key 253's list also starts at 300)
  400-4xx  titles / generic designations (427 Herzog; 447 the first half of a two-code designation of
           the Emperor, cf. 427+641 = 'Herzog [von] Ploen' built the same way: title + name)
  500-5xx  other powers or lands (576 Frankreich; a long block, Frankreich is entry 76)
  600-6xx  the negotiation block: 601 Dennemarck, 602 [Kayser], ~625 Statthalter (Ahlefeldt), 630 Blumenthal,
           634 Holstein, 641 Ploen, 651 and 653 Churbrandenburg (two codes: Churfuerst / Brandenburg, or
           homophones as in HCP 280's doubled entries)
  700-7xx  northern/maritime powers (768 Schweden, 774 Hollandt, 775 General Staaten adjacent)
  800-8xx  829 Berlin, 834 Rex Daniae: either a towns block containing an added sovereign homophone,
           or a supplement of frequently needed items (cf. HCP 267: King of Denmark 235/338/583)

  601 vs 834: compatible. 601 is used locatively ('in <601> Adell, Buerger und Bauern') and as a party;
           834 only as a party next to the Emperor. The 834 gloss literally reads 'Rey Danae' in black ink
           (crop gloss-834-crop-x3.png): Latin 'Rex Dan[iae]', not a town name. Country vs sovereign as
           separate entries is the norm in this family (255: 184 Koen. Dennemarck / 212 Dennemarck;
           266: Dennemarck 185 + king; 280: 532/533 vs 534/535). No re-examination of 834 is needed;
           the consequence is only that 601 = 'Dennemarck' (country/crown), not 'Koenig'.
  602:     the correction 'Kayser' is written where the struck 'Braunschw[eig]' stood, i.e. over 602
           (crop gloss-447-602-crop-x3.png); the struck 'Hauss' stood over 447. So the glosser's two
           readings both treat 447 602 as <word> <name>. Prediction: 602 = Kayser (or Roemischer Kayser /
           Oesterreich) as the SECOND entry of a non-alphabetical parties block that opens with Dennemarck.
           447 is then a qualifier or title (Roemisch[er], Kayserlich, Haus, Ihro...), 20 entries after
           Herzog 427 in a 400 block that may itself be alphabetical (H ... R fits ~20 entries).
  427 vs 447: two different entries; the block model does not require 447 = Herzog. If an independent
           reviewer upholds 447 at occurrence 21, then 447 = Herzog and 602 = a house the glosser first
           called Braunschweig and then Kayser - the weaker reading, because the Dano-Brunswick alliance
           was already concluded on 31 March 1672 and the alliance 'unter Handen' on 4 May was Denmark-Emperor.
""")

# ---------------------------------------------------------------- (4) screening
print("=" * 100)
print("(4) Ten-second screening criterion for any candidate key scan")
print("=" * 100)
print("""
  MATCH if the list has numbered entries above 800 AND entry 601 reads Dennemarck/Daenemark
  (602 Kayser/Roem. Kayser/Oesterreich beside it) AND 634 = Holstein or 651 = Churbrandenburg.
  Supporting: 303 = Alliance at the head of an alphabetical German/French vocabulary that starts at 300;
  768 = Schweden; 829 = Berlin; 641 = Ploen; a 'Statthalter' entry in the 620s.
  REJECT on sight if: entries are one alphabetical run with names interleaved; numbering stops below 834;
  601/634/651 are vocabulary words or syllables; 601 is 'le Pretendant'/'Gnad' (the 1236 lists);
  the sheet is a French 'Chiffre pour M. ...' with four-digit groups.
  Physical expectation: a German two-column list with dash leaders in the 1666 Kanzlei hand of 255's
  pages 14-16, 500+ entries (300-8xx), so 7-9 such pages, probably endorsed for Secretarius Lincker and
  the Daenemark / Hamburg mission 1672; look in HStAM 4 f Staaten D Daenemark (the mission file) and in
  4 d 1234-1236 for sheets whose first column starts at 300 rather than 180.
""")
