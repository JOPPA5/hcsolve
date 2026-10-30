# HCP 1350 / pc_hcp_31 — Caesar −1 English love postcard, Thursday 7 March 1907

Status: **whole message read; review 1 verdict ACCEPT, reading unchanged.** No letter is restored in the transcription or the literal plaintext. Eight small points are disclosed under Uncertainties.

All work on this card by Claude Opus 5.5 as solver, 2026-10-30. There is no earlier work on this number. No published solution of this card was found or used; the portal shows status Not solved with no attached transcription or solution.

## Source and context

Portal record https://crypto.hcportal.eu/dashboard/cryptograms/1350 (`pc_hcp_31`), date 1907-03-07, language Unknown, recipient field "W. Abboú" (catalogue misspelling of Abbott). See `SOURCES.md`, `source/metadata.md`.

- Picture side: printed colour view "Weymouth, view from Sandsfoot Castle", no handwriting.
- Address side: Frith's Series No. 52870, halfpenny Edward VII stamp, postmark 10 PM MR 7 07, town read as WIMBORNE: only WIM and traces under the stamp design are legible here, and the rest is taken from the same postmark form on hcp-1354 (MR 5 07) and hcp-1353. Plain address: Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. Pencil "4" at the top left (not part of the message; presumably a collector's mark).
- Plain date at the end of the message: "Thursday. March. 7th". 7 March 1907 was a Thursday, the postmark day.
- The grey A–Z disc and building logo on the scans are an overlay of the scan, not part of the card.

## Cipher and key

Caesar substitution: each plaintext letter is written as the **next** letter of the alphabet (decrypt −1). The date is in clear.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

Read from `work/hires/pc_hcp_31_adr.JPG` rotated 90° counter-clockwise (`work/reading.jpg`, enlarged crops in `work/crops/`). The dots follow the manuscript and are not significant.

| Ciphertext | Plaintext |
|---|---|
| Nz. pxo. efbstu. Cpz. | My. own. dearst. Boy. |
| xibu bo. vofyqfdufe | what an. unexpected |
| Tvsqsjtf. uijt | Surprise. this |
| npsojoh. Cpui | morning. Both |
| wfsz. ojdf. Zpvs. | very. nice. Your. |
| mpwjoh. hjsm. Mpp | loving. girl. Loo |
| *(in clear)* Thursday. March. 7th | |

**English (original; punctuation editorial):** "My own dear[e]st boy, what an unexpected surprise this morning. Both very nice. Your loving girl, Loo. Thursday, March 7th."

