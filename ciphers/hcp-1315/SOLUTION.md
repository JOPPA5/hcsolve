# HCP1315 — Feri to Jolánka Tóth: a rainy Sunday apart

**Status: complete reading of the card; review 1 (REVISE) addressed, see the last section.** Solved 2026-10-30 by Claude Opus 5.5. No earlier work exists on this number. The portal shows status *Not solved* and attaches no transcription or solution; no published solution was met. The key was taken from the finished sister cards (HCP1216, 1212, 1213, 1217, 1218, 1243, 1301), not invented here.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the "Jolánka" postcard family). Sign classes:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section sign (S/5-shaped) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| short stroke, then long stroke | d | three short strokes | m | gamma/corner | t |
| three bars | e | two short strokes | n | plain cross x | u |
| upright cross + | f | cursive loop | o | chevron | v |
| left bowl with descender | g | long stroke, then short stroke | h / p | low descender loop | y |
| dotted crossed curve | i | inverted T | j | crossed diagonal with long arm | z |
| opposed bowls joined | cs | | | | |

Marks: dots over x give ü; a double stroke over the loop gives ő. On this card *gy* is written as two signs (g + y). The digits in "½ 9" are in clear.

Card-specific forms: *tt* in *attól* (row 11) is one joined sign, gamma linked to gamma (token `TT` in the ledger, `work/crops/r11_full.png`). The n at the end of *egyetlen* (row 2, `review/work/crops/r2n.png`) has its two strokes joined by a top bar; it is otherwise the n sign, and it is read n by the word.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1315/work/decode_opus.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger-opus.txt` (392 signs, one token per written sign) and prints the literal rows and then `work/normalized-opus.txt`. The ledger is a manual reading of enlarged crops, not OCR. It was read with the key and word sense in view, so it is not blind.

## Literal decipherment (as printed by the command)

```
01 szeretetedesjolank?a?m      12 agong?oktolhogy
02 edesegyetl?enremenyem       13 nemtőlthetem
03 kivanomhogyalegjob          14 magavaleztvasar
04 kedvebentalaljaso           15 napotigazhogy
05 raimhogymulatot             16 nemalegjobbido
06 vasarnapremelem             17 voltdeaszobab{a|e}
07 j?olamieng?emilet           18 nemesikazesső
08 ½9korjotemhaza              19 mostma?rtobbet
09 eslefeküdtemes              20 nemirokezelbezaromsoraimma
10 aludtamazalvas              21 radoksihüimadojaferimajdszerdan
11 megmentetattol

