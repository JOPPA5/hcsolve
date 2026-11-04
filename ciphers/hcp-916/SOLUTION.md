# hcp-916 — Solution (round 1)

Solver: Claude Opus 5.5, 2026-11-03. There is no earlier work on this number: the directory and scans were captured today by the orchestrator. No published solution exists as far as I can tell. The portal status is "Not solved" and no transcription or solution is attached. The key family comes from my own finished sister card hcp-1133 (same recipient, same address, same handwriting habits), not from any outside source.

## The card

- Address side, plain Hungarian: "Levelező lap. Ő nagysága Márthé Ilona úrhölgynek, Temesvár-Józsefváros, Eötvös utcza 7 sz." ("To her Ladyship Miss Ilona Márthé, Temesvár-Józsefváros, Eötvös Street No. 7"). The portal spells the recipient "Ilona Marfke", but the scan reads Márthé. A green 5-filler Turul stamp is still on the card, and its postmark reads TEMESVÁR ... 90(4) APR 1. Nothing shows through or around the stamp, so whether anything is hidden under it cannot be checked from the scans. That is a known habit on some Hungarian cards of this period.
- Picture side (rotate it 90° counter-clockwise): a printed Easter scene with three children and a nest, publisher mark "NPG 277-6". In the top corner is the dateline "Tv. 904 III/1." (a small superscript stroke over "Tv"). It is most likely an abbreviation of Temesvár, so 1 March 1904. Below that is a Morse block of 3 lines written diagonally across the oval, followed by a monogram signature. Under the picture is a Morse block of 4 horizontal lines. The picture side carries no plain text apart from the dateline and the monogram.
- The same recipient and address appear on hcp-1133 (Temesvár, December 1902), which is signed "Richter Antal" and also mixes Morse into the text. The writer's nonstandard Morse Á `.-.--` appears on both cards.

## Cipher type and key

**Morse code** written as dots and dashes. A slanted stroke "/" follows every letter, and words are not separated. The key is International Morse plus:

- É = `..-..` (the standard Hungarian sign)
- Á = `.-.--`. This is the writer's own sign, identical to hcp-1133 (the standard one is `.--.-`). It occurs three times here: ILUSKÁM, DRÁGA, LÁTHATOM.
- `.-.-` is used for C in CSÓK (the standard C is `-.-.`). It occurs once, so this rests on word sense.
- Long vowels Í, Ó, Ö are otherwise written as plain I, O. The one exception is the mark at the start of bottom line 4, discussed under Uncertainties.

Register type label: **MASC/Morse**.

## Command

From the repo root:

```
python3 -I ciphers/hcp-916/work/decode.py
```

It checks the SHA-256 of all four scans and decodes `work/morse_transcription.txt`, which holds my sign-by-sign transcription of every Morse line. Output:

```
B joined: ILUSKÁMDRÁGAMIKORLÁTHATOM?KÉREMARANYOMÍRJON
T joined: MILLIOFORROCSOKÉDESEMNEK
```

## Plaintext (Hungarian, Morse text in capitals, word division mine)

Reading order: the bottom block opens the message, and the diagonal block ends it with the monogram.

> Tv. [Temesvár] 904 III/1.
> ILUSKÁM DRÁGA, MIKOR LÁTHATOM? KÉREM ARANYOM, ÍRJON.
> MILLIÓ FORRÓ CSÓK ÉDESEMNEK.
> [monogram]

In modern spelling: "Iluskám drága, mikor láthatom? Kérem, aranyom, írjon. Millió forró csók édesemnek."

**English:** [Temesvár] 1 March 1904. My dear little Ilus, when can I see you? Please, my golden one, write. A million hot kisses to my sweetheart. [monogram]

**Slovensky:** [Temešvár] 1. marca 1904. Moja drahá Iluška, kedy Vás môžem vidieť? Prosím, zlatko, napíšte. Milión horúcich bozkov mojej milej. [monogram]

