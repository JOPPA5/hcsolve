REVISE

# Review 1 of HCP1278 (Claude Opus 5.5, reviewer, 2026-11-01)

Short version: the reading stands. The key, the word sequence and the translations hold on the pixels. One ledger sign is wrong and is described in SOLUTION.md as "clearly written"; the signature's last sign bypasses the key in the "literal" output; a few descriptions need correcting. The normalized Hungarian does not change.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1278/work/decode_opus.py` passes all four SHA-256 checks and prints the 17 rows and normalized text exactly as in SOLUTION.md. The decoder is a thin token mapper; its output is only as good as the manual ledger.
- **Independent decode.** I read the card from my own crops (`review/work/crop_r.py`, `crop_z.py`, `crop_y.py`, `crop_s.py`, output in `review/work/crops/`, from the hires address scan) into my own sign-class ledger `review/work/mine.txt` (264 signs, 17 rows) and decoded it with a separate key table in `review/work/verify.py`, which diffs it against the solver's output. This was not blind: I had read the claimed text first. Result: 15 rows agree. The two differences are row 9 (my literal `ehes` against the solver's `edes`, disclosed in the solver's item 5) and row 13 (finding 1).
- **Key.** Compared with `ciphers/hcp-1216/work/graphic-key.json` and the HCP1216 table: letter values are the same family key, no new values were introduced. c + s on this card is the family's "opposed bowls" cs.
- **Pixels.** Every disclosed point was checked on enlarged crops: rows 3, 7, 8, 9, 12, 13, 14, 15, 16, 17 and the stamp box. Rows 1, 2, 4, 5, 6, 10, 11 were read sign by sign at 2x to 3x.
- **Bar counts.** a/e was counted on every bar sign in rows 7, 9, 12, 13, 15 to 17; ink bands measured with `review/work/profile.py` where it mattered.
- **Sister claims.** HCP1243 and HCP1310 do have *Tudatom, hogy szerencsésen megérkeztem*. HCP1305 and 1308 do have the stamp greeting with a blotted ü, HCP1305 with *e távolból*. HCP1303 and 1309 do give Holes, but HCP1303's capital is uncertain and HCP1309's first letter is open between d/h/p, and each cites the other. HCP1296 has status work-in-progress (no markers) and itself says H is probable with K not excluded.
- **Language and context.** The text is natural period Hungarian, with this writer's habits (single for double consonants, *napokba*, *ij* for *ily*). The apology for a love-picture card in sad days fits the picture side. English and Slovak translations match the normalized text. No published solution; portal status Not solved, none attached. Addresses and the postmark ÁROKSZÁ… 27 / 912 are as stated.

## Findings

