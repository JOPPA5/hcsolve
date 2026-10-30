# HCP1293 — Feri to Jolánka Tóth: apology for a missed meeting after a long duty

**Status: complete reading; review 1 (REVISE) addressed, see the last section.** Claude Opus 5.5, 2026-10-30. No earlier work on this number. Key from the finished family cards; no published solution found; the portal shows *Not solved* with no attached transcription or solution.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, same key as finished card HCP1216 (key table in `ciphers/hcp-1216/SOLUTION.md`; also 1212, 1213, 1217, 1218, 1243, 1301). Every value was confirmed here by the words of this card, none had to be changed.

Card-specific habits: *gy* is written as two signs g + y (not the joined digraph of 1216, except that the two touch); *o* (plain loop) and *i* (loop with a crossing stroke and a dot or tick above) are close, the mark deciding; *ö* has two dots. Writer's *j* stands for *ly* (*ojan*, *ijen*).

Layout: 23 rows on the message half, row 23 running along the bottom of the whole card; it turns the corner and runs **up the right edge** (E1); at the top right an arrow leads on to the **top margin, upside down, right to left** (T1); that ends at a ruled box, where the card is turned once more: **two short rows in the box** (B1, B2), read with the card turned 90° counter-clockwise. A signature block of six short rows sits **in the stamp square** (S1–S6), upright, partly under the printed green triangle.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1293/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (one token per written sign) and prints the literal rows and `work/normalized.txt`. The ledger is a manual transcription from the pixels of `work/hires/*adr.jpg`; `work/crop.py` regenerates the crops into `work/tiles/` (it needs PIL and numpy). The script and the ledger are the only sources of the output: there is no OCR.

## Literal decipherment

```
01 szeretetedesegyetlen            13 mentemszolgalatba
02 remenyemneharagudjonram         14 esepenbeleptemmarszo
03 hogyojansokavarakoz             15 litottakisanevem
04 tattamdeijensokameg             16 esrögtöneluttam
05 sohasemtartottavezen            17 mitnemiskelmonda
06 lesmintmostmikorvege            18 nomdragacsillagom
07 voltelmentemenedesem            19 aligvaromhogy
08 magatkerestemdenemta            20 viszszajöjeklegjobb
09 laltamesaztgondol               21 szeretnekedesemezalatta
10 tamedesemhogyhaza               22 arövididoalatmindig
11 mentekdesenishazamen            23 maletalenikerjekibocsanatomathogyelsembu
12 tematöltöztemes                 E1 csuztamviszontlatasramikora
T1 mikorigerthavalamil   B1 közbe   B2 nemjön
S1-6 csoko lom szam talan szor feri
```

Rows 04 (*de*) and 14 (*épen*, *beléptem*) print the letter read by sense; the written shapes are given in Uncertainty 1.

## Hungarian (normalized)

Szeretett édes egyetlen reményem! Ne haragudjon rám, hogy olyan soká várakoztattam, de ilyen soká még soha sem tartott a vezén[y]lés, mint most. Mikor vége volt, elmentem én, édesem, magát kerestem, de nem találtam, és azt gondoltam, édesem, hogy hazamentek, de [s] én is hazamentem, átöltöztem és mentem szolgálatba, és éppen beléptem, már szólítottak is a nevem[en], és rögtön el[f]uttam. Mit nem is kell mondanom, drága csillagom, alig várom, hogy visszajöjjék. Legjobb[an] szeretnék, édesem, ez alatt a rövid idő alatt mindig mellette le[n]ni. Kérje ki bocsánatomat, hogy el sem búcsúztam. Viszontlátásra, mikor[ra] – mikor ígért, ha valami[l] közbe nem jön.

Csókolom számtalanszor. Feri

## English

Beloved sweet, my only hope! Do not be angry with me for keeping you waiting so long, but the duty assignment has never lasted as long as it did now. When it was over I went off, my darling, and looked for you, but did not find you, and I thought, my darling, that you had gone home, so I too went home, changed and went on duty, and just as I walked in they were already calling my name, and I ran off at once. I need hardly tell you, dear star of mine, that I can scarcely wait for you to come back. Most of all, my darling, I would like to be beside you all the time during this short while. Please ask pardon for me that I did not even say goodbye. Until we meet again, when you promised, if nothing comes up.
I kiss you countless times. Feri

## Slovak

