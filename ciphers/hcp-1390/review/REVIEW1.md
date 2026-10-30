ACCEPT

# Review 1 — HCP 1390 (pc_hcp_71), Caesar −1

Reviewer: Claude Opus 5.5, 2026-10-29. Role: reviewer (round 1, marker DONE1).

## What I verified and how

1. **Solver command.** `python3 ciphers/hcp-1390/work/decode.py` (run with `-I`) verifies
   source hashes and prints six lines: My Own Dearest / Many thanks For / grand Letter /
   to day / From your own / Girl, with the two unresolved fields labelled. Output matches
   the plaintext claimed in SOLUTION.md. 56 confirmed alphabetic positions.
2. **Independent decryption.** `review/work/indep_decode.py` decodes my own transcription
   (made from the scan, not copied from work/) with Caesar −1. All 56 letters of the body
   give `myowndearestmanythanksforgrandlettertodayfromyourowngirl`; a 26-shift sweep shows
   only shift 1 yields English. The key covers every alphabetic body letter with no exceptions.
3. **Transcription vs. scan.** I rotated `source/address.jpg` 90° CCW
   (`review/work/rot.jpg`) and made 3x, 5x and 7x high-contrast crops
   (`l12.png`, `l34.png`, `l56.png`, `l4tail.png`, `l4M.png`, `sig.png`, `sigsup.png`,
   `hjsm.png`). Sign by sign: `Nz. Pxo Efbsftu`, `Nboz. uibolt Gps`, `hsboe. Mfuufs.`,
   `up ebz.`, `Gspn zpvs. pxo`, `Hjsm` are all visible as transcribed (the `j` in Hjsm is a
   long slanted stroke, consistent with this writer's j on sister cards). Dots after many
   words are present in the ink and not transcribed; harmless.
4. **Language and context.** Fluent 1907 English love-card idiom ("many thanks for grand
   letter to day ... from your own girl"), identical in vocabulary and key to the Abbott /
   C. H. family hcp-1386…1407 (Wimborne postmark, Mr W. Abbott, Chudleigh, S. Devon,
   heading "C. H. Monday", date May 6th 1907 — matches portal date 1907-05-06).
5. **Disclosure / sources.** No published solution claimed or found; portal status Not solved.
   Earlier work by the GPT solver and the 2026-10-29 Claude completion are both labelled.

## Findings

1. **minor — stale, contradictory status text in SOLUTION.md.** The top of the file still
   says "Status: partial, not a complete solution and not submitted for review" and
   "No DONE1, FINAL, report or register entry is appropriate while these groups remain open",
   while the later "Completion and handover" section declares the message complete and
   DONE1 exists. The report and SOLUTION.md should carry one consistent status (message
   complete; two closing fields literal/uncertain).
2. **minor — the "Mu." signature transcription is not supported by the pixels.** At 7x
   (`review/work/sigsup.png`) the sign after the capital M is a small raised letter with a
   tall ascender and a closing loop (h/k/b-like), with a dot beneath; I see no `u` shape.
   The conditional decodings `Lt`/`Li` (and the "little" hint) therefore rest on a doubtful
   reading. Since the field is already reported as unresolved and nothing is expanded, this
   only needs the transcription note to say "M + raised h/k/b-like letter, unread" rather
   than "Mu".
3. **minor — the "××" after "to day." may be letters, not crosses.** At 5x/7x
   (`l4tail.png`, `l4M.png`) the two marks after the capital M (which is itself largely under
   the grey watermark band; a dot follows it) each have a small hook/loop at top-left and a
   long descending diagonal — they look like cursive `y y` as much as `× ×`. Under the key
   `yy` → `xx`, i.e. kisses either way, so the meaning is unchanged; the solution should
   mention the `y y` (enciphered xx) possibility rather than asserting plain crosses.
4. **minor — the single command does not print the full final reading.** `decode.py` and
   `transcription.json` still contain only the 2026-10-26 partial state; the M / ×× and
   signature fields appear only as notes. Acceptable because they are non-alphabetic or
   unresolved, but the report should say the command reproduces the body only.

None of these affects the deciphered body text.

## What I could not verify

- The expansion of the capital M after "to day" and of the M-abbreviation before "Girl"
  (initials, pet name, or enciphered letters); sister cards show varying closing fields
  of this kind and none resolves them.
- Whether the M on line 4 is complete: it lies under the watermark band of the scan.
- The farm name in the address (Stokelake? per sister hcp-1397) — outside the cipher.
