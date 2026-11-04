# HCP1236 — Feri to Jolánka Tóth: the club theatre evening and "do you ever think of me"

**Status: complete reading, review 1 (REVISE) addressed.** Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The portal shows status Not solved and attaches no transcription or solution; I found no published solution. The sign transcription is mine (work/ledger.txt): a manual reading of enlarged crops, not OCR. It was not blind in the later rows, because word sense was used to test readings; those calls are listed below.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family.

**Type (2026-11-03): MASC + Steganography.** The cipher body is MASC; a plain Hungarian note was written in the stamp box and hidden under the stamp (see "Stamp-box message (2026-11-03)"). The key is transferred unchanged from hcp-1216 (also 1212, 1213, 1217, 1218, 1243, 1301). Every letter sign below occurs on this card except where noted; no new sign was needed.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (dot below) | k | F-like | r |
| six | b | wave | l | bowl, either facing | s |
| short + long stroke, joined look | d | three short strokes | m | gamma/corner | t |
| three bars | e | two short strokes | n | plain cross x | u |
| cross with high bar and long descender | f | cursive loop | o | chevron | v |
| open loop with descender | g | long + short stroke | h / p | crossed diagonal | z |
| dotted crossed curve | i | joined loop + descender | gy | opposed bowls | cs |
| low bar with short stub below | j | | | | |

f and j are near-neighbours and differ by where the bar sits: f (rows 4, 6) has it high with a long descender, j (rows 1, 2, 3, 13) has it near the foot with a short stub. The dot under the k sign is omitted twice on this card (uncertainty 14).