Milovaná sladká, moja jediná nádej! Nehnevajte sa na mňa, že som Vás nechal tak dlho čakať, ale ešte nikdy netrvala služba tak dlho ako teraz. Keď sa skončila, odišiel som, drahá, hľadal som Vás, ale nenašiel som Vás, a myslel som si, drahá, že ste odišli domov, nuž aj ja som šiel domov, prezliekol som sa a šiel do služby, a práve keď som vošiel, už ma volali po mene, a hneď som odbehol. Ani Vám nemusím hovoriť, drahá hviezdička moja, že sa sotva dočkám, kým sa vrátite. Najradšej by som bol, drahá, počas tohto krátkeho času stále pri Vás. Poproste za mňa o odpustenie, že som sa ani nerozlúčil. Dovidenia, kedy ste sľúbili, ak do toho nič nepríde.
Bozkávam Vás nespočetnekrát. Feri

## Uncertainties

Sign values that rest on word sense:

1. **h / p / d family (corrected after review 1).** On this card h has the short tick on the **right** of the tall stroke (rows 3, 5, 10, 11), d on the **left** (rows 10, 21). Both p of row 14 (*épen*, *beléptem*) have the **d** shape: taken literally the words would be *eden*, *beledtem*. They are read as p by sense, against the shape. No undisputed p occurs on this card to compare. Row 4 *de* has the **h** shape, tick on the right, and is read d by sense (*he ijen* gives no word); the same slip is on HCP1216 row 5. So three signs rest on sense here; the ledger marks them `:shape-H` and `:shape-D`.
2. **Row 6 *mikor*:** the k is an S-sign whose lower bowl is closed, near the b sign; b gives no word.
3. **Row 8 *kerestem*:** the second e is three bars joined at the sides into a loop, not a clean e.
4. **Row 21 end, row 22 start:** *alatta* + row 22 *a*: the end of row 21 is rubbed and faint from *alatt* on, the last "a" faintest; the reading has one a too many (*ez alatt a a rövid*), deleted in normalization as a line-end repeat. The number of gamma signs (the *tt*) cannot be counted on the rubbed surface; TT in the ledger is a sense reading.
5. **Row 22 *idő*:** the ő is a loop overwritten by bar-like strokes; *o* in the ledger, ő by sense.
6. **Row 8 *magát*:** g and a lie in a moisture stain, still legible. **Row 11 k of *mentek*** is dark and swollen from the same kind of wetting of the indelible pencil; its S-form is readable and k is the sense.

Writer's text kept literal and normalized by me:

7. **Row 11 *de s én is*:** literal *desenis*. The sign after *de* is a bowl with a faint left side, read s. I take *de s én is* ("but so I too"), an odd but possible pleonasm; the s is printed in brackets as not needed. An alternative raised in review: the blot before *desen* is the most damaged sign of the card, and if it is a cancelled or overwritten sign, *hazament, édes, én is hazamentem* ("had gone home, sweet, I too went home") is possible; *édes* is his word in row 1. The sense is the same apart from the person of the verb; the signs do not decide. *Mentek* as written is plural, which suggests she was with others (see item 14).
8. **Row 7 *elmentem en*:** word division is mine; literal *elmentemenedesem*.
9. **Row 15 *a nevem*:** normalized *a nevem[en]* ("by my name"); the -en is not on the card.
10. **Row 5/6 *vezén[y]lés*:** the y is not on the card (row 5 ends *vezen*, row 6 begins *les*). **Row 16 *eluttam*:** literal, all signs clear. Normalized as *el[f]uttam* (colloquial for *elfutottam*, "I ran off"); the f is not on the card. If the writer meant another verb, the sense of the clause changes slightly, not of the letter.
11. **Row 20 *viszszajöjek*:** accents are not visible, so *visszajöjjék* ("that you come back") and *visszajöjjek* ("that I come back") are both possible. I chose the former because the end of the card speaks of a meeting she promised. Single j is the writer's.
12. **Row 20 *legjobb*:** normalized *legjobb[an]*, starting the next sentence.
13. **Row 23 *maleta leni*:** literal m-a-l-e-t-a l-e-n-i, normalized *mellette le[n]ni* ("to be beside you"). Only one pair of strokes stands in *leni*; the second n is supplied, like the writer's other single-for-double spellings (*szeretet*, *alat*). The two a-signs stand where standard spelling has e; the row touches the card edge, so a lost third bar is possible for the second one, not for the first with certainty.
14. **Row 23 *kérje ki bocsánatomat* (changed after review 1):** the letters are k-e-r-j-e-k-i. The division *kérje ki* ("ask out, obtain", 3rd-person formal imperative, like *ne haragudjon* in row 2) leaves no meaningless sign and explains the possessive *-omat* ("my pardon"): he asks her to apologise for him, presumably to the people who went home with her (plural *hazamentek*, item 7). This is the preferred reading, not a certainty: *kikér* with *bocsánat* is not the usual phrase, and a native reader should judge it. The earlier division *kérjek i bocsánatomat* ("let me ask your forgiveness", with a stray i and an unexplained *-omat*) stays as the alternative.
15. **E1/T1:** the right edge ends in *mikora*, and after the arrow the top margin begins *mikor* again. I read a restart or *mikorra*; both are shown in the normalization.
16. **T1 final sign:** a wave (l) stands after *valami*, touching the box line. It makes no word (*valamil*); it may be a slip or flourish, dropped in normalization. *Közbe* has its two dots, just under the ruling (found in review).
17. **S3–S5** lie partly under the green triangle; they were read on a blue-minus-green image, which separates the pencil from the print (`work/crop.py`, tiles p1, p2). No sign there is restored.