**Slovak:** „Môj vlastný najdrahší chlapče, aké nečakané prekvapenie dnes ráno. Obidve veľmi pekné. Tvoje milujúce dievča, Loo. Štvrtok, 7. marca."

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1350/work/decode.py
```

It checks the SHA-256 of the four image files, decodes `work/transcription.txt`, tests the round trip, and prints each line, the letter count (78) and the plaintext.

## Uncertainties

1. **`efbstu` (`work/crops/dearst.png`).** After `s` comes the barred tall `t`, then a low `u`, with no `f` between them; this writer's f has a long descender and none is present. The literal decode is DEARST. The transcription is not altered. FINAL hcp-1398 has the identical opening `Nz. pxo. efbstu Cpz.` with the same six letters, confirmed in its review, while hcp-1356 writes `Efbsftu` in full. So this may be a habit of the writer as much as a slip. The English gives dear[e]st, with the E marked as editorial.
2. **`t` of `Tvsqsjtf` (`work/crops/z_full.png`).** This sign is 3-shaped with a long tail curling left below the line, unlike the plain `t` of `uijt` and `efbstu`, and it is the one sign on the card read from the word and not from its shape. It is not this writer's z: all four z on this card (`Nz`, `Cpz`, `wfsz`, `Zpvs`) are flat-topped Z forms, so the sign should not be taken as a tailed z or as an unshifted z of "surprize". Taken as cipher z it would give SURPRIYE, which is not a word. I read it as `t` from the sense. hcp-1353 has the same word, `tvsqsjtf`, with the same tail and hooked foot in this position (`ciphers/hcp-1353/work/crops/surp.png`), but a barred head and not a 3-head, so that parallel covers only the lower half of the sign. Whether it is a t or a personal form is unresolved; the sense SURPRISE is not in doubt.
3. **First letter of `Cpui` (`work/crops/both.png`).** The capital has a curled head, as does the C of `Cpz` (`boy_c.png`) in heavier ink. Taken as E the word would be DOTH, which gives no sense here. What "both" refers to is not stated; presumably two things received that morning.
4. **`Mpp` (`work/crops/moff.png`, `compare_p.png`).** The two `p` differ: the first has a closed bowl, the second an open curled bowl like the `p` of `Cpz`. The capital has three downstrokes after its lead-in, the same count as the m of `mpwjoh` on this line, while the N of `Nz` and the n of `npsojoh` have two (`work/crops/compare_mn.png`). The strokes are close together, so this rests on a small difference. `Mpp` is also the accepted signature on hcp-1398 and is read on hcp-1353 and 1354, cards of the same weeks (postmark 5 March on 1354), and the outline here matches `ciphers/hcp-1353/work/crops/tail.png`. This group is a signature, not a checked word. That Loo is a pet name is conjecture.
5. **Two irregular signs (`review/work/cmp.png`).** The x of `pxo` is Y-shaped with a foot, its strokes merging, unlike the open crossed x of `xibu`. The w of `wfsz` opens with a tall stem unlike the low w of `mpwjoh` and could be taken for a b at first sight. Only OWN and VERY make sense, and `Nz. pxo.` is the opening of hcp-1398.
6. The first sign of `vofyqfdufe` and the `d` of `ojdf` are somewhat ligatured but no alternative gives a word. The final `e` of `vofyqfdufe` is raised above the line for lack of room at the card edge.
7. The town of the postmark is partly inferred (see Source and context).
8. Writer's identity and sex come only from the formula "your loving girl". Weymouth on the picture has no stated connection with the Wimborne postmark.

## Why it is correct

One fixed shift, the key already established on the Abbott cards, gives connected English from all 78 letters: the long words `vofyqfdufe`, `Tvsqsjtf`, `npsojoh`, `mpwjoh` are not formula words and could not be forced. The opening and closing match the couple's formulae, and the plain date matches the postmark and the weekday. Sister cards were used as a hypothesis source and for the points listed above; each word was read on this card.

## Response to review 1

Verdict ACCEPT, with five minor findings. I re-read the crops named below. None changes a letter of the transcription; `python3 -I ciphers/hcp-1350/work/decode.py` was re-run and still gives 4 hashes OK, 78 letters and the same six lines.

1. **`t` of `Tvsqsjtf`: agreed, fixed.** On `review/work/z3.png` the head is a 3, and the four z of the card are flat-topped on `work/reading.jpg`. The "tailed cursive z" wording and the unshifted-z suggestion are withdrawn, the hcp-1353 parallel is limited to the lower half, and the sign is listed as read from the word (uncertainty 2).
2. **Irregular x and w: agreed, fixed.** Both are visible on `review/work/cmp.png` and are now disclosed (uncertainty 5).
3. **`efbstu` parallel: agreed, fixed.** hcp-1398 is cited (its lines 31 and 48-49 confirm the spelling), "slip" is no longer asserted, and the English reads dear[e]st.
4. **Postmark: agreed, fixed.** `review/work/pm.png` was checked. The town is stated as partly inferred from hcp-1354 and hcp-1353, whose SOLUTION.md files record WIMBORNE 10 PM.
5. **Count of uncertainties: fixed.** The status line now matches the list (eight, including the two added above). The report states that the review was Claude on Claude.

The reading is not changed, so no DONE2 is needed.
