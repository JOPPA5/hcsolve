# HCP 1362 / pc_hcp_43 — Caesar −1 English love postcard, 10 April (1907)

Status: **whole message read; review 1 verdict ACCEPT, no word changed.** Five sign points are disclosed below, plus the year (now supported by the postmark and a same-day card). All work on this card by Claude Opus 5.5 (2026-10-30); no earlier work exists on this number.

## Origin

HC Portal cryptogram 1362 (`pc_hcp_43`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Picture side: printed Frith's Series view "Raglan Castle", no handwriting. Address side, plain: **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon** (portal spells the recipient "W. Abboú"); halfpenny Edward VII stamp; postmark ending "BORNE" (the visible part of the WIMBORNE seen on the sister cards), 10 PM, day 10, a faint AP left of the stamp edge level with the day, and 07 below it (`work/crops/stamp_rot.png`, `review/work/z_pm.png`). The message runs up the left half of the address side (turn the card 90° counter-clockwise; `work/crops/all.png`). The grey wheel over it is the portal's watermark, not part of the card.

## Cipher and key

Monoalphabetic Caesar shift, the same key as the Abbott sister cards hcp-1386…1407: each plaintext letter is written as the **next** letter. Decrypt by subtracting one (A→Z). The closing "G. H. April 10th" is ordinary writing.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Plaintext |
|---|---|
| Nz. Efbsftu J ibwf | MY. DEAREST I HAVE |
| pof. Mjlf. uijt | ONE. LIKE. THIS |
| Mpwf boe. Ljttft. | LOVE AND. KISSES. |
| gspn. Zpvs. pxo. | FROM. YOUR. OWN. |
| Hjsm. | GIRL. |
| (plain) G. H. April 10th | G. H. April 10th |

53 enciphered letters, all decoded by the one key. No abbreviation groups on this card.

English (the plaintext language; the portal lists Unknown): *"My dearest, I have one like this. Love and kisses from your own girl. G. H., April 10th."*

Slovak: *„Môj najdrahší, mám jednu takúto. Láska a bozky od tvojho vlastného dievčaťa. G. H., 10. apríla."*

"One like this" presumably means another card of the same view; the card does not say so.

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1362/work/decode.py
```

Checks the SHA-256 of both `source/` images and both originals in `work/hires/`, then prints the full plaintext from `work/transcription.json`, with a round-trip check of each word.

## Uncertainties

1. **`Mjlf`, capital (`work/crops/w22.png`).** The first sign is the least clean on the card: hook, arched diagonal, then a shorter arm running right that ends in a small curl, and the portal's watermark crosses it. It is cramped compared with the three-legged M of `Mpwf` on the next line. At 10x (`review/work/z_M1.png`) it has three elements: hook and diagonal, a second arched stroke falling to a foot, and a separate faint third dab just right of it, crossed by a watermark line. The `Nz` capital has two, so the shape leans to M; the third element is faint, so N (MIKE) is unlikely rather than excluded. The sentence "one like this" agrees. The third sign is a plain stem with a foot, read `l`; a `d` bowl is not visible, so `Mjdf` (LICE) is rejected on shape as well as sense.
2. **`uijt`, first signs (`work/crops/w23.png`).** Pale, partly under the watermark. The first sign has a tall first minim, so it could look like `h`/`l` + bowl at a glance. The reading rests on two dots above the word (i and j), the long j, and the final barred t with its long crossbar running to the card edge. The bar's "2"-shaped head is black fresh ink and overlaps the descender of the f of `ibwf` above.
3. **`Efbsftu`, fourth sign (`work/crops/a2.png`).** A smudged blot. Read `s` because the other six signs are clear and the word is the writer's usual greeting on the sister cards; this is a restoration of a blotted sign, not an independent reading.
4. **`boe`, last sign (`work/crops/c2.png`).** Its loop is filled with ink, so it looks c-shaped: literally `boc`, ANB. The sister notes (hcp-1363) record this writer's e as c-shaped.
5. **`Ljttft`, last two signs (`work/crops/c3.png`).** Very pale, the pen running dry, but legible: f with its looped descender, then t with a detached bar, then a dot. The two t's before them share one bar.
6. **Year.** The handwriting gives no year; 1907 rests on outside evidence, which agrees. The postmark shows a faint 0 and a plain 7 (`review/work/z_pm.png`), and the same-day card hcp-1397 is dated in clear "April 10th 1907", with the same opening `Nz. Efbsftu`. 10 April 1907 is a Wednesday. The month is in the handwriting and is independently supported by the faint AP of the postmark.
7. **`G. H.`** is left unexpanded, as on the sister cards. The G is a large open capital that could also be taken for C; hcp-1386 reads a C there.
8. **Word-dots** are the writer's habit, placed irregularly, and carry no meaning.

## Why it is correct

The key is one fixed shift taken from the sister cards, not tuned to this card, and it turns all 53 letters into a coherent message. Sign shapes were read first; `Mpwf` has the same outline as `Mpwf` on hcp-1366 (`ciphers/hcp-1366/work/crops/love.png`), `Hjsm`, `gspn`, `Zpvs`, `pxo` and `Nz` are the writer's recurring groups, and `Ljttft`, `Mjlf` and `uijt` are not formula words on the sisters yet decode cleanly. Addressee, Wimborne postmark, Frith's card and closing initials agree with the correspondence.

No published solution of this card was found: the portal lists none, and the orchestrator's check of the AI register (2026-10-30) has no record of it. Sister cards supplied the key and comparison shapes, not this card's text.

## Response to review 1

Verdict ACCEPT. All four findings were minor and I checked each on the crops. No letter of the transcription or plaintext changed, `work/transcription.json` and `work/decode.py` were not touched, and the command was re-run after these edits with the same output (source hashes OK, 53 letters).

1. **`Mjlf` capital: agreed, fixed.** `review/work/z_M1.png` shows the three elements the reviewer describes. Uncertainty 1 now says the shape leans to M. I keep the doubt because the third element is faint and crossed by the watermark.
2. **Postmark month: agreed, fixed.** On `review/work/z_pm.png` a faint triangular A stands left of the stamp edge and a bowl at the perforation, level with the day 10, then 0 and a plain 7 below. The Origin paragraph and uncertainty 6 are corrected. `NOTES.md` keeps the original line and adds a dated correction.
3. **Same-day card hcp-1397: agreed, fixed.** Its FINAL `SOLUTION.md` gives the plain date "April 10th 1907", the portal date 1907-04-10, and the postmark `...ORNE / 7 PM / AP 10 / 07`. Uncertainty 6 now cites it as context for the year.
4. **Status count: agreed, fixed.** The status line now says five sign points.
