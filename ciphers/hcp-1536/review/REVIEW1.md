REVISE

# Review 1 – HCP 1536 / pc_hcp_217 (Anna Tichá postcard, 26 Sep 1903)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Round 1, against DONE1.

## Summary

The reading is correct in substance. The Anna Tichá family key, applied to the
transcription, gives continuous, natural Czech of the period. The text fits the
card: Žirovnice u Počátek; Ústí, Choceň; St Wenceslas' day (28 Sep), two days
after the date 26./IX.1903; "already from Prague". It also fits the address
side, which has a **PRAHA 7** postmark and a Žirovnice arrival stamp of 27 IX 03.
I checked against the pixels and found one real transcription error, M01
ODSILAM → ODESILAM. One glyph in M01 (the R of PRAHY) is a restoration the
solver did not disclose. The Claude completion of U01 (MOJE) is visible enough
to stand. However, it was never put into the record, the command or the main
plaintext blocks, so SOLUTION.md contradicts itself. These are concrete fixes.
The reading stands, so the verdict is REVISE.

## What I verified and how

1. **Command from SOLUTION.md.** Ran
   `…/python3 ciphers/hcp-1536/work/decode.py` from the repo root. Hash checks
   pass; 11 rows; 390 keyed tokens → 392 letters; 1 unknown-length span. The
   output matches the "Literal Czech, as decoded" block line for line, including
   the `⟦U01:UNKNOWN-LENGTH⟧` placeholder.
2. **Independent decoder.** `review/work/my_decode.py` builds the key from the
   sister card `ciphers/hcp-1545/work/key.json`, not from this card's key.json.
   It relabels 7→y for J and ř→H for CH, and applies the key to
   `work/transcription.json`. Its output is identical to the solver's for all
   11 rows. Every transcribed sign is in the key, and there are no unknown
   symbols. Sign counts: 390 keyed, plus the "1" in the "U01" label. The
   card's key is identical to the family key (hcp-1545), apart from the two
   label changes.
3. **Pixels.** I rotated source/picture.jpg myself (`review/work/cw.png` for the
   main rows, a 180° rotation for the margin). I made 3×–14× crops:
   - every row B01–B09 and both margin rows at 3× (`review/work/b0*_x3.png`,
     `margin_x3.png`), read sign by sign against `transcription.json`;
   - U01 at 6×, 9×, 12× and 14×, with red-channel autocontrast
     (`u01_x6.png`, `u01b_x9.png`, `u01b_red_x9.png`, `u01c_x14.png`), and
     commas from the same hand (`comma2_x8.png`, `b04_tail_x4.png`,
     `b06_tail_x4.png`);
   - M01 opening word (`m01_head_x9.png`), M01 PRAHY (`m01_prahy_x9.png`,
     `m01_prahy_red_x9.png`), B05 ODOJETI (`b05_odojeti_x8.png`).
   - address side, viewed whole.
4. **Language/context.** The Czech is idiomatic period letter-writing:
   psánko, musil, komissi with -ss-, následkem toho, poněvadž. Names and places
   are coherent: Anuška = Anna; Choceň and Ústí (most likely Ústí nad Orlicí,
   close to Choceň); Žirovnice; Praha. "Loňského svatého Václava" fits a card
   dated two days before 28 September.
5. **Attribution.** SOURCES.md and SOLUTION.md disclose the family key's origin:
   hcp-1520/1527 and the public partial study by Maxim Egorov. The portal shows
   "Not solved" with no attached solution. I found no undisclosed use of a
   published solution.

## Findings

### 1. M01 first word is ODESILAM, not ODSILAM – a sign is missing from the transcription (major)

`m01_head_x9.png` clearly shows `3 t 5 c 4 8 6 n` for the margin's first
word. A full `5` (E) is written between the `t` and the `c`, touching the `t`.
The record has `3tc486n` and leaves it out. Correct reading: **ODESILAM**
(odesílám, the standard form). SOLUTION.md presents "ODSILAM" as an unusual
spelling kept on purpose ("kept literally"). It is a misreading, not a feature
of the writer's spelling.
Fix: change M01 in transcription.json to `3t5c486n`, regenerate the hashes and
counts (391 keyed tokens / 393 letters before the U01 change), and update the
literal, editorial and Slovak texts. Remove ODSILAM from the "unusual forms"
lists in SOLUTION.md and NOTES.md.

