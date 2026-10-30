REVISE

# HCP1290 review, round 1 (Claude Opus 5.5 as reviewer, 2026-10-30)

The key, the language and the bulk of the reading hold. Three ledger signs are wrong against the pixels, and correcting them changes the text. All three corrections remove problems the solution reports as open or as restored:

- the "unresolved word" `jeeléden`
- the unexplained `ó`
- the supplied letters in row 24

The solver's fixes are small, but SOLUTION.md, the translations, the ledger and normalized.txt must all change.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1290/work/decode.py` from the repo root: 4 hashes OK, 585 tokens. Its output matches the literal and normalized text in SOLUTION.md exactly.
- **Independent decoder.** `python3 -I ciphers/hcp-1290/review/work/review_decode.py` has its own key table and shares no code with decode.py. It reproduces the solver's literal text from the solver's ledger, apart from the three corrections below (584 tokens). It needs no value outside the family key. The letter profile is plausible for Hungarian: e 15.0, a 11.0, o 8.4, m 7.1, n 6.4, s 6.2.
- **Transcription.** I checked all 27 rows and the stamp rows sign by sign on my own 2.25x contrast crops of `work/hires/*_adr.jpg` (`review/work/crop.py`, `review/work/crops/s00L…s09R.jpg`, `stamp.jpg`). Doubtful signs were enlarged 3 to 7x (`review/work/z.py`; `r3end`, `r3a`, `r4start`, `r20o`, `r22blob`, `r24start`, `r24mid`, `r24m`, `s6`). This was a check against the ledger, not a blind re-transcription.
- **Stroke count.** Ink column profile for row 24 in `review/work/ink.py`.
- **Picture side.** Printed verse only ("Kis házikóm ablakánál…") and a photo of a rider. There is no cipher there.
- **Sister cards.** Grepped FINAL Jolánka-family SOLUTION.md files for parallels (hcp-1216, 1300, 1308).
- **Sources.** The solution discloses that no published solution was used. The portal attaches none (per SOURCES.md and metadata.md); I did not re-open the portal.

## Findings

### 1. Row 3 final word is `higy`, not `hogy`, and `jeeléden` dissolves (major)

Enlargement `r3end.jpg`: the sign after the h/p sign has a clear round dot above it and the narrow crossed-curve body of **i**. The o of `hogy` on the same card (rows 9, 11, 12, 21) has no dot and a rounder hooked form. So the ledger's `H O GY` in row 3 should be `H I GY`.

Rows 3 to 4 then read literally `higy | je el éden…`, that is **higyje el, éde[s]…** ("believe me, my sweet…"). This is the writer's own formula:

- hcp-1308 row 10 has literal `higyjeedesem`
- hcp-1300 row 8 has `higyje`
- hcp-1216 row 5 has `higgyjeel edesem`, followed by *édesem*

All signs of `jeeléden` were read correctly; only the word division failed because of the o/i error one sign earlier. Consequences:

- Uncertainty 1 falls away as an unresolved word. The remaining question is only the ending: `éden` is probably *éde[s], [é]n olyan…* (a dropped s and a dropped é), which agrees with the first-person *utazok* and with the solver's own side hypothesis. *édesem* with a slip is less close. The solver should state this as a restoration.
- The "Why it is correct" bullet "*hogy* ×6 decode identically" is false: it counted this sign as o. The true count is 5.
- All three translations need the passage filled in: "Believe me, my sweet, I am travelling in as good a mood now as when I started."

### 2. Row 20 `ó` is `i`: *Pásztorinéhoz is, hogy…* (major)

Enlargement `r20o.jpg`. The sign has the narrow triangular-loop body of **i**, the same as the i in `rine` in the same row and in `mejik` (row 16). It does not have the rounded hooked o, which stands two signs to the right in `hogy`. The mark above is a slightly elongated dot, not an accent stroke; ink dots vary on this card.

The text then reads `hoz is hogy`: **"elmegyek a Pásztorinéhoz is, hogy hadd tudjam meg…"** ("I will also go to Mrs Pásztori's, so that I may find out…"). That is plain Hungarian with no gap. hcp-1308 has the same construction (`szüleimhez{i}s`).

So `«ó» s` and uncertainty 3 go, except for the note that *Pásztori-* itself is a sense-based surname. The ledger token `O:acute` should be `I`. Fix all translations.

The dot/accent call rests on the body shape first. I regard it as firm, but it should be recorded as a sign-class correction.

