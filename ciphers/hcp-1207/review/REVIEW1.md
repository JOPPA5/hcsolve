REVISE

# Review 1 of HCP1207 (reviewer: Claude Opus 5.5, 2026-11-02)

The decipherment holds: key, transcription and nearly all of the reading survived the attempt to refute them. One passage is misread. Row 15/16 is not "haza Toriéktól" with an invented person Tori; it is the surname **Pásztoriéktól**, which needs no emendation and is the name Feri uses on sister card HCP1290. The fix is confined to that phrase, its translations and disclosures, plus small corrections listed below.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1207/work/decode_opus.py` runs. All four SHA-256 checks print OK. Its literal rows are identical to the block in SOLUTION.md, and the normalized text is identical.
- **Independent decode.** `review/work/my_decode.py` holds my own row reading as sign-class codes with a separate key table, compared with the ledger. 467 signs in 23 rows. 22 rows are identical. Row 13 differs only at the sign before *csak*, which I type as tall + tick and the ledger calls d, the near-homograph the solver already discloses (item 4). Caveat: I had seen the solver's ledger before I read the crops, so this is a check on the pixels, not a blind transcription.
- **Pixels.** My own crops in `review/work/crops/`, made by `rc.py` and `sep.py`: every row at 2x (`L0`–`L4`, `R0`–`R4`), the stamp square at 3x, the bottom edge, the address, the postmark, and 3–5x zooms of the difficult places (`z_*`). Every row was walked sign by sign. No sign is missing from the ledger and none is invented.
- **Key.** All main-row signs take a value in the HCP1216 family key except the disclosed stray in row 22. Nothing was added to the key to fit this card. The stamp square reads with the same key, with disclosed cursive variants.
- **Language.** Period colloquial Hungarian with the family's spelling habits (`ojan`, single for double consonants, dropped letters). Railwayman vocabulary (*vonathoz vezényelve*, *pihenőm*) is natural and fits Feri on HCP1290. Not noise forced into words.
- **Sources.** The portal shows no solution. The family key is credited. No undisclosed published solution is apparent.
- **Sister check.** `ciphers/hcp-1290` (FINAL): "elmegyek a Pásztorinéhoz is, hogy hadd tudjam meg, hogy van az én drága csillagom". Its address side has the same plain form *Szépreményű Tóth Jolánka úrleánynak*.

## Findings

1. **major: row 15/16 misread; the correct reading is Pásztoriéktól.** Evidence: `crops/z_r15end.png`, `crops/z_r16.png`, `crops/R3.png`, `crops/L3.png`. The signs are tall+short, two bars, right bowl, crossed diagonal at the end of row 15, then gamma, loop, F, i, e, k, gamma, loop, wave. The solver's own sign call is right. The fault is the choice of h for the h/p near-homograph. With p the row runs straight on: **p a sz t o r i é k t ó l**, "Pásztoriéktól", from the Pásztoris'. That reading:
   - needs no emendation, whereas the solver's needs sz for z and a missing a, and calls itself "the weakest word division on the card";
   - uses sz correctly: the writer has plain z in *haza* in row 14, and the two-sign sz here is a real difference the solver had to explain away;
   - needs no invented pet name Tori;
   - matches a named person in this correspondence (HCP1290), and fits the address: she is in Budapest, not her usual Jászárokszállás, so she may be a guest there. That last link is a hypothesis.
   Required: ledger comment, normalized text *Írja meg, hogy mikor megy Pásztoriéktól*, English ("when you are leaving the Pásztoris"), Slovak, and uncertainties item 3; add this p to item 5. The signs themselves do not change. NOTES says "surname" was tested, but records no Pásztori test, and the h/p option was evidently not tried there. The sense of what follows also tightens: *csak maradjon ön … ameddig lehet* means stay on at the Pásztoris'.
2. **minor: undisclosed dropped t.** Rows 12/13 read `latoga | hatom`, so *látogathatom* has lost a t at the row break. No sign is there (`z_r12end.png`, `z_r13.png`). The normalization supplies it silently; item 9 omits it, and the Hungarian has no bracket. Add it to item 9 and print *látoga[t]hatom*. Normalization brackets are also inconsistent elsewhere (for example *Szeret[e]tt* brackets the e but not the added t, and *ameddig* supplies d and g unbracketed); either bracket all of them or state that the normalized text is unbracketed.
3. **minor: count claim.** "Why it is correct" says *édesem* ×5. The script finds 4 (rows 14, 17, 20, 23), plus *édes* in row 1. Correct it.
4. **minor: the address disclosure is incomplete.** The last pencil line under the portal seal (`z_addrlow.png`, `sepRG.png`) is indeed unreadable to me as well; the end looks roughly like "-lleg…/-hegy". It is one line of plain address matter, partly covered by the portal's own seal, not a message clause. I judge that it does not make the card partial. There is also a small separate pencil mark at the extreme right edge above the end of row 23 (roughly "Hé/Hö"), not mentioned in SOLUTION.md. Either it is the end of that line or an extra note. Mention it, and keep both unread items in the report.
5. **minor: wording.** Item 5 contains garbled text ("*lehnagyobb* type shapes", "read p then h→"). Tidy it. List the h/p calls in one place, as the brief asks: p in *pihenőm* and *Pásztori-*; h elsewhere.

## Readings tested and accepted

- Row 3 end `s o` (`R0.png`, `z_r3end.png`): a right bowl with a top curl, as in row 1, then a loop. Accepted; c is not supported.
- Row 9 `7 0 orakor` (`z_orakor.png`): plain figures and plain cursive, the word plausibly *órakor*; the 0 stays unexplained, as disclosed.
- Row 9 `i` in *visza* and g in *regelre* (`z_r9mid.png`, `R1.png`): sense calls, disclosed, and alternatives give no word.
- Row 12 loop over two strokes in *latoga* (`z_r12end.png`): a visible overwrite, disclosed.
- Row 16/17 *mararadjo|non*: repeated *ar*, and the sentence reads. Accepted as an editorial normalization, disclosed.
- Row 22 stray sign (`z_r22.png`): real tick + long stroke between *gondol* and *kodom*, correctly marked {?}.
- Row 13/14 *de csak későn, nem érkezek haza*: awkward but read as written, alternatives disclosed.
- Stamp square (`stamp.png`): reads as claimed; row 3 t and row 4 are variants, disclosed.
- Postmark (`z_pm.png`): BUD… and 13 only, so the date claim is not over-read.

## Could not verify

- The last address line and the corner mark (finding 4).
- Whether Pásztori here is the same household as on HCP1290, though the name match in one correspondence is strong. Whether she lodged with them at the Budapest address.
- Why 0 follows 7 in row 9.
- Blind independence of my transcription (see above).

## Effect on status

After finding 1 is applied, the card is complete in the sense of the brief: every message clause reads, with one stray sign. FINAL needs no new round if the change stays this small.
