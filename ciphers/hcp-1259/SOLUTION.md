# HCP1259 — Feri to Jolánka Tóth: excuse for Ilona, a muddled card, "the evil tongues"

**Status: complete reading of the enciphered text, with one illegible plain line in the stamp box unread (see Uncertainties 8). Review 1 (REVISE) addressed, see the last section.** Claude Opus 5.5, 2026-11-01. No earlier work exists on this number. No published solution was found; the portal shows Not solved with no attached transcription or solution (catalogue row only, see `source/metadata.md`). The orchestrator's AI-register check of 2026-11-01 found no record.

Portal name: cpc_1912-04-04_HU__HU_Jasz Arokszalas_jolanka-14. The portal language says Unknown; the card is Hungarian. The clear postmark reads …ÁROKSZÁ… / 91 ÁPR 4, with no 2 printed in the year. A second cancel over the stamp box shows 912 ÁP, but only a final S of its place name is legible. The date 1912-04-04 rests on these two together and on the portal file name. The picture side (a couple with a mandolin, printed verse headed *Szerenád. Ábránd.*, series number 2317) has no cipher.

## Cipher type and key

Hungarian simple monoalphabetic substitution with invented graphic signs: the Jolánka family key, taken from finished cards HCP1216 (fullest legend), 1212, 1213, 1217, 1218, 1243, 1301. Every sign on this card was read afresh. One local variant: the family legend gives y as a low descender, whereas this card's y (*nyelvek*, *ylona*) is the crossed curve without a dot, so it may be an i with the dot left off. The h/p sign also appears once in the d shape (Uncertainties 12). The stamp-box lines and the address are ordinary cursive, not enciphered.

Type note 2026-11-03: the card is typed **MASC + Steganography** (register label), because the plain closing is written inside the stamp box, where the (now lifted) stamp hid it; see the section Stamp-box message (2026-11-03) at the end.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark, or plain S shape, on rows 1, 3, 13 with a dot beneath | k | F-like | r |
| six | b | wave | l | right bowl | s |
| short + long stroke | d | three short strokes | m | gamma | t |
| three bars | e | two short strokes | n | plain cross | u |
| open loop with descender | g | cursive loop | o | chevron | v |
| tall stroke + tick | h / p | dotted crossed curve | i | crossed curve, no dot | y |
| inverted T | j | joined cursive gy | gy | crossed diagonal with tail | z |

