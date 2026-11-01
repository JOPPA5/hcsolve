ACCEPT

# Review 1 of hcp-1252 (Claude Opus 5.5, reviewer, 2026-11-01)

The cipher block reads as claimed, sign by sign. Only minor issues remain, all in the wording of SOLUTION.md or in the plain-handwriting part.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1252/work/decode_opus.py`: all four SHA-256 checks print OK. The eight rows match the "Literal decipherment" block in SOLUTION.md exactly; 180 tokens.
- **Independent decode.** `review/work/indep_decode.py` uses my own sign names and my own key table, and does not read the solver's ledger or script. It compares with the block in SOLUTION.md: all 8 rows SAME, 180 tokens. Limit: I had seen the solver's text before typing my names, so this proves the sign-by-sign agreement and the arithmetic, not a blind reading.
- **Pixels.** From `work/hires/..._adr.jpg` I made my own crops (`review/work/crop_review.py`, `crop2.py`): every cipher row at 2.5x in two overlapping halves, details at 5x. I checked every sign of all 8 rows, not a sample. Specific checks:
  - Row 1: three gamma signs and four e between the r and the d, so *szeretetet* as disclosed. The third gamma has an attached branch, not the detached tick of h.
  - Row 2: the blot after *sorai* keeps a top bar and a stem, and t is the only fit. The inked sign in *megkaptam* has a tick on the right (h/p), and two three-stroke groups stand for *mm*.
  - Row 3: *o* has no dots at the first vowel; the second and third o have dots (those over the third fall in the band just under row 2). The ledger is right, and a dot follows the k.
  - Rows 3 and 4: the hyphen in *örü-lök* is written.
  - Row 4: *szoli* is followed directly by three strokes, two bars, F, so no t is on the card. The solver's bracket is honest.
  - Row 6: left tick in *édesem, kedvesem, haragudjon*; right tick in *ne haragudjon*'s h.
  - Row 7: the digits have a flagged 1 and a closed ring with no tail, unlike the tailed cipher loop o on the same row. Digits are correct.
  - Row 8: two distinct waves (coordinates checked across the crop overlap), *e n n i*, closing dot.
- **Key and coverage.** The sign classes agree with hcp-1216's legend (tick side for d vs h/p; h/p homograph; dotted o/u). All 180 tokens have a value: 174 letter signs, plus 2 digits, 2 dots, 1 comma, 1 hyphen. Counts in uncertainty 8 are correct (h/p 4, d 7, z 6).
- **Language.** This is natural Hungarian of the period and a private register. The move to *tegezés* suits a courtship card and is unlike a forced text. The writer's spellings (*kel, mer*) and salutation match hcp-1216; there *mer* → *mer[t]* is on record.
- **Plain handwriting.** I read each row at 1.5x plus the stamp corner at 2x. The transcription holds: dates and times, *rendezőre érk.*, *számítsa ki mit kerestem*, *fizetne 6 tized fil*, *kilométerenkint*, *33 órát a 8 fil*, *2 korona napidíj*, *10 órára*, *legközelebb bővebben*, *isten vele édesem*, *Csókolom számtalanszor*, and *Feri* (faint, under the stamp). The address also holds.
- **Sources.** The portal capture has no solution or transcription. Nothing in the directory suggests a published solution was used. `metadata.md` agrees with SOURCES.md. Not on `skip.txt` or `register-exclusions.json`.
- **Internal check.** The claimed pay sum is coherent: 237 km × 0.6 f + 33 h × 8 f + 2 K is about 6.06 K, so the sum is a plausible figure; it does not settle the third digit.

## Findings

1. **minor: the unread itinerary phrase should be stated as a limit wherever completeness is claimed.** Third plain row: *{vigas} in. {18 ól. u}*. The cipher is complete; this fragment sits only in the unenciphered part. It should stay outside any claim of a complete reading in the report. The solver dropped *vissza*, yet the sequence asks for a return leg (out to Érsekújvár, then arrival back at the yard on the 11th), so *vissza in[dultam]* ("started back") is worth recording as an open hypothesis. The pixels are v, i, a descending z/g-like letter, then a/o and s, so I cannot confirm it. Keep the phrase untranslated, but the current gloss "dep.(?)" could carry this.
2. **minor: *mer* is argued in a slightly circular way.** Uncertainty 2 cites *mer* to support a dropped t, while uncertainty 13 reads a word that looks like *men* as *mer*. In the crop that word does look like *men*. Support from hcp-1216 is sound; the citation within this card is not independent. State it as coming from hcp-1216 only.
3. **minor: the title asserts what the text says is inference.** "a railwayman's pay sum" in the heading, while uncertainty 14 says the writer's job is not stated. The inference is strong (*rendező*, km pay, hours, day allowance), but mark it as such in the report.
4. **minor: "every one of the 180 tokens" overstates the key.** Six of the 180 are digits and punctuation, so 174 are key signs. Say so in the report.

## What I could not verify

- The third digit of *23[7?]* and the 1913-06-13 date (postmarks unreadable; the date comes only from the filename).
- Whether *rendező* means marshalling yard as used by this writer; no further card text was checked for it beyond a directory search, which shows the word also on hcp-1247, 1248 and 1267 (not read).
- The accents in the normalized text, which are mostly supplied, as the solver says.
