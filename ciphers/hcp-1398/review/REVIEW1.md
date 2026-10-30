REVISE

# Review 1 — hcp-1398 (pc_hcp_79)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. The solver's work is credited
truthfully: transcription and the Caesar −1 reading were done by the OpenAI GPT solver (2026-10-26).
Claude Opus 5.5, acting as solver, completed the signature (M → LOO) and handed over DONE1 on 2026-10-29.

## Summary

The reading is correct: the card is a Caesar −1 (each cipher letter is one place after its plaintext
letter) love note in English, "My own dearest boy, I only have this view in my album. Your girl, Loo."
I confirmed the key, every word and the signature initial on enlarged crops. One word, however, does
not match the ink. The manuscript has `efbstu` (6 letters, decoding to DEARST), but the transcription
gives `efbsftu`, which adds an `f` that is not on the card. SOLUTION.md also still contains stale
"partial / no DONE1" text, and the single command prints `[L/M]OO`, not the claimed final reading.
These are concrete fixes. The reading itself stands.

## What I verified and how

1. **Solver command.** `python3 ciphers/hcp-1398/work/decode.py` (output saved in
   `review/work/solver_output.txt`). The hash check passes. Output: `MY. OWN. DEAREST BOY. / I. ONLY.
   HAVE THIS / VIEW IN. MY ALBUM / YOUR. GIRL / [L/M]OO`, "51 frozen letters, 1 additional position".
   This matches the plaintext block in SOLUTION.md, but it does not match the "Completion" section's
   final reading (LOO).
2. **Independent decryption.** `review/work/indep_decode.py` applies Caesar −1 to my own transcription
   (no solver files used):
   `MY. OWN. DEARST BOY. / I. ONLY. HAVE THIS / VIEW IN. MY ALBUM / YOUR. GIRL / LOO`, 51 letters in all.
   One fixed key covers every letter. No substitutions or skipped groups are needed.
3. **Transcription against the scan.** I rotated `source/address.jpg` 90° counter-clockwise and checked
   every word sign by sign on 3–8× crops. Thresholded crops (`*_thr.png`) remove the grey printed
   watermark wheel.
   - `review/work/msg3x.png`: the whole message block.
   - `rows12_4x.png`, `dearest8x.png`, `dearest_thr.png`: salutation. `Nz. pxo.` and `Cpz.` agree with
     the transcription. The middle word: see finding 1.
   - `uijt8x.png`, `uijt_thr.png`: `uijt`. The u has two minims, then i, then j, each with its own dot,
     then a crossed t. THIS is confirmed. Without thresholding this group looks like "wjt", but the
     thresholded crop shows both dots.
   - `ibwf_thr.png`, `rows34_4x.png`, `row3_thr.png`: `J. pomz. ibwf`, `wjfx Jo. nz bmcvn` confirmed.
   - `row4_thr.png`: `Zpvs. hjsm` confirmed.
   - `sig6x.png`: signature. A lead-in curl, then three downstrokes joined by two arches, then two
     descending p's (the second with a closed bowl). That is a copybook capital **M**, not N, so
     `Mpp` gives **LOO**. The solver's resolution of the M/N alternative is supported by the ink. It is
     not forced from context.
4. **Language and context.** This is ordinary Edwardian English endearment. The phrasing matches the
   same couple's Caesar −1 cards to W. Abbott, Stokelake Farm, Chudleigh (hcp-1388 "Your own girl",
   hcp-1395, hcp-1397 FINAL "this one is a Scotch view … your own girl"). "This view in my album" fits a
   picture postcard. The address on this card reads "Mr W. Abbott, Stokelake Farm, Chudleigh,
   S. Devon", agreeing with the portal recipient "W. Abboú". The heading "Thursday" (plus overwritten
   marks) is plaintext and is correctly not shifted.
5. **Published solution.** The portal shows status Not solved with no attached transcription or
   solution (source/metadata.md, SOURCES.md). I found no sign that a published solution was used.

## Findings

1. **major — `efbsftu` is not what the card says; the actual group is `efbstu` (DEARST).**
   Evidence: `review/work/dearest8x.png` and `dearest_thr.png`. After `e` comes one looped `f`, whose
   up- and down-strokes look doubled. Then `b` (written like a 6), `s`, a tall stroke with a crossbar
   running over the next letter (t), and `u`. That is six letters. This writer's `f` descends well below
   the baseline (compare `ibwf`, `wjfx` and the f just after `e`), and nothing between `s` and `u`
   descends. So there is no second `f`. The ciphertext reads DEARST, a writer's slip (or a dropped
   letter) for DEAREST. The transcription adds the missing `f`, which is a silent normalization.
   Because of it, the letter count of 51 + 1 is really 50 + 1.
   Fix: transcribe `efbstu`. Print DEARST (or DEAR[E]ST, with the restoration marked) and disclose the
   restoration in SOLUTION.md and the report. Correct the counts.
2. **minor — the single command does not produce the claimed final plaintext.** decode.py still prints
   `[L/M]OO` and "signature not securely identified", while the Completion section claims LOO.
   Fix: freeze `Mpp` in transcription.json, or print the chosen reading along with the disclosure.
3. **minor — SOLUTION.md contradicts itself.** The header still says "**Partial, no DONE1.**" and
   "the signature is not securely identified". "Remaining limit" still says "No DONE1, watcher,
   reviewer…". The Completion section appended at the end says the opposite. Rewrite the top sections
   so that they state the current claim.
4. **minor — some context is left out.** The address side gives a recipient name (Mr W. Abbott,
   Stokelake Farm, Chudleigh, S. Devon) that is consistent with the sister cards hcp-1395/1397. The
   postmark looks like "…MBORNE" (perhaps Wimborne), 10 PM, with a halfpenny Edward VII stamp, which
   suggests 1902–1910. Both could be noted for the report. Linking the card to the 1907–08 couple is
   supported but not proven. "Loo" as a pet form of Louie/Louisa is correctly offered as conjecture only.

## What I could not verify

- Whether DEARST is the writer's slip or a pen skip; only the ink can be reported.
- The overwritten initials and the right-hand heading word after "Thursday" (it looks like "Today"),
  and the exact postmark town and date. None of them is cipher, and none affects the reading.
- The sender's identity behind "Loo".