Features of this card: sz is written right bowl + z, sometimes joined (rows 16, 18). In *legyen* and *nagyon* the writer drops into ordinary cursive for the rest of the syllable (*gyen*, *gyon*). Letters c, f do not occur.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1259/work/decode.py
```

It checks the SHA-256 of all four image files, decodes the sign ledger `work/ledger.txt` (18 rows, one token per written sign) with the key above, and prints the literal letters and then `work/normalized.txt`. The ledger is a manual transcription from the pixels, not OCR; the key was known beforehand, so it was not blind. Enlarged crops for checking are in `work/crops/`.

## Literal decipherment

```
01 kedvesjolankam
02 remélemhogyelég
03 joltelnekórái
04 edesemlegyENel
05 nézesel[nezese]ilo
06 naylonaira{n}dena
07 gyONsokdolgavan
08 {h}igyeelédesem
09 {i/o}jzavarosirás
10 {m}intitvanamit
11 lat{h}atsoraimza
12 varosirásábol
13 {m}erszetakartamteh
14 {n}i.edesemir{j}onhon
15 {h}ogymiujsag{h}ogy
16 {r}{a}{g}odnakrajtamarosz
17 {n}y{e}lvek.istenvela
18 viszontlatasra
```

UPPERCASE = ordinary cursive; {x} = blotted, overlapped, pale or off-form sign whose value rests on word sense, {i/o} = hidden sign, either letter; an accent is shown where a mark is written on the card; [..] = struck through by the writer; h stands for the h/p sign.

## Hungarian (normalized)

Kedves Jolánkám! Remélem, hogy elég jól telnek órái. Édesem, legyen elnézéssel Ilona irán[t], de nagyon sok dolga van, higgye el, édesem. [I/O]ly zavaros írás, mint itt van, amit láthat soraim zavaros írásából, mer[t] szét akartam tépni. Édesem, írjon hon[n], hogy mi újság, hogy rágódnak rajtam a rossz nyelvek. Isten vel[e], a viszontlátásra.

Stamp box, plain cursive: [one illegible line, unread] Csókolo[m] számtalanszor. Sírig hű kedves[e], Feri.

Address, plain cursive: Szépremény[ű] Tóth Jolánka úrleánynak, Jászárokszállás.

## English

Dear Jolánka! I hope your hours are passing quite well. My darling, be indulgent towards Ilona, but she has a great deal to do, believe me, my darling. Such muddled writing as there is here, which you can see from the muddled writing of my lines, because I meant to tear it up. My darling, write from home what the news is, how the evil tongues are chewing on me. Farewell, until we meet again.

Stamp box: [one illegible line, unread] I kiss you countless times. Your sweetheart, faithful unto the grave, Feri.

Address: To the promising Miss Jolánka Tóth, Jászárokszállás.

## Slovak

Milá Jolánka! Dúfam, že Vaše hodiny plynú celkom dobre. Drahá, buďte zhovievavá voči Ilone, ale má veľmi veľa práce, verte mi, drahá. Také zmätené písmo, ako je tu, čo môžete vidieť zo zmäteného písma mojich riadkov, lebo som to chcel roztrhať. Drahá, napíšte z domu, čo je nové, ako ma ohovárajú zlé jazyky. S Bohom, dovidenia.

V poli pre známku: [jeden nečitateľný riadok, neprečítaný] Bozkávam Vás nespočetnekrát. Váš do hrobu verný milý, Feri.

Adresa: Nádejnej slečne Jolánke Tóthovej, Jászárokszállás.

## Uncertainties

Calls that rest on word sense, not on the sign alone:

1. **Row 9, first sign.** A pale blot with a right spur hides the sign before the j. Directly above it stands a separate mark. Elsewhere on this card marks between rows belong to the row below, which points to the dotted i, though this mark is about twice the size of the i dots and may be a blot. The spur fits the arm of i as well as o. So *ily* and *oly* ("such", spelled *ij* / *oj*; the same writer spells *ojan* on HCP1216) are both open, and both fit *mint itt van* ("as there is here"). The meaning is the same either way. *Ej* ("ah") gives a poorer sentence.
2. **Rows 5–6, *ilo|na ylona*.** The writer struck the repeated *nézése*, then wrote *ilo*, broke the row, and wrote *na* and *ylona*. The second *ylona* has no dot on its first sign, which is literally y. Read as a repeated *Ilona* with the dot omitted. *Ilona* or *Ilonka* occurs on HCP1263, 1265 and other family cards; I claim no identification beyond the name.
3. **Row 6, *irán[t]*.** The two pale strokes after *ira* run up into a stain. They are read as n. No t is visible; the stain could hide one but I do not claim that. *Irán[t]* ("towards") gives the construction with *elnézéssel*. Another possibility is a slip for *írna* ("[Ilona] would write"), which would change the clause to "Ilona would write, but she has a great deal to do". The n/d call on this pale pair rests on word sense.
4. **Row 13 end to row 14 start, *tépni*.** The tall-plus-tick sign is taken as p, not h (h/p near-homograph), and the blotted first sign of row 14 as n. Both rest on the word. Row 15 *hogy* (both) and row 14 *hon* take the same sign as h.
5. **Row 14, *ír{j}on*.** A heavy blot covers the sign after r. Its wide foot fits the inverted T; *írjon* ("write") fits the sentence. Blots also cover the first signs of rows 13, 15 and 16: m (*mer*), h (*hogy*), r a (*rágódnak*). Row 15's second *hogy* also has a blotted h. Further blotted signs are the first of row 10 (m of *mint*) and the first of row 17 (n of *nyelvek*). These calls rest on the word, with parts of the strokes visible; all are flagged in the ledger. The g of *rágódnak* (row 16) is an ink blob with a long tail and could be k by shape; *rákódnak* gives no sense here, so *rágódnak* stands, but it rests on sense more than the other words of the card.
6. **Row 14, *hon*.** Written *hon*, normalized *hon[n]* (older spelling for "at home"); translated "from home" by sense.
7. **Row 17.** The e of *nyelvek* shows one bar plus a wedge under the g tail of row 16; sense decides it. The last sign of row 17 is two clean bars, literally a. I read it as the article of the family's closing *Isten vele, a viszontlátásra* (HCP1216 row 22: *istenveleaviszontlatasra*; HCP1212), with the e of *vele* left out by the writer. So *vel[e], a*; no bar count is emended.
8. **Stamp box.** The topmost line is an illegible pink mass, partly outside the box, with one loop visible at its left, and is **not read**. It is about one word long. Whether it was deleted on purpose or smeared cannot be told. Below it *csokolo* (a final m is not visible at the box edge), *számta|lanszor*, *sirig hű* (only one dot is visible on the last letter, beside a smear), *kedves* (no final e is visible), *Feri*. The stamp-box text is read as plain script with help from the family's formula.
9. **Sense.** Row 9–13 is clumsy as a sentence, though it matches the card, which has a struck line and many blots. *Rágódnak rajtam* is taken as "gnaw at me", i.e. gossip; the exact shade is an interpretation.
10. Writer's spellings normalized: *higye* → higgye, *elnezesel* → elnézéssel, *mer* → mer[t], *mintit* → mint itt, *rosz* → rossz. The dot after *tépni* is read as a full stop. The dot after k in *nyelvek* may be a full stop or part of the k, as the dot beneath k on rows 1, 3 and 13 seems to be; the text does not change. Marks between rows are mostly real accents or i dots of the row below. Written accents show on é of *remélem*, *elég* and row 8 *édesem*, ó and á of *órái*, the first e of *nézésel*, á of row 9 *írás*, and two á of *írásából*; a further stroke stands over the first e of *elég*, which standard spelling does not accent. All other accents are supplied.

11. **Address.** The first word ends at y, where paper damage begins; no ű is visible, so *Szépremény[ű]* (as on HCP1250).
12. **h signs of unusual form.** In *láthat* (row 11) the sign has the d shape, a short stroke at upper left against a long stroke, as in rows 1, 4 and 8, not the h form of rows 2 and 13. *Ládat* gives nothing here, so h rests on word sense. The first sign of row 8 (*higye*) is a long stroke with a low short stroke, also not a clean h, and likewise rests on the word.
13. **Portal capture.** The detail page timed out and was not re-read in this round, so "nothing attached" rests on the catalogue row (`source/metadata.md`).

## Why it is correct

- The family key turns all 18 rows into Hungarian with no sign left over. The local variants are listed above (y without a dot; h in the d shape in *láthat*).
- Unforced checks: *kedves*, *édesem* ×3 (rows 4, 8, 14), *zavaros írás* ×2 (rows 9, 12), and a close *Isten vel[e], a viszontlátásra* as on the family's cards.
- The content fits: Feri signs, the closing formulas match sister cards, Ilona(ka) recurs in the correspondence, and the remark about muddled writing matches this card's strike-through and blots.

## Response to review 1

Verdict REVISE. I rechecked each finding on the reviewer's crops and on the pixels. All are accepted; none changes the sense of the card. After the changes `python3 -I ciphers/hcp-1259/work/decode.py` runs cleanly, all four hashes are OK, and the literal text above is its output. The letters are unchanged, except for row 9's first letter, now i/o.

1. **Row 17 *vel[e], a*: fixed.** The last sign is two clear bars. The normalized text now reads *Isten vel[e], a viszontlátásra*, in `work/normalized.txt` and above; translations are unchanged. The bar-count claim is removed.
2. **Row 9 *ily/oly*: fixed.** The ledger token is now `?io`, printing {i/o}, and the normalized text is [I/O]ly. Uncertainty 1 mentions the mark. One addition to the finding: the mark is about twice the size of an i dot, so I keep the letter open rather than choosing i.
3. **Row 11 *lát-h-at*: fixed.** Confirmed in `review/work/r11.png`: d shape. New ledger token `?thd`; disclosed in Uncertainty 12 with row 8's first sign, also flagged. The "only one sign" claim is removed.
4. **`?` flags: fixed.** Now flagged: rows 6 (pale n), 8, 10, 11, 13, 14 (first sign), 15 (both h), 16 (r, a, g), 17 (n). The ledger header definition is widened to cover these. Row 16 g and rows 10 and 17 are added to Uncertainty 5.
5. **Accents and dots: fixed.** Confirmed on the band crops. Accents are added to the ledger for *elég*, *órái*, *nézésel* and *írás*. Beyond the finding, I also found the é of row 8 *édesem* and a stroke over the first e of *elég*. Uncertainty 10 and the key table are corrected, and the full stop after *nyelvek* is no longer asserted.
6. **Address: fixed.** *Szépremény[ű]*.
7. **Postmark: fixed** in the header paragraph.
8. **Stamp box: fixed.** "Illegible" is used throughout, and Uncertainty 8 no longer treats the line as a deletion. It is one lost word in the plain closing, so the card stays complete.
9. **"Used unchanged": fixed.** The y variant and the picture side are stated in the header and the key section.

Could-not-verify items: the row 6 pair and *Ilona irán[t]* versus *írna* stay open (Uncertainties 2 and 3). The portal detail capture was not retried; this run is limited to finishing this card (Uncertainty 13).

## Stamp-box message (2026-11-03)

Stamp-box audit, done on the human's instruction of 2026-11-03 (Claude Opus 5.5). Crops of the original `work/hires/..._adr.jpg` (x 2560 to 3160, y 40 to 760 at 2x; the top line x 2950 to 3180, y 150 to 420 at 5x, with a blue-channel map) are in `work/stamp-2026-11-03/`.

- **State:** stamp lifted, writing under it. The printed dotted frame of the stamp box and its small blue P.R.A. wreath are bare paper. The second cancel (912 ÁP) stops at the left edge of the frame, so the stamp was on the card when it was cancelled; the red lines lie on bare paper inside the frame and were hidden under it.
- **Script:** plain Hungarian cursive only; no cipher signs in the box.
- **Literal reading** (lines from top right, diagonal): [illegible line] / csokolo / számta (paler ink) / lanszor / sirig hű / kedves / Feri.
- **Normalized Hungarian:** [one illegible line] Csókolo[m] számtalanszor. Sírig hű kedves[e], Feri.
- **English:** [one illegible line] I kiss you countless times. Your sweetheart, faithful unto the grave, Feri.
- **Slovak:** [jeden nečitateľný riadok] Bozkávam Vás nespočetnekrát. Váš do hrobu verný milý, Feri.
- **Unread:** the topmost line, about one word, a smeared pink mass partly outside the frame; the 5x crop and the blue channel show only a loop at its left and give no letters, so it stays unread (Uncertainties 8). The final m of csókolo[m] and e of kedves[e] are not visible and are supplied only in the normalized text, as before. This reading is the same as the one already given above; nothing new was read and nothing was restored.
- The reproduction command decodes only the 18 cipher rows (`work/ledger.txt`); the stamp text is plain script read by eye, so the script was not changed.
