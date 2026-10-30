REVISE

# Review 1 — HCP 1540 (pc_hcp_221), Pepouš to Anna Tichá, 9 Sep 1903

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Reviewed state: DONE1
(earlier partial work by the OpenAI GPT solver, plus the "Completion and handover" section by
Claude Opus 5.5 as solver).

## What I verified and how

1. **Solver command.** I ran
   `.../python3 -I ciphers/hcp-1540/work/decode.py --indexed` from the repo root. It exits 0, and
   its hash and inverse checks pass. Its literal output is the **old partial reading**: B03
   `⟦unknown length⟧ned`, B04 `zv⟦unknown length⟧ti-`, B10 `⟦unknown length⟧ecny`. The token B04.029
   is still `q` (Z). It does **not** print the completed text claimed in "Completion and handover"
   (IHNED / KVĚTINOVÝ / SRDEČNÝ).
2. **Independent decoder.** `review/work/indep_decode.py` takes the glyph tokens and applies the
   family key from `ciphers/hcp-1545/work/key.json`, not the solver's key.json. Its output matches
   the solver's literal output row for row (B01–B10, M01–M02). Every glyph class in the record is
   in the family key, so no glyph is left without a key value. The key is the standard Anna Tichá
   family substitution, credited to earlier cards and to the published partial study by M. Egorov.
3. **Pixels.** I rotated `source/picture.jpg` 90° counter-clockwise myself
   (`review/work/crops.py`, `crops2.py`) and made 3–9x crops in `review/work/`. I compared these
   sign by sign with the record:
   - B01 (`cht5sm1 t4g q6 fqb3n4mg2 q s4qg3f6. bh6f4c, q5`), B05, B07, B08 and M01/M02 match the
     record.
   - B04 end (`kvet.png`): **`g f 5 d 4 -`** is plainly visible. The `5` sits under the brown oval
     line but can be read. There is no real "unknown-length" gap; the gap is one sign, E.
   - B10 start (`srd.png`, `b10L.png`): it is overinked, but `c h t` (S R D) can be read, followed
     by `5 s m 1`. It is the same form as the B01 opening. SRDEČNÝ is supported.
   - B03 after "(I.)" (`ihned.png`, `ihned_hc.png`): this is a blotted, crossed-over group about
     1.5 signs wide, followed by a clear `m 5 t`. I cannot read `4 r` (I H) in it; see finding 3.
   - B09 `hned` (`hned8.png`, `b09a.png`): five signs, **`r h m 5 t`**; see finding 2.
4. **Context.** The address reads Anna Tichá, učitelka, Pelhřimov. Čížkov is a village in the
   Pelhřimov district, so "vzpomínka z Čížkova" fits well. Ústí (the Ústí/Choceň/vrchní správce
   sister cards) fits. "Lístek květinový" (a flower postcard) fits, and this card is itself a
   flower-picture card. The Czech is natural 1903 private correspondence. Pepouš/Anunka match the
   family.
5. **Sources and status.** The portal shows "Not solved" with no attached solution. Prior
   published partial family work is disclosed. I found no undisclosed use of a published solution.

## Findings

1. **[major] The completed reading cannot be reproduced and the files contradict each other.**
   The "Completion and handover" section claims IHNED, KVĚTINOVÝ (and says "This corrects the
   recorded first sign (q→g)") and SRDEČNÝ. But `work/record.json` and `decode.py` were not
   updated: the single command still prints three unknown spans and `zv…ti`. The top of
   SOLUTION.md still says "partial … not FINAL" and "the unknown place and damaged words are not
   completed", while the end says "complete reading". The README asks for a single command that
   produces the full plaintext. Fix: update the record (B04.029 g; add B04 `5`; B10 `c h t`;
   B03 as a marked restoration), regenerate the output and hashes, and make the status statements
   consistent.

2. **[major] B09 has a transcription error: one glyph is missing.** The scan shows five signs
   before `b3`: `r h m 5 t` (9x crop `review/work/hned8.png`; the looped `h` is the same R-sign as
   in `bh6f4c` PRAVIS). The record has only four (B09.009 `r`, B09.010 `m`). The literal decode is
   therefore **HRNED**, probably a slip for *hned*, or a habitual spelling. It is not a clean HNED.
   This must be recorded, and either disclosed as `hrned [sic]` or argued for. The record's
   reading silently drops the sign.

3. **[minor→major for B03] IHNED in B03 is a restoration, not a reading.** The pixels show a
   blot, about 1.5 signs wide and struck over, before `m5t`. The claimed outline `4 r` cannot be
   confirmed. Given finding 2, the same writer may have produced `rh` here (HRNED/HNED with a
   correction) rather than `4 r`. *Hned/ihned* is certain from the sense, but the literal output
   should show something like `⟦blot: ih?/hr?⟧ned` and present "(i)hned" as an editorial
   restoration. The solver writes "partly restored", which is a disclosure, but the wording "its
   outline is that of 4 r" claims more than the scan shows.

4. **[minor] The g-versus-q argument for KVĚTINOVÝ is weaker than stated.** In this hand Z (`q`)
   often has a looped, g-like form: M02 `bh6qtm4m6ř`, B01 `s4qg3f6`, M01 `q685q4d3cd`. So the
   claim "looped g (K), not q" is not decisive on shape alone. KVĚTINOVÝ is still clearly right:
   *zvětinový* is not a word, the following `f5d4-/m3f1` is visible, and the picture side is a
   flower card. The solution should say that the reading rests on language plus the shape, not on
   the shape alone. The reading itself stands.

5. **[minor] The completion's editorial Czech adds undisclosed normalizations.** The earlier
   sections deliberately kept *tíden, svom, Anunku, prázdnináh, psaníco*. The completion paragraph
   silently changes these to *týden, svém, Anunka, prázdninách, psaníčko*. *Psaníčko* inserts a K
   that is not in the ciphertext. Either keep the literal forms or mark each normalization as such.

6. **[minor] The "unknown-length span" labels overstate the damage.** The oval is a pale filled
   outline and leaves the script readable. Two of the three spans (B04, B10) can be read in full
   on the pixels; only B03 is genuinely blotted. Revise the uncertainty section to match.

## What I could not verify

- The exact signs under the B03 blot, at the available resolution (1024 px scan).
- Whether HRNED in B09 is a writing slip or the writer's habit; I did not search the other family
  cards for HNED glyph by glyph.
- The address side was not re-examined in depth (it is plaintext and not enciphered).

The reading of the card is correct in substance. The fixes needed are to the record and output,
to the B09 transcription, and to how restorations are disclosed. Hence REVISE, not REJECT.
