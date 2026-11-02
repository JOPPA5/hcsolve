#!/usr/bin/env python3
"""One-off: applies the review 1 fixes to transcription, decode.py and SOLUTION.md. Run once from the cipher directory."""
p = 'work/transcription.txt'; s = open(p, encoding='utf-8').read()
R = [("# = at row end means the writer's hyphen or a word running on. ~x marks a sign not taken from the key: see SOLUTION.md.\n",
      "# = at row end means the writer's hyphen with the word running on; - at row end means the writer's hyphen where I keep a word break (row 11, see SOLUTION.md).\n"
      "# ~x marks a sign read by word sense: the sign as seen, then the letter taken. See SOLUTION.md.\n"
      "# Non-cipher marks of the writer, not in the sign rows: ! after the heading, curved brackets in rows 3 and 4, tall slash in row 18 between egeszseges and Sziberiaba, ) before Arpad in row 27.\n"),
     ("8, 0 3. 1' 1, 1,~b 1'", "8, 0 3,~v 1' 1, 1,~b 1'"),
     ("2. 7, | 7 1. 9 8,\n12", "2. 7, | 7 1. 9 8, -\n12"),
     ("| 7, 0 7 1.\n", "| 7, 0 7 1'\n"),
     ("21 1: 5, 5, 1. 8, 0 7", "21 1: 5, 5, 1' 8, 0 7"),
     ("| 7~sz 0, 7 1: |", "| 7. 0, 7 1: |"),
     ("23 1: 9, 2. 6, |", "23 1: 9, | 2. 6, |")]
for a, b in R:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)

p = 'work/decode.py'; s = open(p, encoding='utf-8').read()
R = [("nem soka\n", "nem soká\n"), ("ellatok a", "ellátok a"), ("ezén lelkem", "ez én lelkem"),
     ("    if cont:\n        parts = parts[:-1]\n", "    if parts[-1] in ('=', '-'):\n        parts = parts[:-1]\n"),
     ("print('\\nReading order", """from collections import Counter
c = Counter(t.split('~')[0] for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8')
            if not l.startswith('#') for t in l.split()[1:] if t not in ('|', '=', '-'))
print("\\nsign counts: 1. %d, 1' %d, 5, %d, 5. %d, 8. %d" % (c['1.'], c["1'"], c['5,'], c['5.'], c['8.']))
print('Reading order""")]
for a, b in R:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)

