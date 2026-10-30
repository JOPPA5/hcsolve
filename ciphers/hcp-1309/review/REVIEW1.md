REVISE

# Review 1 of HCP1309 (reviewer: Claude Opus 5.5, 2026-10-30)

The decipherment stands: every sign I checked gives the claimed letter, and the plaintext is coherent period Hungarian. One false statement must be fixed (finding 1: the surname is on sister cards). The other findings are small disclosure corrections.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1309/work/decode.py` from the repo root: all four SHA-256 checks print OK. Every literal row and stamp row in SOLUTION.md is in the output, and the normalized text agrees.
- **Independent decode.** `python3 -I ciphers/hcp-1309/review/work/my_decode.py`. I retyped the key from `hcp-1216/SOLUTION.md`, typed my own sign transcription in my own sign names from my own crops (`review/work/crop.py`, `review/work/crops/`), and compared letter by letter with the solver's output. Result: 25 rows, 0 differences, 361 signs, 22 sign types. It treats the 20 long+short signs as one class and ignores accents and `[ ]`. Limit: this was not blind, because I had read the ledger first.
- **Key coverage.** No sign outside the HCP1216 key. The only unread stretches are the row 13 deletion and the stamp smear. c and f each occur once, so this card alone cannot confirm those two values.
- **Transcription against the scan.** I read all 19 rows and the stamp field at about 1.15x from the hires original, and enlarged these at 2–5x: rows 3, 4, 5, 6, 7, 11, 13, 14, 16, 18, 19, the stamp smear, and both postmarks.
- **Each claimed restoration:**
  - Row 11 `[o]`: loop visible under a heavy overwrite, sense-supported. Fine.
  - Row 14 `[e]`: three bars over an earlier loop. Fine.
  - Row 14 `-tánt`: one clean bar, plus the ends of a second bar showing on both sides of the pale blot (`blot14.png`). It is a, as claimed, not an F.
  - Row 16 `[a]`: two bars with slanted strokes between them, a #-like block, not a clean a. It looks like bars written over two strokes, and S6 has a similar block. Sense-supported, as disclosed.
  - Row 18 `[c]`: a filled tall form open to the right, consistent with a left bowl, with a dot to its left. Sense-supported, as disclosed.
  - Row 6 last sign: long + short, as disclosed.
  - Row 3 s of *soraim*: a right bowl touched by the loop of the i above it. The solver calls this the y-descender; it is the i in row 2, and the reading is unaffected (`r3s.png`).
  - Row 13: the two strike lines run through the stretch and the lower one crosses the dotted i, as stated.
- **Plaintext.** Normal period Hungarian. Clear return address, addressee and family formulas agree with the cipher text. The content fits the family: Szentmihály also appears in HCP1213, and Rákospalota cancels appear on HCP1216, 1299, 1307 and 1308. Word division runs correctly across rows (*ki|vanom*, *la|kom*, *szomba|ton*, *jo|lankam*, *Árok|szállás*).
- **Published solutions.** The portal attachment list in `source/metadata.md` shows no solution or transcription. I saw no sign that one was used. I did not search for one myself.
- **Key attribution.** The earlier work on the family key is credited correctly.

## Findings

1. **major: "No sister card gives his surname" is false, and the surname should not stay {H|P|D}oles.** SOLUTION.md Uncertainty 1 makes this claim, and the normalization and all three translations use the placeholder.
   - HCP1303, also a Feri card, has in plain pencil at the bottom, after the cipher: *cím Holes*, followed by a faint word. That is the same "address: name" construction as here. I viewed it on a crop of `hcp-1303/work/hires/…jolanka-84_adr.jpg` (`review/work/crops/s1303.png`); *Holes* is clearly written.
   - HCP1296 is signed in plain writing `[H?]al[o/e]s Ferenc`, a weaker parallel with an uncertain vowel in the first syllable. `hcp-1296/SOLUTION.md` itself leaves the identity open.
   - Fix: report *Holes Feri*, stating that the sign itself is only the d/h/p class and that H rests on the HCP1303 clear word. Correct the statement. HCP1303 is at DONE1, still unreviewed, but its clear word can be seen directly.
   - This also adds support for the `[c]zim` reading in Uncertainty 11, and that should be cited there.

2. **minor: Row 7 final a is presented as clean, but it rests on sense too.** The ledger has plain `A`, and the notes say "the bars at the margin are two". The two bars are there, but a red dot on the divider rule sits where a third bar would fall (`r7.png`). *lekom* gives no word, so a stands. Add it to the sense-based calls.

3. **minor: Stamp field: visible residue in the smear is undisclosed.** Row S2 is given as `le{smear}le…`. An enhanced channel (`smear.png`) shows, below the first *le* and left of *sem*, a hook-like sign and a long bar. These are remains of further signs, or set-off, between S2 and S3. I cannot read them. Uncertainty 2 should say that the unread material is not only a stretch of S2 but also lies lower, at this level.

4. **minor: Literal accents are inconsistent.** Row 4 has a tick above the gap between a and r of *már*, but the ledger gives plain A and `mar`, while other ticks are recorded (`r4.png`). The ticked `é` in row 4 `él` (of *eljöttem*) is also missing from the spelling list in item 13.

5. **minor: The citation for the formula is partly wrong.** Uncertainty 7 cites *találja soraim* from HCP1212, 1315 and 1317. The wording is confirmed in HCP1315 and 1317, but the phrase does not appear in `hcp-1212/SOLUTION.md`, and the grep there finds no *talál-* form at all. Drop 1212 or check its wording.

6. **minor: Postmarks are not described.** "The date is not legible" is true, but there are two strikes, neither mentioned.
   - Right of the stamp, a ring shows three clear capitals, read as `?AL`. The first is a closed O/D-like form. A reading PAL(OTA) would need a P whose stem I do not see, so I do not claim it.
   - Top centre, a faint strike shows only broken characters and a barred block.
   - Say they exist and are unread, so that a reader does not assume the card has none.

7. **minor: Normalization could stay closer to the card.** *bövennem* is normalized to *bővebben nem*, although *bőven nem* is what is written and the sense is the same. The change is disclosed, but *bőven* is the better printed form.

## What I could not verify

- What stood under the row 13 deletion, in the S2/S3 smear, or under the overwrites in rows 11, 14, 16 and 18.
- The date, and either postmark's place.
- Which Szentmihály is meant.
- Whether Feri, *Holes* of HCP1303 and `[H?]al[o/e]s Ferenc` of HCP1296 are provably one man. Name, formula and family context point that way.
- Whether a published solution exists outside the portal.