Every letter in the ledger corresponds to a written sign. Letters the writer left out are supplied only in the normalized text, in brackets. Small accents are mostly not visible and are supplied. The date is not legible; the postmark is cut by the torn stamp. The plain-written address reads approximately *Szépreményű Tóth Jolánka úrleánynak, Budapest, Petőfi u. 16*, plus a faint last line starting *ház-* (perhaps *házfelügyelő…*); it was not needed for the decipherment and I do not claim it exactly. The address differs from the Jászárokszállás of the file name. The portal lists the language as Unknown; it is Hungarian. The printed picture-side captions are not part of the message.

## Why it is correct

- A key fixed on other cards gives connected Hungarian across all 33 rows, including the corners, the upside-down margin and the box, with one stray final sign (item 16) and three signs read against their shape (item 1). The reading order was forced by sense: *búcsúztam* runs round the corner and *ha valami közbe nem jön* runs into the box.
- Long words that could not be forced: *várakoztattam, vezénylés, átöltöztem, szolgálatba, szólítottak, csillagom, bocsánatomat, búcsúztam, viszontlátásra, számtalanszor*.
- Repeats decode identically (*hogy* ×4, *édesem* ×3, *mentem*).
- The closing *Csókolom számtalanszor* and signature Feri match HCP1216 verbatim in formula; the content (duty, roll call) is consistent with a man in service. Feri also signs other family cards; I do not claim more than the name.

## Response to review 1

Verdict REVISE. All six findings are addressed. The ledger and `work/normalized.txt` were corrected and `python3 -I ciphers/hcp-1293/work/decode.py` re-run: all four hashes OK, output agrees with the rows above. Literal letters changed in one place only (row 23 lost an n); B1 gained its dots; one word division in row 23 changed. The reading of the card is otherwise the same.

1. **Row 23 extra n: fixed.** Checked on crop `review/work/crops/n23.png`: one pair of strokes between e and the smudged i, no room for a second. Ledger and literal table now `leni`; normalized *le[n]ni*; the "No sign is restored" sentence is replaced; Uncertainty 13 updated.
2. **B1 dots: fixed.** The two ticks stand above the loop on `box.png`. Ledger `O:diaeresis`, Uncertainty 16 corrected.
3. **h/p/d statement: fixed.** On `p14.png`, `d10.png` and `d4.png` the tick positions are as the reviewer says. Ledger header and Uncertainty 1 rewritten; the three signs carry `:shape-` marks in the ledger. The readings stand, now on the correct stated basis. My earlier claim that p looks like h on this card was wrong.
4. **Row 23 division: accepted as preferred reading.** *Kérje ki bocsánatomat* removes the stray sign and explains *-omat* and the plural *hazamentek*. Hungarian, English and Slovak updated; Uncertainty 14 keeps the old division as the alternative and says this needs a native reader.
5. **Row 11 alternative: added** to Uncertainty 7. I cannot decide it either; the main reading stays because the signs are readable as k and s.
6. **vezén[y]lés: fixed.** The y is now bracketed and listed in Uncertainty 10.

Also from "What I could not verify": the sense basis of TT at the end of row 21 is stated in Uncertainty 4.

Note: `review/work/review_decode.py` treats any `:` in a ledger token as dots, so it now shows a false difference at the three `:shape-` tokens in rows 04 and 14. Those differences are the shape marks themselves. `work/decode.py` ignores the marks.
