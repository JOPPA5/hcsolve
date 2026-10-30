REVISE

# Review 1 – hcp-1432 (pc_hcp_113), Morse postcard, 12 Aug 1907

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1 (state: DONE1, no REVIEWED1).

**Summary.** The reading is correct: KINDNESS ON SATURDAY / VERY TIRED /
REACHED HOME / TRUE. It fits the cursive letter word for word. I checked every
group on my own crops and pixel measurements and confirmed both disclosed writer
slips (`.-.-` for C, `-.` for R). But the transcript, which is presented as
"literal pen strokes only", leaves out a conspicuous extra pen stroke in VERY
(finding 1). The context paragraph also misreads the address (finding 2). Both
fixes are small and documentary, and the plaintext does not change.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1432/work/decode_full.py`
   (run from the repo root) printed `source hashes OK`, 42 groups, 1
   non-alphabet group, 2 editorial readings. Literal output:
   `KIN | DNESSONS | ATURDAY | VERYTI | RED | REA{.-.-}HEDH | OME | TNUE`.
   The reading is `REAcHEDHOME / TrUE`, which matches SOLUTION.md.
2. **Independent decoder.** I wrote `review/work/my_decode.py` with my own
   Morse table and my own transcript, built from the pixels and not copied
   from `work/`. Its output is identical: 42 groups, 41 A–Z letters plus `.-.-`.
   It also marks the crossed dash from finding 1.
3. **Pixel check of every row.** I rotated `source/address.jpg` 180° with PIL
   (`review/work/crop.py`) and enlarged every row 3–14×: `r1, r2a, r2b, r3a,
   r3b, t1, t1z, cross, t2, h1, h1a, h1b, h2, h2b, c1, cz, cz2, s`.png. I
   segmented ink by luminance and blue-minus-red hue (`review/work/comps.py`).
   The ink is blue-black (b−r ≈ 0…+13). The printed POST CARD / LANGSDORFF
   lettering is brown (b−r ≈ −30…−45). The overlaid grey wheel watermark is
   neutral.
   - thanks-1/2/3: `-.- .. -.`, `-.. -. . ... ... --- -. ...`,
     `.- - ..- .-. -.. .- -.--`. Confirmed. The third dot of the final S lies
     on the printed "S" of LANGSDORFF. It is clearly ink (luminance 76–78
     against 140–150 for the print), so S is confirmed.
   - tired-1/2: `...- . [crossed -] .-. -.-- - ..` and `.-. . -..`. The
     raised dot after "not" (x≈600, y 349–354) sits about 5 px above the Morse
     dots and is bigger than they are. I agree it is not a Morse element. See
     finding 1 for the crossed dash.
   - home-1: `.-. . .- .-.- .... . -.. ....`. Group 4 at 6× has a heavy
     first element (9 px wide: an oval dot, not a dash), then dash, dot, dash.
     So `.-.-` is a faithful reading. The alternative `--.-` (Q) would be no
     better. The final group has exactly four dots before the slash, so it is
     H and not the digit 5.
   - home-2: `--- -- .`. Confirmed.
   - closing: `- -. ..- .`. Confirmed. I independently dumped luminance and
     b−r over the left curve of the printed P bowl (x 691–698, y 603–614).
     Values: L 120–145, b−r −30…−43. That is pure brown print, with no
     blue-black ink, while the dash inside the bowl measures b−r +2…+13. No
     leading dot exists, so the literal letter is N. U2 is correctly disclosed.
4. **Key coverage.** The standard International alphabet is used and nothing is
   tuned to the card. All 42 groups are accounted for. No other Morse runs are
   on the card. The picture side has no cipher.
5. **Language and context.** The text is natural Edwardian English and fills
   the cursive gaps exactly: "for all your [kindness on Saturday] evening",
   "not [very tired] when you [reached home]", "Your [true] Friend". The
   cursive signature "Louie" matches the LOUIE in the Morse of sister card
   hcp-1433 (same addressee).
6. **Published solution.** The portal says "Not solved" and has no attachment
   solution. I found no indication that a published solution was used. The
   credit to the earlier GPT solver is present and specific.

## Findings

1. **major – undisclosed crossed dash in tired-1 (VERY).** Between E (`.`) and
   R (`.-.`) there is a full ink dash, x 695–717, y 350–354. The letter-closing
   slash is drawn straight through it, so it looks like "†" (see
   `review/work/cross.png` and `t1z.png`). No slash stands between the E-dot
   and this dash. Taken literally, the group is `.-` (A, giving "VARY"), or the
   dash is struck out by the slash. VERY is plainly intended either way, so the
   reading stands. However, `work/transcription-full.txt` claims "Literal pen
   strokes only – no corrections here" and writes `...- / . / .-.`.
   SOLUTION.md U4 discusses tired-1 in detail but never mentions this mark.
   This is a third writer irregularity of the same kind as U1/U2, and it must
   be disclosed.
   **Fix:** add the crossed dash to the literal transcript (or a note on that
   row). Add an uncertainty entry stating the two readings (cancelled dash vs.
   `.-` = A) and why VERY is still read. Adjust the "40 of 42 decode literally
   to letters forming correct English words" claim accordingly.
2. **minor – address misread.** SOLUTION.md's context says "90 West Green
   Rd(?), Tottenham". On the address side (upright crop
   `review/work/addr_up.png`) the address reads "Mrs G. Groves, 90 Westbourne
   Rd, Barnsbury N." (Islington). Tottenham is only the postmark, that is, the
   posting office. Correct the address and keep sender location (Tottenham
   postmark) and recipient location (Barnsbury) apart. This matters for the
   report's context section.
3. **minor – faint dash of U in SATURDAY.** In thanks-3 the pen runs nearly dry
   (the T dash is grey). The dash of U (`..-`, x≈657–674, y≈233–236) is a very
   faint band, L≈200 and b−r −8…−10 against the background's −13…−15. Only its
   dark end (x 671–674) is solid, and that end is dot-sized. Without the faint
   band the group would read `...` (S). I accept U, because the band is slightly
   bluer than the neutral watermark lines and is horizontal, not diagonal. Still,
   it deserves a one-line note, because the transcript presents the group as
   unproblematic.
4. **minor – wording of U1.** The first element of the `.-.-` group is a heavy
   oval (9 px), larger than the other dots. The conclusion does not change.
   Saying "four clear marks" overstates how clean this group is, so a short
   note is advisable.
5. **minor – hcp-1433 cross-reference.** SOLUTION.md says the sister card's
   Morse "contains the name LOUIE" and uses it to support the signature. That
   is fine. Note, though, that hcp-1433's own SOLUTION leaves open whether
   LOUIE there is the addressee's pet name or the writer's signature. The
   genders and roles remain open, as the solver already says.

## What I could not verify

- Whether the crossed dash in VERY was a cancelled stroke or a written-over `A`
  (writer intent). Either way the word is VERY.
- The cursive salutation initials ("D. S.") and the faint pre-closing cursive
  scribble (U3). These are not ciphertext, and I did not re-read them.
- Anything beyond the 1024×674 scan the portal provides. A higher-resolution
  original might settle finding 3 and the P-bowl question definitively.

## Files

Reviewer scripts and crops are in `review/work/`: `crop.py`, `comps.py`,
`my_decode.py`, and the PNG crops listed above.
