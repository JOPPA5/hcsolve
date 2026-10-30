# HCP 1346 / pc_hcp_27 — German love postcard, St. Johann to Neunkirchen, April 1901 (round 1)

Portal status at capture (2026-10-30): **Not solved**; category Substitution, language Unknown; no transcription or solution attached. No published decipherment was found or used, and no separate literature search was made beyond the portal page and this repo. All of this work (transcription, key, reading) is by Claude Opus 5.5, 2026-10-30; there was no earlier work on this number.

## Card and context

Pencil digits across the picture side of an embossed rose card. The address side is plain script: tentatively *Fräulein M. Scheck in Neunkirchen, [...] park* (the street line is only partly legible and is not needed). Stamp: German Reich 5 Pf. Germania, postmark St. Johann, 16.4.01; arrival Neunkirchen 16.4.01. The portal date 1901-04-16 fits. Both places are in the Saar region, so German is expected.

## Cipher type and key

**Monoalphabetic substitution with 20 signs**: the ten digits, each either plain or with a small dot after it. The dot is part of the sign, not punctuation. Heavy, widely spaced dots and line ends separate words. No sister card in the repo uses this key.

| digit | plain | dotted |
|---|---|---|
| 0 | M | A |
| 1 | E | B/V |
| 2 | F | C |
| 3 | G | D |
| 4 | H | P |
| 5 | I | Z |
| 6 | K | R |
| 7 | L | S |
| 8 | N | T |
| 9 | O/Ö | U/Ü |

B and V share one sign. Umlauts are not marked, so O/Ö and U/Ü share signs. J, Q, W, X, Y do not occur on the card. The sequences E–I, K, L and N, O (plain) and A–D, R–U (dotted) follow the digit order, which supports the key independently of the text. Key file: `work/key.json`.

## Reproduce (one command, from the repo root)

```
python3 -I ciphers/hcp-1346/work/decode.py
```

This checks the four source hashes and decodes `work/transcription.txt` (290 signs, one token per sign, doubtful ones marked `~`, emended ones written `a=b`) with `work/key.json`. Its output is lower-case with the first letter of each shared sign (so "fuhle", "einberstanden"); the text below normalises that. It also prints the one emendation: the card has `dind`, the text reads `ging`.

## Plaintext

Reading order: rows top to bottom on the right-hand block, then the upside-down line at the top edge, then the two margin lines at the left.

```
Mir, liebe Mir!
Teil ich mit dir deinen Schmerz, fühle, könnte ich nur auf der Stelle alles ändern,
den Plan für Sonntag teile ich dir noch mit, und schreibe mir, ob du einverstanden bist.
Da ich gestern Abend spät nach Hause kam, konnte ich dir noch nicht eher schreiben.
Mit herzlichem Kuß verbleibt dein dich nie verlassender August.
[margin] Das Schreiben ging in Eile.
```

As written: *fuhle*, *konnte* (twice), *andern*, *fur*, *einverstanden* with V=B, *spat*, *Kus*; *herz-lichem* is split across a line end. Punctuation is editorial, because the cipher has none.

**English:** Mir, dear Mir! I share your pain with you, I feel it; if only I could change everything on the spot. I will still let you know the plan for Sunday, and write to me whether you agree. Since I got home late yesterday evening, I could not write to you any sooner. With a heartfelt kiss I remain your August, who will never leave you. [Margin] This was written in haste.

**Slovensky:** Mir, milá Mir! Delím sa s tebou o tvoju bolesť, cítim ju; keby som len mohol hneď na mieste všetko zmeniť. Plán na nedeľu ti ešte oznámim a napíš mi, či súhlasíš. Keďže som včera večer prišiel domov neskoro, nemohol som ti napísať skôr. So srdečným bozkom ostáva tvoj August, ktorý ťa nikdy neopustí. [Na okraji] Písané v zhone.

## Uncertainties

36 of 290 signs carry `~` in the transcription, and 2 of them are also emended (see point 1). The pencil is faint, the portal's grey watermark disc crosses the middle of the card, and the scan is only 1785 px wide. All words are read, but one of them only by emendation, and the points below are readings where the pixels alone do not settle the sign.