### 3. Row 24 has one m, not two: *keze, de most* (major)

Enlargements `r24m.jpg` and `r24mid.jpg`, and profile `ink.py`. Between the dark e and the o there are exactly three strokes (x about 880, 904, 924), the first one retouched and thick. The ledger's `M M` needs six. No second m is on the card, so the ledger token is invented and the printed literal `kezedemmost` is wrong.

The true literal is `kezedemost`, which divides with **no restoration at all**: *keze, de most bezárom soraim* ("the hand of fate. But now I close my lines…"). The last e of *keze* is simply the first dark-ink sign.

Solver's uncertainty 7 and the normalization *[É]de[s]em, most* should be withdrawn. They supply two letters and a word the card does not have. The English and Slovak "My sweet, I now close…" must change. The ink-change statement also needs correcting: the dark ink starts with the final e of *keze*, and SOLUTION.md's "Rows 24 (from *edem*)" should reflect this.

Row 27 (`veledesem`) is a separate case; see finding 5.

### 4. `Why it is correct` overstates (minor)

"The joins were not chosen by me" and "Word sense decided only the listed points" do not hold for the *[É]de[s]em* division in row 24, which was a choice. Rephrase after the fixes. *hogy* needs the corrected count (finding 1).

### 5. Row 27 normalization should give the alternatives evenly (minor)

Literal `veledesem`. With finding 3 removing the row 24 parallel, *vele, [é]desem* no longer has the "same pattern" support the solution claims. *veled, [é]desem* is equally a dropped é and has the same cost. The formal address on the card favours *vele*, and that is the only argument. State it so; the reading itself is fine.

### 6. Undisclosed retouch in row 20 `hagy` (minor)

The sign after `ha` is a doubled, retouched g with a dot-like mark to its right, before y (crop s06R, row 20). The reading `hagy` (= hadd) is the best one, but it is not listed among the uncertainties.

### 7. Ledger comment does not mention the sixth stamp row (minor)

SOLUTION.md describes it, but the ledger says only S1 to S5, so `decode.py` prints no marker for the unread remainder. Add a `[UNREAD]` token or a comment.

### 8. Second postmark (minor)

SOLUTION.md says the postmark was not read beyond 16. The circular postmark at the stamp has legible letters (including S and E at the left arc, see `crops/pm2.jpg`, and a place-name ending in the large scan). I could not resolve a name; a possible …PEST reading is my hypothesis only. Say so or attempt it. It does not touch the plaintext.

## Readings I tested and confirm

- Key: all tokens map; no new value is needed.
- Row 24 first sign: heavy, but its body matches the z at the end of row 23 (upright with an upper-left stroke and a right bar), and differs from the clean + of `fojtatom` (row 26). z is safe, and more secure than the solution says.
- Row 3 `szen`: two long strokes, no p tick; n is right and *szé[pe]n* is a disclosed restoration.
- Row 21 `n` + `d`: agreed.
- Row 22 blot (`r22blob.jpg`): upright, heavy foot and a top flag. It is a retouched sign; `{j}` from sense stands and is disclosed.
- Row 27 first sign: dotless; `{i}` from sense stands and is disclosed.
- Row 6 bar: ink bar about three signs wide; nothing is legible beneath it. A small tick shows above the bar, and I cannot interpret it.
- All other rows, including row 4 (`je el`): agree sign by sign.
- Stamp rows: `csok | lom | szam | talan | szor` agree; ink partly lies over the triangle print. The sixth row is unreadable, agreed. `csók[o]lom` is disclosed.
- The signature is lost, the sender is not established, and the solver claims nothing beyond that.

## What I could not verify

- The final letters of `éden` (finding 1): the division is firm, the restoration is a judgement.
- Anything hidden under the row 6 bar, the end of the stamp text, and the signature.
- The date and place of the postmarks.
- The sender. *csapat*/travel fits a railway-type crew, and the family writer Feri (hcp-1216) passes Vámosgyörk by train, but this card does not name him. That stays a hypothesis.

## Required fixes for FINAL

1. Ledger: row 3 `H I GY`, row 20 `I` (not `O:acute`), row 24 single `M`.
2. Update literal, normalized text, all three translations and normalized.txt accordingly.
3. Rewrite uncertainties 1, 3, 7 and 10, the status line ("one unresolved word") and the "Why it is correct" section.
4. Add the row 20 `hagy` retouch and the row 27 alternatives.