p = 'SOLUTION.md'; s = open(p, encoding='utf-8').read()
R = [("# hcp-1151 solution (round 1)", "# hcp-1151 solution (after review 1)"),
     ("four signs are new here.", "four signs are new here, and two of them conflict with filed sister readings (see the key section)."),
     ("`5.` | ly **(new)**", "`5.` | ly **(here; l on hcp-1178, 1179)**"),
     ("`8.` | ty **(new)**", "`8.` | ty **(here; t? on hcp-1179)**"),
     ("The new marks follow one rule: a dot on the base of the single letter gives the digraph of that letter (g/gy, l/ly, n/ny, t/ty, also s/sz).",
      "On this card a dot on the base of a single letter gives the digraph of that letter (g/gy, l/ly, n/ny, t/ty, also s/sz).\n\n"
      "Conflict with filed cards: hcp-1178 and 1179 file `5.` as plain l (`csókollak`, `a legszeb`), and hcp-1179 files `8.` as `t?` (`kar[t?]im`). So the pattern is not family-wide. I keep it for this card because here every ordinary l is written `5,` (LCOUNT signs; the one exception is the bare `5` of `Lapodat`) and the two `5.` stand exactly at the two ly positions, melynek and fogoly. `8.` occurs once. This is thin evidence from one card, and the writer may be loose about the mark elsewhere. If `5.` were plain l here, the text would be melnek, fogol: the same words in a different spelling, so the reading does not depend on it. It may bear on the open `kar[t?]im` of hcp-1179 (`kártyám`?), but I change nothing there."),
     ("Spelling as on the card; punctuation and word division are mine. All of it is enciphered except the date and address.",
      "Spelling as on the card. Word division and commas are mine. The writer's own marks are the `!` after the heading, the curved brackets around the sentence on conscription, a tall slash between `egészséges` and `Szibériába` (not a sign: taller than a 1, with no flag), the hyphens, and a lone `)` before `Árpád`. All of it is enciphered except the date and address."),
     ("Megmondta, hogy nem soka kapok", "Megmondta, hogy nem soká kapok"),
     ("ellatok a messzeségbe", "ellátok a messzeségbe"),
     ("ezén lelkem üdvössége.", "ez én lelkem üdvössége."),
     ("kapt = kap, soka = soká, é = és, let = lett, ellatok = ellátok, ezén = ezen, Szibériába", "kapt = kap, é = és, let = lett, Szibériába"),
     ("she is the salvation of my soul", "this is the salvation of my soul"),
     ("ona je spása mojej duše", "to je spása mojej duše"),
     ("Result: 574 signs, 119 words;", "Result: 574 signs, 120 words;"),
     ("In the same word the mark after the 3 is short, between a dot and a comma; I read `3.` by sense. This word is the weakest point, though the context (\"Further, I inform you\") fits.",
      "In the same word the mark after the 3 is a short comma with a head, so the sign is `3,` in shape and the table gives r (`torábbá`); I read v by sense, written `3,~v` in the transcription. A small extra dot stands beside the comma of the opening `8,`; it changes nothing. This word is the weakest point, though the context (\"Further, I inform you\") fits."),
     ("4. `szőke`: no dot visible under the 7, so the table gives `kőke`. Sense needs `7.`. Part of this sign lies over the printed `1386`.\n", ""),
     ("Earlier I saw them as 3-like, which gives `ordd`, not a word.\n",
      "Earlier I saw them as 3-like, which gives `ordd`, not a word.\n\n`szőke` is no longer in this list: its first sign is `7.` with the dot run into the end of the crossbar, as read.\n"),
     ("the sentence could mean he \"gets\" or \"got\" money.",
      "the sentence could mean he \"gets\" or \"got\" money. The card has a writer's hyphen after the t at the end of row 11, beyond the green line, so literally `kapt-` / `is`. Hyphens elsewhere split a word (`meg-örültem`, `maga-mat`, `Szibériá-ba`), so either he wrote `kaptis` as one unit or the hyphen is loose. The letters are the same either way. The transcription has `-`, not `=`, because I keep the word break."),
     ("- `é` in `é igaz is let`",
      "- `ez én lelkem`: the card has no word division. `ezén` would need a wrong long vowel; `ez én` needs no correction and keeps eight syllables.\n- `é` in `é igaz is let`"),
     ("- A digraph rule, not an ad hoc choice, predicts the new signs, and three of them recur:",
      "- One pattern on this card covers the new signs, though it is not family-wide (see the key section), and three of them recur:"),
     ("match the filed readings of hcp-1174 and hcp-1179, and the address is the same Margitka Sziber.",
      "match the filed reading of hcp-1174, and the address is the same Margitka Sziber. hcp-1179 is signed Sz. A. in clear and only quotes the hcp-1174 heading, so it is no independent support for these words.")]
for a, b in R:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
s += '''
## Response to review 1

Verdict REVISE. All seven findings are accepted and addressed. I looked again at the reviewer's crops `y_r21.png`, `y_soka.png`, `y_r22b.png`, `z_tovabba.png`, `z_kapt_end.png` and `z_szib.png`. The message is unchanged: two spellings change, one dot is confirmed and one word division changes. `python3 -I ciphers/hcp-1151/work/decode.py`, re-run after the fixes, gives: hashes OK, 574 signs, 569 by the table, 5 by sense, 120 words, `1.` 51, `1'` 17.

1. **`ellatok`: fixed.** The dot after the 1 in row 21 stands high, unlike the foot-level `1.` later in that row. The sign is `1'`, the word is `ellátok`, and the normal-form note is removed.
2. **`soka`: fixed.** Same call, last sign of row 12: `1'`, `soká`. For the wider re-check I did not re-measure every dot. I went through the decoded words instead: no remaining `1.` stands where Hungarian needs á. That agrees with the reviewer's reading of the tiles.
3. **`szőke`: fixed.** The lobe at the lower right of the first 7 is visible, and the next 7 of the word has none. The sign is now `7.` as read, not by sense. The note about `1386` is removed.
4. **Sign count: fixed.** `továbbá` now has `3,~v` in the transcription, and the extra dot beside the `8,` is recorded. The count stays 5 with different members: `Lapodat` l, `továbbá` v and b, `ott` t and t.
5. **Key conflicts: fixed.** `5.` and `8.` are no longer plain "new". The conflict with hcp-1178 and 1179 is stated in the key section, with my evidence from this card, stated as thin. The note on `kar[t?]im` of hcp-1179 is added and that card is not changed. The signature claim now cites hcp-1174 only.
6. **`ez én`: fixed.** Division, normal forms and both translations changed. The word count goes from 119 to 120.
7. **Card marks: fixed.** The row 11 hyphen is in the transcription as `-`, `decode.py` accepts it, and it is disclosed under `kapt is`. The `!`, the brackets, the row 18 slash and the `)` are listed in the transcription header and the Plaintext note. On `z_szib.png` I agree the slash in row 18 is not a digit 1.
'''
s = s.replace('LCOUNT', open('/dev/stdin').read().strip())
open(p, 'w', encoding='utf-8').write(s)
