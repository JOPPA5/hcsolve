# HCP 1375 / pc_hcp_56 — Caesar −1 English love postcard, 15 Oct 1907

Status: **whole message read (59 of 59 enciphered letters); review 1 verdict ACCEPT, findings addressed, no decoded letter changed.** Two abbreviation groups are kept literal; `tqjo` has one disclosed sign-level point. All work on this card by Claude Opus 5.5 (2026-10-30); no earlier work exists on this number.

## Origin

HC Portal cryptogram 1375 (`pc_hcp_56`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Picture side: printed view "St. Mary Redcliffe, Bristol" (Wrench Series No. 14921), no handwriting. Address side, plain: **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**; halfpenny Edward VII stamp, postmark WIMBORNE 10 PM OC 15 07, matching the plain dateline "Oct. 15th = 1907." and the portal date. 15 Oct 1907 was a Tuesday, matching the plain heading.

The message is written up the left half of the address side (turn the card 90° counter-clockwise; the portal's grey wheel watermark overlies it and is not part of the card).

## Cipher and key

Monoalphabetic Caesar shift, the same key as the Abbott sister cards hcp-1386…1407: each plaintext letter is written as the **next** letter. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

`(G. H.) Tuesday` and `Oct. 15th = 1907.` are ordinary writing. `E. L.` (twice) and `N & L` are abbreviations kept literal, as on the sister cards.

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Plaintext |
|---|---|
| (G. H.) Tuesday | (plain) |
| Nz. Pxo. E. L. Cpz | MY. OWN. [E. L.] BOY |
| J. xbt. pvu. gps | I. WAS. OUT. FOR |
| b. mjuumf tqjo | A. LITTLE SPIN |
| uijt. bgufsoppo | THIS. AFTERNOON |
| Nz. N & L gspn. | MY. [N & L] FROM. |
| Zpvs Pxo. E. L. Hjsm | YOUR OWN. [E. L.] GIRL |
| Oct. 15th = 1907. | (plain) |

59 enciphered letters, all decoded by the one key; 6 abbreviation letters kept literal.

English (the plaintext language; the portal lists Unknown): *"(G. H.) Tuesday. My own E. L. boy, I was out for a little spin this afternoon. My N & L from your own E. L. girl. Oct. 15th 1907."*

Slovak: *„(G. H.) Utorok. Môj vlastný E. L. chlapec, dnes popoludní som si vyšla na malú vyjažďku. Moje N & L od tvojho vlastného E. L. dievčaťa. 15. okt. 1907."*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1375/work/decode.py
```

Checks the SHA-256 of both `source/` images and both originals in `work/hires/`, then prints the full plaintext from `work/transcription.json`.

## Uncertainties

1. **`tqjo` = SPIN (the one real reading point).** `t` is secure: the barred form, identical to the `t` of `tqfdjbm` on hcp-1380. The second sign is a bowl; the next is a long dotted diagonal with a hooked foot. On hcp-1380 and hcp-1370 the `q` tail runs down-left from the right side of the bowl, and no such separate tail exists here. A hairline runs from the bowl to the top of the long diagonal, so I read the diagonal as doing double duty: stem of `q` and stem of `j` together (a shared stroke). That is a reading of the writer's stroke order, which a scan cannot prove. The hook under the bowl is not part of this: it is the ordinary foot of this writer's long `j` (same form in `uijt` and `mjuumf`), and the gap between bowl and hook is clean paper. Without the shared stroke the group is literally `tojo` / `tbjo`, decoding SNIN / SAIN, neither a word. SHIN and SKIN are English but fail on the sign, since the bowl is not `i` or `l`, and they make poor sense after "out for a little". The parallel `Mjuumf. Tqjo.` on hcp-1370 (30 Sep 1907, "having a little spin") has a clearer bowl-and-tail `q`, while this card has the secure barred `t`, so each firms up the other's weaker sign. This is mutual support, not independent proof, because hcp-1370 cites this card for its T and is not itself FINAL. The writer's cycling (hcp-1377: "going to bike to Wimborne") fits, but nothing on this card says what the spin was on. This is a sense-supported sign reading, not an unambiguous one.
2. **`mjuumf`.** Minims run together (`uum`), and the dot lies inside the first arch of `m`, about 90 px of the original scan left of the `j` stem, much further than on `uijt`, where it is just left of the stem. The letter count fits (m, long j, four minims of `uu`, three of `m`, final f with its long loop), no other word fits A ____ SPIN as well, and the same word stands on hcp-1370.
3. **`E. L.`, `N & L`, `G. H.`** are not expanded; their meaning is not proved. On sister cards the same groups occur; the shifted values (D. K., M & K) are not adopted. The `&` is unshifted. The first letter of `N & L` is read N from its two full downstrokes (as in `Nz`), but its second foot carries a short squared stub to the right (work/closing-N-stub.png) that `Nz` does not have, and the sister cards divide between N and M on this group (hcp-1370's review and hcp-1383 read M). So `M & L` stays possible. The letter is outside the 59 and changes no decoded word.
4. **Word-dots** are the writer's habit and placed irregularly; they are transcribed where visible and carry no meaning. The dots after `Cpz`, `tqjo`, `bgufsoppo` are not clearly present.
5. **The `o` of the second `Pxo` (row 6) is damaged.** It is a dark blot inside a grey ink halo with no visible counter (review/work/y_pxo2.png). It is read as `o` from the shape of the group and the formula, not from the sign itself; no other reading is plausible.

## Why it is correct

The key is one fixed shift, not tuned to this card, and it turns all 59 letters into a coherent sentence. The formula "My own E. L. boy … My N & L from your own E. L. girl" recurs on the sister cards to the same addressee. `Nz`, `Pxo` (except the blotted `o` of Uncertainty 5), `Cpz`, `gspn`, `Zpvs`, `Hjsm` were read from pixels here and then match; `bgufsoppo` (nine legible letters) and `xbt pvu gps` are not formula words and decode cleanly. Date, weekday, Wimborne postmark and addressee all agree with the correspondence.

No published solution of this card was found: the portal lists none and the orchestrator's check of the AI register (2026-10-30) has no record of it.

## Response to review 1

Verdict ACCEPT. All four findings are minor and accepted; no plaintext letter changed. `python3 -I ciphers/hcp-1375/work/decode.py` was re-run after the edits and gives the same output, 59 + 6 letters, hashes OK.

1. **`q` mechanism: fixed.** I looked again at review/work/z_tqjo.png and y_tq_hook.png and re-ran review/work/gap.py: rows 411–415 of the gap have minimum values 191–210 against paper 188, so the "faint trace" was wrong and is dropped. The hook is the `j` foot. Uncertainty 1 now gives the hairline and shared stem, and says that stroke order cannot be proved.
2. **"Only English word" and missing parallel: fixed.** Uncertainty 1 now names SHIN and SKIN and why they fail, cites hcp-1370 and states the mutual dependence. One update to the finding: hcp-1370 now has REVIEWED1 (verdict REVISE, not FINAL), and its review confirms the `q` there and likewise calls the two cards mutually dependent.
3. **Damaged `o`: fixed.** Confirmed on y_pxo2.png; added as Uncertainty 5, and "Why it is correct" now excepts it.
4. **`mjuumf` dot: fixed.** Uncertainty 2 now gives the position as measured (first arch of `m`, about 90 px left of the stem).

One addition of mine, not in the review: while comparing with the `M & L` finding in hcp-1370's review, I saw that the first letter of `N & L` here has a stub on its second foot (`z_nl.png`, `y_nl2.png`). I keep N, which is what the reviewer confirmed, and disclose M as an alternative in Uncertainty 3. No decoded letter is affected.