(Iluska / Ilus is the usual pet form of Ilona, the addressee's name.)

## Uncertainties

1. **First mark of bottom line 4.** It is not a clean Morse sign. It is a long horizontal stroke that turns down into a short slant with a small tick, and a separate dot stands above it. It comes before `.-./.---/---/-./` (RJON), so the word must be ÍRJON ("write!"). I read it as Í. One possible account is that the writer made a cursive "í" (dotted stroke) instead of a Morse group. This letter rests on word sense alone.
2. **C = `.-.-` in CSÓK.** All four elements are clear (dot, dash, dot, dash) and none is hidden. This is the writer's slip or private sign, and the word is unambiguous ("millió forró csók").
3. **Stray dots in bottom line 2.** Three small isolated dots stand above the line: above the separator after M of MIKOR, above the separator between Á and T of LÁTHATOM, and above the last dash of O in LÁTHATOM. They lie off the writing line and change nothing. If they were meant as accents, the third would make O into Ó/Ö, which is not a word here ("láthatom" is correct as written). I leave them unassigned.
4. **S in ÉDESEMNEK.** The middle dot of `...` is an ink blot (a larger round dot). It is still a single dot between two dots.
5. **Question mark** after LÁTHATOM is a written "?" (not Morse).
6. **Monogram.** It is a looped initial crossed by a stroke, possibly two initials joined. I cannot read it with confidence, so I report it literally. The sister card hcp-1133 from the same correspondence is signed Richter Antal, but I do not claim this monogram is his.
7. **Date.** The dateline says III/1 (1 March), while the postmark seems to read APR 1. The portal file name says 1904-04-01. I report both as they stand. "Tv." for Temesvár is my interpretation of the abbreviation.
8. **Under the stamp** (address side): this cannot be inspected from the scans. Nothing is visible at the stamp edges.
9. Word division and punctuation in the Morse text are mine. Long-vowel accents in MILLIÓ, FORRÓ, CSÓK are added from the language, because the writer used plain O.

## Why I believe it is correct

- Every Morse sign on the card is transcribed: 4 + 3 lines, 7 groups in all. All decode under one key (International Morse, Hungarian É, and the writer's Á, which is already attested on hcp-1133). Only the two disclosed one-letter points depart from it.
- The output is fluent, idiomatic Hungarian of the period. It is a short love note that addresses the recipient by her pet name (Ilus/Iluska for Ilona) and fits the card's Easter-picture postcard format and the earlier hcp-1133 correspondence to the same address.
- The two blocks complement each other: a greeting and request, then kisses and a signature.

## Credit

Transcription, key transfer from hcp-1133 and decipherment: Claude Opus 5.5 (2026-11-03). No earlier solver work on this card.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave the verdict ACCEPT with four minor findings. All are accepted; none changes a decoded letter. After the changes `python3 -I ciphers/hcp-916/work/decode.py` was re-run from the repo root: all four hashes OK, and the output is unchanged (`B joined: ILUSKÁMDRÁGAMIKORLÁTHATOM?KÉREMARANYOMÍRJON`, `T joined: MILLIOFORROCSOKÉDESEMNEK`).

1. **Stray marks in bottom line 3 (fixed).** Confirmed on review/work/B3R.png: a small isolated dot below the separator before the R of ARANYOM, and an ink blob on the separator after that R. Neither is a Morse element. Added to Uncertainty 3 (below) and as a comment in work/morse_transcription.txt. The reading is unchanged.
2. **No closing "/" after top line 2 (fixed).** Confirmed on review/work/T23end.png: the K `-.-` of CSÓK is followed by no separator stroke. work/morse_transcription.txt now writes `.-./---/.-.-/.../---/-.-` without the final "/", with a comment. The decoder output is unchanged.
3. **HCPORTAL overprint (accepted).** The grey "HCPORTAL.EU · Collection: Tobias Schrödel" stamp over the start of the diagonal lines and the monogram is a modern collection mark, not part of the 1904 card. The signs under it (M of MILLIÓ, R of ROCSÓK, É of ÉDESEMNEK) were read on enlargements by both solver and reviewer. This is stated in the report.
4. **Monogram (accepted).** I note the reviewer's hypothesis of a cursive A crossed by a stroke with a looped second letter (possibly R), which would fit "Richter Antal" of hcp-1133. It stays a hypothesis; the monogram is reported as unread.

Additional point (from the human's note about steganography under stamps on the Jolánka series): this card is not in the Jolánka family, and its stamp is still attached, so nothing under it can be inspected. No hidden writing shows at the stamp edges or elsewhere on either side. The type therefore stays MASC/Morse; "MASC + Steganography" cannot be demonstrated here.

Updated Uncertainty 3: stray dots in bottom line 2 (three, as listed above) and in bottom line 3 (a dot below the separator before R of ARANYOM and an ink blob on the separator after it). None is a Morse element and none changes the reading.
