ACCEPT

# Review 1 of HCP1250 (reviewer: Claude Opus 5.5, 2026-11-01)

The reading stands. I tried to refute it on the pixels and found no sign value and no word that has to change. The findings below are all minor: disclosure gaps, one undisclosed alternative reading, and translation points. The solver can address them in the response section without a new round.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1250/work/decode.py` ran. All four SHA-256 checks print OK, it reports 570 signs, and all 32 printed literal rows occur verbatim in SOLUTION.md (checked by script).
- **Independent decode.** `review/work/my_transcription.txt` holds my own row-by-row reading as glyph names, made from my crops (`review/work/crop.py`, `crop2.py`, 1.5x tiles of the hi-res address scan as green-channel images, plus 3–6x zooms). `review/work/check.py` decodes it with a key table I wrote from the HCP1216 sign list, then compares it with the solver's ledger. Run from the repo root: `python3 -I ciphers/hcp-1250/review/work/check.py`. Result: 570 signs, 0 rows differ, after treating h/p as one sign and the three signs I refuse to read (row 14 overwritten, row 17 blot, stamp row 5 faint) as unknown. Limit: I had read the ledger before transcribing, so this is a check against the pixels, not a blind reading.
- **Coverage.** I read all 24 main rows and all 8 stamp rows, including the tail of row 24 past the card's vertical rule (`z24.png`) up to the right edge. No sign is left without a value, and the ledger has no token outside the key. Rows stand as segmented; the row 4/5 and 12/13 alignment noted in NOTES.md is correct. Stamp rows are upright, as claimed.
- **Zooms on every restoration and doubtful call.** Row 17 blot (`z17`, `r17c`), stamp row 5 (`a5`, `t12`), row 14 overwrite (`z14`), row 22 p (`z22`), row 23 tail (`z23`), row 24 tail (`z24`), row 19 s (`z19`), row 2 ss beside the stain (`z2`), row 6 *rais* (`z6`), row 8 d (`z8`), row 4 gap (`z4`), row 1 tail (`y1`), stamp row 1 (`s1`, `ys`), stamp rows 6–8 (`s7`).
- **Key.** It matches the HCP1216 table sign for sign. On this card *gy* is two signs, as disclosed. The tall+short sign serves both h and p here; I could not separate them on the pixels, so the solver's "word sense" label is right.
- **Stated repeats.** By script on the literal stream: hogy 4, mulat 4, mert 2, alig 2, idö 2, feri 2. All as claimed.
- **Language and context.** This is natural period Hungarian with the writer's known habits: dropped letters as in HCP1216, and *édes egyetlen reményem* as in HCP1216. The address reads *Szépremény…, Tóth Jolánka úrleánynak, Jász Árokszállás*, matching HCP1252/1253. The picture side is print only (Cigányprímás, Lári-Fári and a verse).
- **Disclosure.** The portal capture shows Not solved and no attached solution. Nothing in the solution suggests outside plaintext. The target is not in `register-exclusions.json` or `skip.txt`.

## Findings

1. **minor: row 6 alternative reading not disclosed.** The literal stream is `r a i s m e r t`, and no sign stands between a and i (`z6.png`), so *rá is* is what is written. This writer drops letters all the time, though, and the stamp field has *gondoljon néha rám*. So *gondoljon rá[m] is, mert nélkülöznöm kell…* ("think of me too, because I must do without…") is a live alternative. It also suits *mert* better than the current English "think of this too, that…", which stretches *mert* to "that". Give it as a disclosed alternative, or adopt it with the m in brackets. The plaintext signs do not change.
2. **minor: row 4 `mostanaba` normalized without notice.** The card has no n after the a, yet the normalized text prints *mostanában* with no bracket, and the item 14 spelling list omits it. Either keep *mostanába* (colloquial -ba for -ban) or bracket the n. Between that a and the j of *jó* there is also a short oblique ink stroke, about x 1245, y 333 in the hi-res scan (`z4.png`). It is real ink, not in the ledger, and not mentioned. It is probably a comma, and it would support the sentence break there. Disclose it.
3. **minor: row 17 restoration overclaims.** SOLUTION says "only a thick wave is compatible". On the zoom the blot has three legs joined at the top (`z17.png`, `r17c.png`) and could as well hide three strokes (m) as a wave. The pixels do not choose. The l rests on *egymástól* alone. The restoration itself is sound and is marked `[L]`, so only the wording needs changing.
4. **minor: stamp row 1 `kad-` is not a safe writer's error.** The sign after k is smudged (`ys.png`): one upper bar, then a thick lower mass that can be one bar or two merged. It cannot be told from three bars (e). Item 14 states "two bars for e" as a fact. Mark the sign uncertain; *kedvesem* stands either way.
5. **minor: row 22 p is more than "a heavy left stroke".** Under zoom (`z22.png`) there are three elements: a separate wedge-shaped blob touching the tall stroke, the tall stroke, and the short stroke. The blob may be a blot or a cancelled sign. It is not a token in the ledger. *a párom* stands, but say that an unexplained mark precedes the sign.
6. **minor: row 19 s of *Istenben* is damaged and not listed.** The sign has a hollow, abraded top (`z19.png`) and reads as a right bowl only with some allowance. The word decides it. Add it to the "word sense" calls.
7. **minor: accents are understated.** SOLUTION says accents are "mostly not readable". Clear ticks stand over bars in row 12 (*hatnánk*), row 15 (*enyém*), row 22 and stamp row 4 (*né-*). The ledger records none except ö/ü. No change to the reading is needed, but the statement should be softer, because these marks are evidence for the readings.
8. **minor: translations.** The English "rare with us" and the Slovak "u nás" add "with us", which the Hungarian lacks (*Mi sajnos ritkán van mostanában*). Slovak "na čo sotva, sotva čakám" does not carry *alig várom*; use something like "čoho sa sotva, sotva dočkám". Finding 1 also affects the English and Slovak of that sentence.

No blockers or majors. Stamp `[A]` is acceptable: there is faint pink over the seal between the h and the r (`a5.png`, `t12.png`), it is restored from *néha rám*, and it is disclosed. Row 14 overwrite: three bars crossed by a long stroke, as described. The tail of row 23 has three strokes, so *várom* is confirmed.

## What I could not verify

- The sign under the row 17 blot and the faint sign in stamp row 5 cannot be read from the pixels.
- The song quotation is not identified.
- The date comes only from the portal file name; I did not read the postmark independently.
- The Hungarian judgement is mine, not a native speaker's.
- My transcription was not blind (see above).
