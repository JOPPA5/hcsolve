REVISE

# Review 1 of HCP1289 (reviewer: Claude Opus 5.5, 2026-10-30)

The decipherment stands: the key is right, the text is real Hungarian and the card is a love letter from Feri to Tóth Jolánka about money and marriage. Five signs are mis-transcribed and one sign is missing from the ledger. Two of these errors change the meaning of the row 28 clause that the solver called weakest: the literal text is *ráérek* ... *foglalkozni*, so the English and Slovak subject there is wrong and the [lal] restoration is not needed. Several "writer's error" claims in the Uncertainties section are false.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1289/work/decode_opus.py` ran; all four hashes OK; 823 signs; its output matches the literal and normalized text in SOLUTION.md.
- **Independent decoder.** `review/work/indep.py` has its own key table, reads the same ledger and then applies my pixel corrections. Without the corrections it reproduces the solver's literal rows. With them it gives the diff in findings 1 to 5 and 824 signs. Run it from the cipher directory.
- **Transcription.** I read all 29 rows and the 8 stamp rows from my own crops of `work/hires/*_adr.jpg` at 2.3x (`review/work/crop.py`; `review/work/c/a1…h5.png, s.png`) and compared them sign by sign with the ledger. Contested signs were enlarged 5x to 7x (`review/work/zoom.py`; `review/work/c/z_*.png, y_*.png, m0–m3.png`).
- **Key.** It agrees with the HCP1216 table (section mark = k). All 22 sign classes used have a value, so the key covers the whole text. No sign is left undeciphered.
- **Restorations 1 to 5.**
  - Row 7 [v]: the lower-left chevron stroke shows at the blot. Acceptable.
  - Row 8 [d]: a solid blot with two prongs at the top. Consistent with d, and disclosed.
  - Row 19 [ü]: a cross shape is still visible under the dark ink and the two dots are clear. If anything, more secure than "restored".
  - Stamp row 4 [a]: top bar visible. Fine.
  - Row 29 [i]: the two strokes of n reach the worn corner and the i is lost. Fine.
- **Language and context.** Period love-letter Hungarian with formal address. Name, addressee and place are correct. The address side is in clear; the postmark shows Árokszállás and 22. The picture side carries the printed verse *Sokszor úgy szeretnék sírni*, which SOLUTION item 17 mentions only as "the printed poem". Sándor is a known acquaintance on HCP1216 and 1217.
- **Sources.** The portal metadata shows Not solved with no attachments. No sign of an undisclosed published solution.
- **Repeated-word claims.** *hogy* 7× confirmed by count; *boldog-* ×3 (one is *boldodog*); *pénz* ×3; *szeret-* ×4.

## Findings

1. **Major. Row 28: the sign after *ráér-e-* is k, not s.** The ledger has `F A E F E )`, read *ráér és*. The sign is the S-shape with a flat top (crop `z_r28S`), the same class as the k of *csak* and *mikettén* in that row, not the right bowl. Literal: *raerek*, so **ráérek**, "I have time", first person. No *és* is written here. SOLUTION item 12, the normalized Hungarian and all translations of the clause need revising.

2. **Major. Row 28: a wave sign was dropped from the ledger.** The card has `+ O G L A L K O Z N I`: + o g wave a wave k o z n i (crops `h2`, `y_lak`). The word is **foglalkozni**, written in full. The restoration *fog[lal]kozni* and the alternative *lakozni* in item 12 rest on a miscount, and the total becomes 824 signs.
   With findings 1 and 2 the clause reads literally *a Sándor meg ráérek meg foglalkozni*. My suggestion is "as for Sándor, I have time to deal with [him/that]" (*a Sándorral* would be the regular form), which leads naturally into "let only the two of us be loving". The current English ("he has the time and will deal with it") and Slovak are wrong. The case ending and what exactly is meant stay an open uncertainty to disclose.

3. **Minor. Row 10 *ades* is misread: the sign has three bars.** The bars are staggered (crop `z_r10end`), with the accent tick above. Literal: **edes**. Not a misspelling.

4. **Minor. Row 29 *vale* is misread: three strokes.** The sign after the chevron has three strokes (crop `z_r29vale`). Literal: **vele**. Findings 3 and 4 remove both parallels that item 9 cites for *de a lfeledtem*. On row 4 itself the sign has two bars plus a detached dark stroke below and to the left (crop `z_r4de`), the same offset pattern as finding 3 though with a wider gap. The solver says "a faded third bar is possible but not seen"; the stroke is seen and should be reported. *de elfeledtem* then needs no error.

5. **Minor. Dots missed, so two claimed oddities are false.**
   - Row 18 first *o*: two clear dots sit above it (crop `z_r18o`). Literal *köztün*, so item 11's "no dots on the first o" is false and *ösztön* is firmer (the s is still omitted, ü for ö).
   - Row 2 last sign: two dots above and to the right, on a loop with a tail (crop `z_r2end`). I read ö, not dotted i. Literal *köszö|nök*, so the misspelling *köszi|nök* in item 15 goes.

6. **Minor. Row 8 *jeljesíteni*: the first sign is not a plain inverted T.** It has both the foot of j and the top bar of t (crop `z_r8t`), an I-beam shape, most likely a correction between the two. The "j for t" in item 15 should say so; it is not a clean error.

7. **Minor. Ledger omissions and unflagged sense calls.**
   - Row 27: the second *elöbb* has clear dots (crop `h2`); the first has two marks above it (crop `z_r27el`) that may be dots. The ledger records neither, and item 15 lists *elobb* as a misspelling.
   - Row 28 *szeretetel*: the fourth sign after s z e is closer to the gamma than to F (crop `y_szer`, the grey portal stamp nearby). r rests on word sense and is not disclosed. The single t in *szeretetel* is not listed in item 15 either.
   - Row 28 *légy*: the disclosed "flatter sign" could equally be k by shape (crop `y_legy`); correctly disclosed, kept for the record.

8. **Minor. "Why it is correct" overstates.** It says the ledger turns all signs into Hungarian. With the fixes above, the count, the literal block and the list of writer's errors in SOLUTION.md all need updating, along with `work/ledger-opus.txt` and `work/normalized-opus.txt`, so the command reproduces the corrected text.

## Not verified / remains open

- The meaning of the row 28 clause beyond the letters (who or what Sándor concerns).
- *hogadja* = *fogadja* and *ottobi* = *utóbbi*: the signs are as the solver says (first sign h/p and o respectively). These are interpretations of misspellings and were disclosed. A sound alternative did not come up, but the original wording cannot be proved.
- Row 17 *merr*: the second F-like sign has a hook and is blotted. The reading *mert* is disclosed and I did not settle it beyond that.
- The date (month and year of the postmark). I did not attempt a date from the blurred cancellation.
- Sender identity with the Feri of HCP1216: plausible, not proved. No claim is made.
- I did not search external literature for a published solution; I checked the portal capture only.