### 2. U01 completion (MOJE) is not in the record, the command output or the plaintext blocks; SOLUTION.md contradicts itself (major)

The "Completion and handover" section claims the word MOJE. However:
- `work/transcription.json` still has U01 with `glyph_count: null`, and its
  reason field says "MOJE is a contextual candidate only";
- the single command still prints `MO⟦U01:UNKNOWN-LENGTH⟧ ZA`, so it does not
  produce the full claimed plaintext, as README step 4 requires;
- the opening paragraph still says "partial transcription/decryption, not a
  fully solved … claim", and the Uncertainty section still says MOJE "is
  excluded from the literal reading … Channel/contrast crops … do not justify
  its recovery"; the literal, editorial and Slovak blocks all keep the
  placeholder; the comma after MOJE is missing from every block.

Pixel check of the completion itself: my crops show the following. After the
clear `n3` there is an angular 7-shaped sign. Its straight descender slants to
the lower left, which matches the y/J sign in `yc5n` JSEM (B03) and in
`3t3y5d4` (B05). It is not the hooked q/Z. Next comes the lower bowl of a
`5`, then a slanting stroke that descends below the line, then `q6`. The
baseline is visible along the whole span. No other sign bottoms fit between
these marks, so the span is two signs plus one mark: y5 + mark = **JE**.
**MOJE is supported by the pixels**, not only by context. One caveat: the last
stroke is longer than this writer's commas elsewhere (`bc6mg3,` and `2h6t2,`
are short ticks). Reading it as a comma is plausible, since grammar needs one
after the vocative "dušinko moje", but not certain. It should be described as
"probable comma".
Fix: record U01 as `y5` plus a comma, with a note that the tops of both signs
are hidden by the printed cherry. Make the command emit MOJE, flagged as
partly obscured. Rewrite or remove the stale "partial / MOJE excluded"
statements so the file states one position.

### 3. The R of PRAHY (M01, `bh6r1`) is not visible and was not disclosed (minor)

In `m01_prahy_x9.png` and `m01_prahy_red_x9.png`, `bh6` is clear. It is
followed by the dark printed stem of the leaf, faint specks, and then `1`.
No r-shaped sign (compare `rm5t` HNED or `d3r3` TOHO) can be seen there. The
sign is either covered by the stem or extremely faint. PRAHY is almost
certainly right: the address side has a PRAHA 7 postmark. Still, the R is a
restoration from context and from the postmark, and it must be labelled as
such in the transcription and in the uncertainty section.

### 4. Postmark evidence not used (minor)

The address side carries **PRAHA 7** (sender's office) and **ŽIROVNICE 27 IX 03**
(arrival). This independently confirms "Odesílám lístek již z Prahy" and the
one-day transit, and supports PRAHY in finding 3. SOLUTION.md calls these
"postal cancellations" without reading them. Add them as context evidence.

### 5. Stale status text from the earlier collaboration (minor)

SOLUTION.md and NOTES.md still say "No watcher, review, DONE/FINAL marker …
was created" and "The partial remains marker-free", while DONE1 exists.
Clean this up when revising, so the record is not misleading. The credit split
should stay: GPT root/collaborator transcription and key transfer on
2026-10-28; Claude Opus 5.5 completion on 2026-10-29.

## Checked and found correct (no action)

- Rows B02–B09 and M02 match the scan sign for sign at 3× in my reading.
  Examples: B04 `fhHm4` VRCHNI with the CH sign; B06 `t3 H3sm5` DO CHOCNE;
  B07 `y4q` JIZ; B09 `d4c4sgh6d5 84p6n` TISICKRATE LIBAM.
- **ODOJETI** (B05 `3t3y5d4`) is truly written that way (`b05_odojeti_x8.png`:
  3-t-3-7-5-d-4). It is rightly kept as the writer's form.
- B03 ending ODLOZITI: Z is the only letter in that position that gives a
  Czech word, and it agrees with the solver's shape comparison.
- KOMISSI with -ss- is a normal spelling around 1900.

## What I could not verify

- The scan is only 1024×674 px. Fine stroke details, such as the top of the
  U01 signs and the exact shape of the mark after JE, are limited by
  resolution. No higher-resolution image was available.
- The sender's identity: no signature. On sister cards he is "Pepouš", but
  nothing on this card names him.
- Which Ústí is meant (Ústí nad Orlicí is likely, given Choceň). This is not
  established by the card.
- Whether an earlier, unpublished solution of this card exists.