1. **`ging` (M17) is the weakest word, and it is an emendation.** On the card both 3s carry a dot: one under the foot of the first 3, one after the last 3, both low and separate from the mid-height word dividers that follow. Literally the word is `3. 5 8 3.`, which decodes to DIND, not a word. I read `ging` (`3 5 8 3`), which *Das Schreiben ging in Eile* needs, and assume a writer's slip or stray dots. The decoder keeps both forms (`3.=3~`). This word therefore does not support the plain/dotted key; G (plain 3) rests on *Sonntag*, *gestern* and *August*, where no dot follows the 3, and on the digit order E F G H I.
2. **`nie` (end of R15).** At first sight the pixels look like `8 3 7`. I read `8 5 1`. The writer's 5 regularly has a long top bar running right over the next sign (*dich* in R15, *schreibe* in R10, M17), and the middle sign has that S-shaped body. A short gap remains between its stem and the bar, so the assignment of the bar to the 5 is likely, not certain. The last sign has no hooked head and no crossbar of its own, unlike this writer's 7, so it fits 1. *dich nie verlassender* confirms it; `8 3 7` gives no word. The signs stay `~`.
3. **The flagged 1.** The writer's 1 sometimes has a flag that makes it resemble 4 or 7. It is read as 1 (E) in *deinen* (first E), *Stelle*, *den* and *gestern*.
4. **Similar digits.** The 2/9 confusion is general in this hand: 2. is read where the sign looks like 9 in the first *ich* of R05 and in *nach* (R13). 9. is read where it looks like 4 under the watermark band in *nur*. The first sign of *Teil* (R02) lies on the watermark edge and sits between 8 and a footed 2, with no dot visible with confidence; `8.` rests on the context and on the clear `8.` of *teile* in R09. In *schreiben* (R14) and *gestern* (R12) several signs lie on or beside watermark lines, including the 6. of *gestern*, and in my first pass I misread both words; the final grouping of signs there fits, but they are `~`. Their dots are not all visible.
5. **Z = dotted 5.** Both Z's (*Schmerz*, *herz-*) have the dot sitting well to the right of the 5, at mid-height, at a line end. It could be taken for a word divider. Plain 5 would give *Schmeri*, *heri*, so the dotted reading is required, but Z is based on these two cases only, and it breaks the digit-order pattern (Q would be expected there).
6. **Faint dots.** Some dots are not visible with confidence, marked `~`: for example in *Hause* (9., 7.), *Da* (0.), *abend* (1.), *Kuß* (7.), *verbleibt* (first 1.), *August* (7., 8.). Where a dot is hidden, the letter rests on the word.
7. **The name "Mir".** It is read clearly, twice (`0 5 6.`), and is taken as a pet name of the addressee, M. Scheck; that interpretation is a guess. Read as the pronoun, "mir liebe mir" would make no sense as a salutation.
8. **Interpretation.** *fühle* could belong to the preceding clause ("I share your pain, feel it") or the next. *konnte/könnte* is not distinguished in the cipher; R04 is taken as subjunctive from context, and R13 as past. The addressee's street line is not read.

## Why I believe it is correct

- A single 20-sign key decodes 288 of the 290 signs as they stand into continuous, grammatical German, with no unkeyed sign. The other two are the emended dots of `ging`.
- The key rests on long words that are hard to get by accident: *schreiben* (three times, including the margin), *einverstanden*, *verlassender*, *Sonntag*, *gestern*, *verbleibt*.
- The content is coherent and fits the period and the card: a love letter, a plan for Sunday, a request for a reply, a signature *August*, a closing formula *verbleibt dein ...*, and an apology in the margin. The context expected German from the postmarks.
- The dotted/plain split was not assumed; it follows from the statistics (in the final transcription 2. occurs 15 times, always before 4, i.e. CH, and plain 2 three times, always F; the first-pass count in NOTES.md was 2 followed by a dot 17 of 23 times) and from `69888.1`, which has triple 8 only if the last 8 is a different sign (NNT in *konnte*).
- The digit order of much of the alphabet is an independent check on the key.

## Response to review 1

Verdict REVISE. All six findings are accepted and addressed. The decoded text did not change; the changes are in the transcription apparatus, the decoder and this file. The command was re-run and still works: hashes OK, 290 signs, 36 marked ~, 2 emended, 0 unkeyed, same text.

1. **`ging` (major): fixed.** I confirm it on `review/work/y_ging2.png` and `m17b.png`: both 3s have a low dot, separate from the mid-height dividers after the word. On `y_sonntag.png`, `z_gestern.png` and `y_aug.png` no dot follows the 3. M17 is now `3.=3~ 5 8~ 3.=3~`, and `decode.py` prints "M17 emended: card has dind, read ging". It is uncertainty 1, and the claim "no unread word" is restated.
2. **`Teil` first sign (minor): fixed.** Now `8.~`, and described in uncertainty 4.
3. **`verbleibt` V (minor): fixed.** Now `1.~`, listed in uncertainty 6.
4. **Uneven `~` (minor): fixed.** `2.~` in *nach* (R13), `6.~` in *gestern* (R12); uncertainty 4 now calls the 2/9 confusion general. Count updated from 30 to 36.
5. **`nie` (minor): accepted with one reservation.** Uncertainty 2 now gives the pixel argument and `ging` is the weakest word. On `z_nie.png` I still see a short gap between the stem of the 5 and the bar, so I say "likely" and keep the `~`.
6. **Stale statistic (minor): fixed.** Recounted from the final transcription: 2. 15 times, plain 2 three times. Updated here and in NOTES.md, where the old figure is labelled first-pass.