1. **major, row 13: the sign after *ezt* is a, not e, and SOLUTION.md misdescribes it.** The ledger has `E Z T E L A P O T` and item 10 says "*ezt e lapot* → *ezt a lapot* (three bars are clearly written, the e may be dialect or a slip)". There are two bars. `review/work/crops/y13a.png` shows the gamma, then two bars, then the wave. `profile.py` in the window under the gamma gives ink bands 1618–1624 (tail of the gamma's own top arm), 1648–1656, 1704–1722, so two bars. The control e in row 7 has three bars below the arm (925–939, 952–965, 979–995). The neighbouring a of *lapot* in the same crop has the same two wide-spaced bars. Fix: ledger token to `A`, literal row 13 to `runapokbaeztalapot`, delete the *ezt e* note. The plaintext gets better, not worse: *ezt a lapot* is as written, with no normalization.

2. **minor, row 16: the "literal" line does not print the sign as keyed.** The last sign of the signature has its own token `F.`, which maps to itself, so the "literal decipherment" shows Latin `F.` where the key gives r. The sign has the same form as the heavy r of rows 13 and 17; its point stands inside the bars, at the arm's lower right, rather than clearly "beneath" it. The family's f is a different sign (the upright cross). *Holes F.* may be right, as an initial in Latin capital amid cipher, and item 3 discloses it as an interpretation. But the literal output should show `r` (or `{r, read F.}`), and the normalized text should mark *F.* as read, not given. The whole signature is thus: first sign blotted, last sign interpreted, and the surname carried by mutually-citing cards. Say so in the summary line and do not rest on HCP1296, which is unfinished and has its own doubt about H.

3. **minor, row 15: item 1 understates the pixels.** See `review/work/crops/r15L.png`. Two blobs stand above a clear X with both diagonals visible at lower left, and to their right a short stroke merged with the blob and a full long stroke. That matches ü + d of row 14 (`r14L.png`). "One dot-like mark" and "neither sign can be read cleanly" are too pessimistic. The restoration stays disclosed, but item 1 should describe what is visible; it is not only a parallel of wording.

4. **minor, row 16 first sign.** Item 3 is fair but incomplete. `r16L.png` shows at least one, perhaps two, heavy slanted strokes left of the o loop, so the class is not safely d/h/p: n is also compatible. State it as open; *Holes* rests on the sisters alone.

5. **minor, row 17: the m of *maradtakat*.** The third stroke is short and is overlaid by two dark foxing specks (`r17.png`). m is by far the best reading (*naradtakat* is no word), but it rests partly on word sense; add this to the uncertainties. NOTES records the first reading *ner…*, SOLUTION.md does not.

6. **minor, unlisted blots and marks.**
   - Row 2: the c of *hogy*'s gy is heavily blotted or overwritten; not disclosed (the word is certain).
   - Row 11 ends with a blob point after the gamma (`y11.png`), as does row 3, but only row 3's is in the ledger. Treat both the same way. It is a plausible sentence stop.
   - Row 15: of the two "dots" over the first ö, one is a free blob and the other looks like the foot of row 14's d. Item 10 says visible dots; say this one rests on the word.
   - Calling marks "spatter" (item 7) sits awkwardly with accepting the mark over row 4's u as ú: many similar free marks stand on this card (over the r of row 2, under most k signs). Row 4's mark is larger, but say that ú is likely, not read. It changes nothing, since *út* is required.
   - Stamp box: the first letter of *csókolom* lies under a pink blot and is therefore restored; say so.

7. **minor, item 12: the second postmark is not mentioned.** A second cancellation rings the stamp box (`review/work/crops/pm2rot.png`), with letters like G and V or Y, and digits with 91. The likely departure office is not read. Report it as seen and unread; it bears on where the writer was.

8. **minor, normalization of *küldök*.** The row 14 sign is a clear k. *küldöm* is an editorial change disclosed in item 10, which is fine, but "Why it is correct" then quotes *küldök* as read with no choice. No fix beyond keeping the two distinguishable.

## Confirmed, no change needed

- Row 3 and row 8 blots: no letter is needed, and the surrounding signs are as ledgered.
- Row 7 m + stray tick: three strokes then a detached tick, with the k overwritten just before; *mostani* is right and the disclosure is adequate.
- Row 9 h-shaped d: literal *ehes*; *édes Jolánkám* decides it; disclosed.
- Row 12: three-bar e on both sides of z, three spatter dots beside z, *nezel*. *Nézze el* is an editorial reading, disclosed.
- Row 14 `#` over n: two strokes crossed by two bars, as described, resting on word sense, disclosed.
- h/p split by tick height: consistent in rows 8, 11, 12, 13 and 14.
- Rows 16–17 *tisztelem az ot maradtakat* is legible, and *az ott* is a sound normalization.

## Could not verify

- The first sign of row 16 and the true value of the last one: no pixel test decides them.
- Holes as the writer's surname beyond the cross-references above.
- What was under the row 3 and 8 blots, and whether the row 7 tick has any meaning.
- The two pen marks in the stamp box (unread by me too), the month, the second postmark's office, and the cause of the "sad days".
- My sign reading was not blind, so its agreement is a check on the pixels, not an independent discovery.
