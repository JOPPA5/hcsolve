ACCEPT

# Review 1 of hcp-1132 (Debrecen goose-girl card, Morse) - Claude Opus 5.5, 2026-11-03

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1132/work/decode.py` was run from the repo root. All four SHA-256 checks
   print OK, and the 21 column outputs plus the bottom line (BL) match the table and the plaintext in SOLUTION.md exactly.
2. **Independent decoder.** `review/work/mydecode.py` is my own Morse table (International Morse plus Hungarian É `..-..`,
   Á `.--.-`, Ö `---.`, Ü `..--`). It shares no code with work/decode.py. Running
   `python3 -I review/work/mydecode.py work/transcription.txt` gives the same text column by column. Every token is a valid
   Morse letter, so no `?` appears. The key covers the whole transcribed ciphertext. It is standard Morse, so there is no secret key to be inconsistent.
3. **Transcription against the pixels.** I made my own crops of `work/hires/..._adr.jpg` with `review/work/crop.py`
   (autocontrast, enlarged, turned 90° anticlockwise as the solver says):
   - `review/work/r_right.png` covers C1-C5. Read sign by sign, it gives ÉDES JO KIS / URAM! KEDVES / SORAID MEG /
     KAPTAM! BO / CSÁS MEG É. This matches. The "!" in C2 and C4 is a stroke with a dot below it in the reading
     orientation, as described.
   - `review/work/r_mid.png` covers C6-C9. It gives DESEM HOGY / ÉN NEM VÁLA / SZOLTAM SO / RAIDRA DE SOK. This matches.
   - `review/work/left.png` covers C20-C21. C21 shows R L A K, then a two-mark "!!" group, then T Á N C O. This matches.
     C20 is harder because the columns lean, but the A-N-Y-A grouping is consistent with what is visible.
   - `review/work/bot.png` and `review/work/heavy.png` cover the bottom corner, which holds the disputed restorations.
     The bottom line reads `.-.. ..- -.` and then `-.` plus the horizontal foot of an L-shaped stroke, which gives LUNK.
     C11 ends `. - - .` plus the vertical arm of the same L, which gives Á. C13 ends in the heavy black stroke. The C10
     strike-through is a long line drawn through about five dots, near hires x≈800, y≈1810-2040.
4. **Language and context.** The plaintext is fluent colloquial Hungarian of the 1930s-40s: a wife's affectionate note
   ("kis uram", "kis feleséged") to a Debrecen hairdresser at a Debrecen street address. The stamp is the 1938 Debrecen
   Collegium issue. The plain joke "Vigyázz a kis libákra" fits the goose-girl picture. Names, place and date are coherent.
   The spellings as written (BOCSÁS, MOSTANÁBA, no Ó in Morse) are disclosed.
5. **Picture side.** I viewed `review/work/pic.png` and saw no handwriting. The only marks are the printed number 173 and the HCPortal watermark.
6. **Sources.** The portal status is Not solved, with no transcription or solution attached. I found nothing to suggest
   that a published solution was used.

## Findings

1. **minor - The shared L-stroke (uncertainty 3) is a context-driven restoration.** In `heavy.png` the L is clearly one
   continuous stroke. Using its vertical arm as the last dash of C11's Á and its foot as the last dash of BL's K is the
   only split that gives words (MOSTANÁBA / TÁNCOLUNK). The alternatives, MOSTANP plus LUNN, are nonsense. So the reading
   is very probably right, but it rests on word sense and not on separate marks. The solver discloses this correctly.
   The report should keep the wording that this is an inference.
2. **minor - The heavy stroke at the end of C13 (uncertainty 2).** In `heavy.png` it is a single thick, darker, possibly
   retraced stroke with a waist and a thickened foot. I cannot see a separate dot. Reading it as `-.` (N, giving ELMON|DOM)
   rests on the word ELMONDOM. This is disclosed. Keep the disclosure.
3. **minor - The plain note has three exclamation marks, not two.** `review/work/note2.png` (crop x1450-1750, y0-200,
   turned 180°) clearly shows "libákra !!!". SOLUTION.md gives "Vigyázz a kis libákra !!". Correct this in the
   transcription of the plain part and in the report.
4. **minor - Morse letter splits chosen by word sense** (É in C1, Y in HOGY, ANYA in C20) are listed. They are
   unavoidable in unspaced Morse and do not affect the reading.
5. **minor - The type label.** `MASC/Morse` is one of the allowed register labels and fits plain Morse. Note in the
   report that Morse has no secret key. No change is needed.

## What I could not verify

- **Under the stamp.** There is no image of the card without the stamp, and the user's collaborator reports that cards
  of other series often hide a message there. Nothing on this card points to one, but it cannot be ruled out. The solver
  should keep this as a stated limitation.
- **The postmark date.** It is not legible at this resolution.
- **The marks under the C10 strike-through.** They are not read, and I agree that they should not be.
- **The C20 boundaries** (`-.--` in ANYA) are hard to separate because of the column lean. I accept them on the
  strength of the coherent result.