Accents are written as separate ticks above the sign (two bars + tick = á, two ticks over the loop = ö/ő). c and y do not occur alone here.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1236/work/decode.py
```

It checks the SHA-256 of both source scans and both hi-res originals, decodes work/ledger.txt with the key, prints the literal rows, then prints work/normalized.txt.

## Literal decipherment (as printed by the command)

```
01 szeretettédesjolan          10 edesemhogyérzi
02 kámkivánomhogylegjobb       11 magátgoadoleneha
03 kedvebentaláljasora         12 atavolbanönert
04 imhogymulatottafar          13 ehedöszivtulajdo
05 sangbaamiengemill           14 nossaraéncsakakkor
06 lethetfötátdolgoz           15 vagyokigazánbol
07 tamkeddenhedigelmen         16 dogdaaszéhszemébe
08 temazegyletbeahol           17 nézhetekistenveleaviszoat
09 szineöadasvolt              18 latasra
```

h stands for the h/p sign throughout.

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy legjobb kedvében találja soraim. Hogy mulatott a farsangba[n], a mi engem illet, hétfőt átdolgoztam, kedden pedig elmentem az egyletbe, ahol színe[l]őadás volt. Édesem, hogy érzi magát? Gondol-e néha a távolban önért epedő szív tulajdonosára? Én csak akkor vagyok igazán boldog, ha a szép szemébe nézhetek. Isten vele, a viszontlátásra.

Unenciphered margin note, on the bare patch where the stamp was: Csókolja távolba számtalanszor Feri.

Unenciphered address: Szeretett Tóth Jolánka kisasszonynak, Jász Árokszállás.

Printed on the picture side (not part of the message): "Sorrentói ábránd", a six-line sentimental verse beginning "Ez a levél az utolsó, amit hozzád irok". No handwriting on that side.

## English

My beloved sweet Jolánka! I wish that my lines may find you in the best of spirits. How did you enjoy yourself at the carnival? As for me, I worked all through Monday, and on Tuesday I went to the club, where there was a theatrical performance. My darling, how are you feeling? Do you sometimes think of the owner of the heart that pines for you in the distance? I am truly happy only when I can look into your beautiful eyes. Farewell, until we meet again.

Margin: Feri kisses you from afar countless times.
Address: To the beloved Miss Jolánka Tóth, Jászárokszállás.

## Slovak

Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako ste sa zabavili na fašiangoch? Čo sa mňa týka, celý pondelok som pracoval a v utorok som išiel do spolku, kde bolo divadelné predstavenie. Drahá moja, ako sa cítite? Myslíte niekedy na majiteľa srdca, ktoré za Vami v diaľke túži? Ja som naozaj šťastný len vtedy, keď sa môžem pozerať do Vašich krásnych očí. S Bohom, dovidenia.

Na okraji: Bozkáva Vás z diaľky nespočetnekrát Feri.
Adresa: Milovanej slečne Jolánke Tóthovej, Jászárokszállás.

## Uncertainties (none changes the sense)

Each of these is a call or a normalization; the ledger keeps what is written.

1. **Written a for n, twice.** Row 11 *goadol* and row 17 *viszoat* have clear horizontal two bars (a) where *gondol* and *viszont* need n. I treat both as slips of the pen, since n and a differ only in the direction of the two strokes. This rests on word sense.
2. **Row 16, *ha* written with d.** The sign before *a* has short stroke left, long stroke right, the d shape, as in *dog* just before it, not the h shape. Literal *da a szép*; normalized *ha a szép*. Word sense only.
3. **Row 13, *szív tulajdonosára*.** After *szí* stands one merged sign: a chevron whose right leg also serves as the stem of a t-like top bar and hook. I read it as v and t sharing a stroke. If it is t alone, the writer omitted the v of *szív*; the reading is the same.
4. **Row 17, i of *Isten*.** A heavily inked sign with no visible dot, between the i and o shapes. Read as i because only *Isten vele* fits; the same formula closes hcp-1216.
5. **Row 9, *színe[l]őadás*.** Literal *szineöadas*; the e is on the card, only the l is missing (writer's omission, supplied in brackets). The word is an interpretation of that spelling.
6. **Row 8.** The a of *az* is re-inked thickly over something unreadable; the bars are still visible. Row 4 *farsangba[n]*: no final n on the card (colloquial form). Row 10 *hogy*: the gy is overwritten but legible. Row 11: the t of *magát* has a pale overwrite and a blot beside it. Row 14: the o of *akkor* is overwritten. None of these has a competing reading.
7. **Rows 5–6, *ill-let*.** The word is written *ill* at the row end and *let* on the next row, so one l is doubled across the break. The second wave at row 5 sits on the card's vertical divider and is short. Normalized *illet*.
8. **Row 14, *tulajdonossára*.** Two s signs are written (normalized one s).
9. **Row 6, *hétfőt átdolgoztam*.** Written as one run, *hetfotatdolgoztam*; the word division is mine: preverb verb, "I worked through Monday".
10. **h/p, by word sense:** p in *pedig* (7), *epedő* (13), *szép* (16); h in *hogy*, *hétfőt*, *ahol*, *néha*, *nézhetek*. **d/n:** these do not collide on this card; every d has one long stroke and one short, every n has two equal short strokes.
11. **Accents.** Marks in the ledger are only those I saw. Others are supplied in normalization, and the stray mark on the o of *boldog* (row 15) is ignored. Small ticks between rows may belong to either row.
12. **Bottom edge.** Row 18 *látásra* is squeezed against the card edge and its last a is slightly clipped, still readable. Row 17 overlaps the printer's logo with the ink visible over it; no sign is lost.
13. **Address line 4** looks like *Jósz*; read as *Jász*, the town name on the portal filename and sister cards. Of the two postmarks one is partly under the lost stamp. The date 1912 and day 22 come from the portal file name `cpc_1912--22`; the left postmark, rotated and contrast-stretched, agrees with a year ending in 912 and a day beginning with 2, but the month is not legible. As an inference only: Shrove Tuesday 1912 was 20 February, so a card of Thursday 22 February would fit the carnival question and "on Tuesday". The month is not established. The pencil "18" at top right is a collector's or later mark.

14. **k without its dot, twice.** The first k of *csak* (row 14) and the k of *nézhetek* (row 17) have no dot below. Both are forced by the word.
15. **Row 2, *legjobb*.** The j has a pale upper stem where the pen ran dry, but the low bar and short stub are the j shape (review finding 1).
16. **Punctuation.** The ledger records letter signs only. Marks left out: hyphens after *Jolán-* (row 1) and *sora-* (row 3), full stops after *soraim* (row 4, in the stain) and *volt* (row 9), and a comma stroke after *farsangba* (row 5), which is a lone stroke and not a letter.

The sender "Feri" is the signature name; the same name signs hcp-1216, and the closing formula matches, but I claim no more than that.

## Why I believe it is correct

- The family key, transferred unchanged, turns all 18 rows into continuous Hungarian with no unexplained sign. Items 1–5, 10 and 14 rest on word sense, and each concerns one sign or one letter.
- Repeated words decode identically: *hogy* ×3, *édes-* ×2, *engem/elmentem* morphology, *t a m* endings.
- The reading of *epedő szív tulajdonosára* came from the signs, and is a natural phrase of the love-letter style; the card's own printed verse and the plain note *csókolja távolba* ("from afar") match the distance theme, and *Isten vele, a viszontlátásra* is the closing of hcp-1216.
- Address and recipient match the portal metadata and the file name.

## Response to review 1

Verdict REVISE. All six findings accepted; none changes the sense of the message.

1. **major, row 2 `legjobb`: fixed.** I compared the signs in review/work/fj_compare.png: the row 2 sign has the low bar and short stub of j (rows 1, 3, 13), not the high bar and long descender of f (rows 4, 6). Ledger token `+` became `J`; work/normalized.txt, the literal row, the Hungarian text and item 11 are corrected, and the f/j difference is now in the key section. The English and Slovak already meant "best" and stay.
2. **minor, row 6: fixed.** Now `hétfőt átdolgoztam`; item 9 rewritten. Same signs.
3. **minor, date: fixed.** Item 13 now gives 1912, day 22, from the file name plus postmark. My look at review/work/pm_read.png supports only that much; the month is unreadable, and the carnival date is labelled as inference.
4. **minor, dotless k: fixed.** Confirmed on review/work/z14.png and z17a.png; added as item 14, and the "why correct" statement no longer says only items 1–4 needed word sense.
5. **minor, punctuation: fixed.** The ledger header now says punctuation is left out and lists the marks; also item 16. The row 5 stroke (review/work/z5.png) is explained as a comma.
6. **minor, bracket: fixed.** Now `színe[l]őadás` in work/normalized.txt and the text, and item 5.

After the fixes `python3 -I ciphers/hcp-1236/work/decode.py` passes all four hash checks and prints the corrected rows. The change is one letter value plus editorial notes, so the reading is not substantially changed and no second review round is needed.

## Stamp-box message (2026-11-03)

Audit of the stamp box on the hi-res address side (work/hires/..._adr.jpg), crops in work/stamp-2026-11-03/ (stampbox_1x.png, rows12_3x.png, rows35_3x.png).

- **State: stamp lifted, writing under it.** The stamp is gone; its perforated outline remains as a clean pale rectangle at top right. The right postmark's ring stops at the edge of that rectangle, so the stamp was in place when the card was cancelled and the note inside the rectangle was covered by it.
- **Script: plain Hungarian only**, pink ink, five lines. No cipher signs in the box.
- **Literal reading (every letter read from the pixels, no restoration):** `csokolja / tavolba / szamta- / lanszor / Feri` (no accents written; *számta-lanszor* divided across lines 3–4).
- **Normalized Hungarian:** Csókolja távolba számtalanszor Feri. (*távolba* = *távolból/a távolban*, colloquial.)
- **English:** Feri kisses you from afar countless times.
- **Slovak:** Bozkáva Vás z diaľky nespočetnekrát Feri.
- **Unread:** nothing; every letter is clear. This note was already in this file and in the report as the "margin note"; it is now identified as the hidden stamp-box message. The stamp text is read by eye and is not in work/ledger.txt or work/decode.py, which cover the cipher rows only (left unchanged).
