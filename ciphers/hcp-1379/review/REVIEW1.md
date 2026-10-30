ACCEPT

# Review 1 of hcp-1379 (pc_hcp_60), reviewer Claude Opus 5.5, 2026-10-30

Note on independence: the solver was also Claude Opus 5.5, so this is a separate session of the same model, not a second vendor.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1379/work/decode.py` from the repo root: 4 hashes OK, prints the five lines exactly as in `SOLUTION.md`, 52 letters, 1907-04-09 is a Tuesday.
2. **Independent decode.** `review/work/indep.py` holds my own transcription, typed from my crops, and a separately built table. Output: `my dearest i hope you are feeling better love from your own girl`, 52 letters. It is identical to the solver's. All 25 shifts are printed; only −1 (k=25) gives language.
3. **Key coverage.** Every token is decoded by the one shift. No cipher group is left over. I recounted 52 by hand: 2+7+1+4 / 3+3+7 / 6+4 / 4+4+3 / 4.
4. **Pixels, every word.** I rotated the un-converted original `work/hires/pc_hcp_60_adr.JPG` myself and enlarged it 3–7x with contrast (`review/work/a_…p_*.png`, `rot.png`, `low.png`). I did not reuse the solver's crops, apart from viewing `sis1397r3.png`. Word by word:
   - `Nz.` is clean: long diagonal, arch, one further leg, so a two-legged N. z, dot.
   - `Efbsftu` is clear. E, descending f, b, s, long f, t with a long bar, u. The solver's "run together" caution is, if anything, too modest: it reads well.
   - `J.` and `ipqf` are clear: dotted i, p, q, f.
   - `Zpv.` and `bsf.` are clear, with dots.
   - `gffmjoh`: g, f, f clear. j has a looped descender that runs up into o (`p_jolh.png`), which explains two strokes that first look like extra descenders. h clear. The `m` (`k_m_gffm.png`) is a compressed mass: one clear arch and leg, then a dark blob. Two or three minims cannot be counted firmly. Disclosed as weak in Uncertainty 3.
   - `cfuufs:` c, descending f, four minims, long f, s; two marks one above the other, so a colon is fair.
   - `Mpwf` (`l_capM.png`, `g_mpwf.png`): the long diagonal, then an arch to a leg, then a separate thick short leg with the tail into p. That is one more leg than the N of `Nz`, so **M stands on the pixels, not only on sense**. p and the final long f are clear; the middle is compressed minims.
   - `gspn`: pale split-nib ink but all four letters are visible.
   - `Zpvs.`, `Pxo` and `Hjsm.` are clear. The dot after Zpvs and the dot after Hjsm are present.
   - Faint `"`-like mark between gspn and Zpvs (`o_ditto.png`): really there, very pale, disclosed and left out. It sits in the gap and has no letter form.
5. **Language and fit.** Ordinary English of the period, one sentence plus a closing. Nothing forced. "Love from your own Girl" matches the formula; `SOLUTION.md` of hcp-1397 does record `Mpwf gspn zpvs. Pxo. Hjsm`. C. H. headings and the Wimborne postmark recur on sister cards (e.g. hcp-1373).
6. **Context.** Picture side reads "Loch Long. Highland Cattle", no writing. Address: Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. Postmark WIMBORNE 10 PM AP 9 07, halfpenny Edward VII stamp. Heading Tues. April 9th agrees with the postmark and the calendar. `work/reading.png` is correctly oriented.
7. **Restorations and sources.** No "completion" section exists; there is one solver round only. No restored letters. `NOTES.md` is consistent with `SOLUTION.md`, including the first wrong tries at line 3 word 2.

## Findings

1. **minor. Heading initial C vs G not disclosed.** `SOLUTION.md` gives "C. H." flatly and Uncertainty 7 discusses only the meaning. On this card (`n_head.png`) the first letter is a large loop with a low curved finish that runs into a small descending stroke, and it could be read G. Sister reviews are divided (hcp-1355, 1386, 1397; several read G. H.). Clear text, so the decipherment is unaffected. Fix: add one line stating the doubt.
2. **minor. "No restorations: every letter is read from the pixels" is slightly stronger than Uncertainties 2–3 allow.** The `w` of `Mpwf` and the `m` of `gffmjoh` are selected by the word, not counted from the strokes; the solver says so itself. Fix: say "no restorations; two letters (w, m) are chosen by word sense from compressed minims". Nothing about the reading changes: no other letter makes a word in either place.
3. **minor. Pencil "(11)" at upper left of the address side is not mentioned.** It looks like a later collector's or archive number and is not message content. One line in the report would make the account of the card complete.

No blocker or major findings. I tried to refute the reading via N for the `Mpwf` capital (MOVE), n for the `gffmjoh` m (FEEMING), and other shifts; each fails.

## What I could not verify

- The portal status and attachments (read from the solver's capture; I did not reopen the portal). `metadata.md` is taken as captured.
- That nobody has published this card elsewhere. The orchestrator's register check is taken as stated.
- The meaning of "C. H." The identity of the writer. Whether the hand is the same as on hcp-1386…1407: I compared only the cited formula and heading pattern, not the hand in detail.