Stamp corner, s1-s8: istenve | l?eedesem | [s]zamta | lan[s]zor? | csok?o?l? | [s]zer{a|e} | tokedve | s{a|e}nf?eri
```

## Hungarian (normalized)

Szeretet[t] édes Jolánkám! Édes egyetlen reményem! Kívánom, hogy a legjob[b] kedvében találja soraim[at]. Hogy mulat[t]ott vasárnap? Remélem, jól. Ami engem il[l]et, ½9-kor jöt[t]em haza, és lefeküdtem, és aludtam. Az alvás megmentet[t] attól a gon[d]októl, hogy nem tölthetem magával ezt [a] vasárnapot. Igaz, hogy nem a legjob[b] idő volt, de a szobába nem esik az es⟨s⟩ő. Most már többet nem írok, ez[z]el bezárom soraim[at], maradok sí[rig] hű imádója, Feri. Majd szerdán.

Stamp corner: Isten vele, édesem! [S]zámtalan[s]zor csókol [s]zerető kedvese⟨n⟩ Feri.

[x] = supplied or restored by the editor; ⟨x⟩ = written on the card, removed by the editor.

## English

My beloved sweet Jolánka! My sweet, only hope! I wish that my lines may find you in the best of spirits. How did you enjoy yourself on Sunday? Well, I hope. As for me, I came home at half past eight [8:30], went to bed and slept. Sleep saved me from the worries that I cannot spend this Sunday with you. True, it was not the best weather, but in the room it does not rain. I will not write more now; with this I close my lines and remain, faithful unto the grave, your adorer, Feri. Until Wednesday, then.

Stamp corner: God be with you, my darling! Your loving sweetheart kisses you countless times, Feri.

## Slovak

Moja milovaná sladká Jolánka! Moja sladká jediná nádej! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako ste sa zabavili v nedeľu? Dúfam, že dobre. Čo sa mňa týka, prišiel som domov o pol deviatej, ľahol som si a spal som. Spánok ma uchránil pred starosťami, že túto nedeľu nemôžem stráviť s Vami. Pravda, nebolo najlepšie počasie, ale do izby nezaprší. Teraz už viac nepíšem, týmto končím svoje riadky a zostávam Váš do hrobu verný ctiteľ, Feri. Teda v stredu.

V rohu pod známkou: S Bohom, drahá moja! Nespočetnekrát Vás bozkáva Váš milujúci milý, Feri.

## Uncertainties (all disclosed)

Calls resting on word sense or on an imperfect sign:

1. **h against p, and d.** d and h/p are told apart by stroke order: d is a short stroke then a long one, h/p a long stroke then a short one. This held at every place checked (d in rows 1, 2, 4, 9, 10, 16, 17, 21; h/p in rows 3, 5, 6, 8, 12, 13, 15, 21), so d does not rest on word sense. Only h against p does: *hogy*, *haza*, *tölthetem*, *hű* (h), *vasárnap* (p). n against d rests on stroke length, which is clear here (*egyetlen*, *reményem*, *bezárom*).
2. **Row 7 first sign `j?`.** Heavily overinked and apparently corrected. A base stroke and stem are visible with a short arm at top right, so the shape does not fully match a clean inverted T. *jól* is chosen from context ("Remélem, jól").
3. **Row 7 `g?` of *engem*.** The bowl is retraced and closed at the top; g from context.
4. **Row 12 `g?` (*gon?októl*).** The sign is written as the g sign, not d. Taken at face value the card has *gongoktól*, which is no word. It is normalized to *gondoktól* as a writer's slip (g for d). "attól a gondoktól" is also slightly ungrammatical (singular *attól*, plural noun), and is translated by sense.
5. **Row 19 `a?` of *már*.** Blotted: two bars joined by an overinked stroke, with a hook at right. The word *már* gives the a.
6. **Row 17 last sign `{a|e}`.** Two bars are visible and the printed dashed line runs through the sign, so a third bar cannot be excluded. Normalized *szobába*.
7. **Row 21 `si hü`.** The signs read s, i (dot visible), h, ü (dots visible). *sírig* is not written in full; *sí[rig] hű* is an expansion from the family's formula *sírig hű* (HCP1216). The reading "faithful unto the grave" depends on that expansion.
8. **Row 20 `soraimma|radok`.** The word *soraim* is followed directly by *ma-* of *maradok* (row 21); the accusative *-at* is not written, and is supplied in brackets. The second m has a bar joining its strokes.
9. **Row 21, *Majd szerdán*.** The signs are clear and the card ends after n at the corner. The phrase is elliptic and could mean "[I will write/come] on Wednesday"; the card does not say which.
10. **Stamp corner (under the stamp, partly torn off, overprinted by a triangle mark).** This part is weaker than the main text:
    - s3: the first s lies on the tear and only traces remain; **restored** as the one letter that makes *számta-*.
    - s4: the s lies under the triangle's edge and is merged with printed lines; **restored** from *-lanszor*.
    - s6: the first s is only a partial arc on the tear (**restored**); the last sign lies on the triangle, and only two bars can be separated from the print (`{a|e}`). A short arc just below them, at the height of a third bar (`review/work/crops/c67.png`), may make it e, which is what *szerető* needs.
    - s2 first sign (*l* of *vele*): a green blot, read from sense (`l?`).
    - s4 last sign (*r* of *-szor*): a spread blot, F-like only in outline (`r?`).
    - s5 *k, o, l*: laid over the dense print of the triangle (`k? o? l?`).
    - s8: the bars after s are incomplete (`{a|e}`). Then n is clear (two real strokes), and the blot is read as f: a heavily overinked cross, which is read from *Feri* (`f?`). Literally the row gives *…kedvese n Feri*. Three explanations are open: a slip; the adverb *kedvesen*; or the blot has a separate left diagonal at about the right spacing, so that n + f might be m + f, giving *kedvesem Feri*, which fits less well after *csókol*. Normalization marks the deleted n as ⟨n⟩.
    - s8 last sign: the stem and crossing stroke are clear, but the loop sits on the tear, so i is not fully seen.
    - s5–s7 *szerető* is written without visible ő marks and with s6 ending in the print; *szerető kedvese* is the sense-based reading.
11. Other writer spellings normalized: *szeretet* → szeretett, *legjob* → legjobb (row 3, while row 16 has bb), *mulatot* → mulattott, *ilet* → illet, *jotem* → jöttem, *megmentet* → megmentett, *esső* → eső, *ezel* → ezzel. *soraim* (rows 4/5 and 20) stands for *soraimat*, and the family writes it so; the ending is supplied in brackets in both places. Vowel marks: *tőlthetem* (double mark over o on the card) → *tölthetem*; *ido* → *idő*; ö dots are not written in *jöttem* and *többet*. Other accents (á, é, í, ó) are mostly not visible and are supplied.
12. Row 14: *ezt vasárnapot* is what the card has; no article stands between t and v. The *a* in *ezt [a] vasárnapot* is the editor's, required by the grammar.
13. Two more weak signs on the main rows: row 1 *k a* of *Jolánkám* lie in a wet smear, with a brown S-arc and two bars still visible (`k? a?`); row 2 *l* of *egyetlen* lies in a stain, only a blurred wave (`l?`). The word decides both.
14. Row 8 is read as the clock time ½9 (Hungarian "half nine" = 8:30). The first sign is a fraction stroke with a small 2 under it, followed by a clear 9 and *-kor*.
15. Not cipher, and not part of the ledger: the plain address "Szepremenjü Tóth Jolánka …, Budapest, István út 5" (one word of the address is hard to read; it is not needed here), the postmark BUDAPEST with year ending 914, and the printed picture-side verse "A szerelem hőmérője" (The thermometer of love).

## Why it is correct

- The key comes unchanged from reviewed sister cards, and no value was fitted to this card. It turns all 21 main rows into continuous Hungarian with no unassigned sign; the only weak signs are listed above.
- Repeated words decode identically in different places: *hogy* ×4 (rows 3, 5, 12, 15), *vasárnap* ×2 (rows 6, 14–15), *nem* ×4, *legjob* ×2, *soraim* ×2, *édes* ×3 (rows 1, 2, s2), *Feri* ×2.
- The style and formulas match the family. The closest parallel is HCP1301, *Remélem, jól. Ami engem illet*. Others: *kedvében … találja soraim* and *Hogy mulatott vasárnap?* (HCP1217; the first also HCP1218), *Ezzel bezárom soraim* (HCP1218, 1306, 1308, 1310), *imádója* (HCP1301), *Isten vele* (HCP1212, 1216), *számtalanszor csókol … Feri* in the stamp corner (HCP1212), *szerető kedvese Feri* (HCP1306), *sírig hű kedvese* (HCP1213, 1216). The sense also runs from sentence to sentence (a lonely wet Sunday, sleep as a refuge from missing her).
- The unexpected "½ 9" and the small joke ("in the room it does not rain") are not what forced word-fitting would produce.

## Response to review 1

Verdict REVISE. All seven findings accepted after rechecking the scans. The command was re-run after the fixes: four hash checks OK, 392 signs, output matches the sections above.

1. **Phantom *a*, row 14: fixed.** Confirmed on `review/work/crops/r14b.png`: wave, three bars, crossed z, gamma t, then at once the chevron v. The token is deleted from `work/ledger-opus.txt`; the row is now `magavaleztvasar` and the ledger has 392 signs. The article was supplied from grammar and wrongly entered as read. Normalized text now has *ezt [a] vasárnapot*; see uncertainty 12. English and Slovak do not change.
2. **d against h/p: fixed.** Stroke order rechecked (row 10 *aludtam*, row 8 *haza*, row 13 *tölthetem*, row 21 *hű*). Key table, ledger header and uncertainty 1 restated: only h against p rests on sense.
3. **Unflagged weak signs: fixed.** Row 1 *k a*, row 2 *l*, s2 *l*, s4 *r*, s5 *k o l* now carry `?` in the ledger and are listed under uncertainties 10 and 13.
4. **Stamp corner s8 and s6: fixed.** The m + f alternative (*kedvesem*) is listed; the deletion is shown as ⟨n⟩. The arc under s6's last sign is noted; the sign stays `{a|e}` because the print does not let me decide. The three restored s are now bracketed in the normalized stamp text as well.
5. **Evidence counts and citations: fixed.** *hogy* ×4 and *édes* ×3 recounted from the ledger. *kedvében találja soraim* is now cited to HCP1217 and 1218, not HCP1212. *imádja Feri* is removed; the phrase is not in HCP1212 or 1216, and *imádója* is cited to HCP1301, which is also added as the closest parallel.
6. **Normalization: fixed.** *mulat[t]ott*, *soraim[at]* in both places, *tőlthetem* → *tölthetem* and *ido* → *idő* are shown or listed (uncertainty 11). Beyond the finding, *gon[d]októl* and *es⟨s⟩ő* are also marked, and `work/normalized-opus.txt` states the bracket convention.
7. **Key table: fixed.** The joined `TT` sign and the barred n of row 2 are described in the key section. Reviewer's citation `r11tt.png` shows row 12, not row 11; I checked the sign on my own crop `work/crops/r11_full.png`, and the joined gamma-gamma is real.

The reading is not substantially changed: one sign removed, no word and no translation altered, so the card goes to FINAL and not to a second review round.
