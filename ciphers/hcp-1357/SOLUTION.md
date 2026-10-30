# HCP 1357 / pc_hcp_38 — Caesar (+1) love postcard, 22 March 1907

**Status: whole message read; review 1 verdict ACCEPT; closed (FINAL).** The points that rest on sense and not on the sign alone are disclosed below: the last letter of `Zpvs` is a restoration under an ink blot, the `v` of the same word is damaged, and some letter forms are anomalous (uncertainties 9 and 10).

> **My own dearest boy, this will make the pair for album. From your girl.**

Credit: capture by the orchestrator (Claude Opus 5.5, 2026-10-30); transcription and decipherment by Claude Opus 5.5 (2026-10-30). There is no earlier work on this number. The key was first established on the sister cards of this correspondence and was tested afresh here.

## Origin

HC Portal cryptogram 1357 (`pc_hcp_38`), portal status *Not solved*, with no attached transcription or solution (`source/metadata.md`, `SOURCES.md`). No published solution of this card turned up in the portal or the repo; no separate web search for one was made.

- Picture side: Raphael Tuck "Glosso" *Illustrated Hymns*, Postcard Series 5534, a printed verse of "The day is past and over" credited to J. M. Neale (translator). There is no handwriting on it.
- Address side: Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. Halfpenny Edward VII stamp; postmark WIMBORNE with PM, MR and 07 legible; the day is only partly legible and is compatible with 22. The portal's "W. Abboú" is a misreading of Abbott; the metadata file is unchanged.
- The message is on the left half of the address side and is read with the card turned 90° counter-clockwise (`work/crops/reading-2x.png`). The date "March 22nd 07" is in clear and agrees with the postmark and the portal date 1907-03-22.
- Language: English. The hand and phrasing match the Abbott series (e.g. hcp-1395, hcp-1368).

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet. Decrypt by subtracting one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

| Ciphertext | Plaintext |
|---|---|
| Nz. pxo. Efbsftu Cpz. | MY. OWN. DEAREST BOY. |
| uijt Xjmm. nblf. uif | THIS WILL. MAKE. THE |
| qbjs gps bmcvn | PAIR FOR ALBUM |
| gspn. Zpvs. Hjsm | FROM YOUR GIRL |
| (clear) March 22nd 07 | March 22nd 07 |

54 enciphered letters, one key, no per-word adjustment. Word divisions follow the handwriting; sentence punctuation in the reading is editorial.

**English (original language):** My own dearest boy, this will make the pair for album. From your girl. March 22nd 07.

**Slovak:** Môj vlastný najdrahší chlapec, toto doplní pár do albumu. Od tvojho dievčaťa. 22. marca 1907.

## Command (from the repo root)

```bash
python3 -I ciphers/hcp-1357/work/decode.py
```

It checks the SHA-256 of all four captured images, decodes `work/transcription.json` and prints the plaintext.

## Uncertainties

1. **`Zpvs` = YOUR, last letter restored.** The final sign lies inside an ink blot (`work/crops/zpvs-blot.png`), and only a pale tail runs out of it. S is the only letter making a word in `from you? girl`, and this writer's `zpvs` is standard on the sister cards. It is a disclosed restoration, not a pixel reading.
2. **`Zpvs`, the `v`.** The `v` is damaged by the same smudging: a low stroke and a stroke rising to the right can be seen, with heavier ink at the top. Z and p are clear.
3. **`qbjs`, first letter.** Its body resembles the g on this card, so GBJS (FAIR) must be excluded. On this card g has a short hooked tail (`work/crops/gps-hooked-g.png`), while the first letter of `qbjs` has a long descender closing in a loop (`work/crops/qbjs-long-looped-q.png`). That loop is the writer's q in `qptu` on hcp-1395, hcp-1368 and hcp-1376 (`work/crops/hcp1395-qptu-gspn-comparison.png`). Both pixels and sense give PAIR.
4. **`uijt`, first letter.** It has a tall first stroke and looks like h. It is this writer's tall word-initial u, as recorded in `uijt` on hcp-1358 and hcp-1362; there is no evidence that it is a capital. Taken as h the word would give GIHS, which is no word. THIS is secure from the i, j and t.
5. **Dash after `uijt`.** It is transcribed as nothing: either the bar of the t carried to the right, or a hyphen. No letter depends on it.
6. **Meaning of "pair".** The words are clear; what they refer to is not stated. Probably this card matches another one for his album, but which one is an inference. The album also appears on sister card hcp-1398.
7. **Faint marks.** A brown smudge left of "March" looks like a stain, not writing. Stain and the portal watermark overlay parts of lines 2 to 4.
8. **Dots.** Dots between words are kept as read, including the small ones after `gspn` and `Zpvs`, but some may be accidental. No letter depends on them.
9. **`Xjmm`, the j.** This sign has no dot, unlike the j's of `uijt` and `qbjs`. It has a large head loop and a hooked tail, so it is nearly the same shape as the g of `gps` (`review/work/z_j.png`). Taken literally the word would give WFLL. WILL rests on sense and on the word on hcp-1351, not on the sign alone. The minims after it number about six, which fits `mm`, but they cannot be separated one by one (`review/work/z_mm.png`).
10. **Other letter forms settled by sense.** The second f of `Efbsftu` has a closed round head and a straight descender, with no ascender or lower loop (`review/work/z_efb.png`). The c of `bmcvn` has a closed e-like top, and the v of that word is cursive and runs into the n stroke (`review/work/z_album.png`). The j of `Hjsm` has no visible dot (`review/work/z_hjsm.png`). DEARPST, ALDUM and GORL are not words. Head shape alone does not separate g, j, q and f in this hand, so the q of `qbjs` rests on its descender loop and on sense, not on the head.

## Why I believe this is correct

- One fixed shift turns all 54 letters into plain English with no per-word adjustment, including long words (DEAREST, ALBUM) and all the group types the writer normally uses.
- Word by word the shift was checked on 4–6× crops of the un-converted original, not taken from sister cards. Only the disclosed blot depends on a restoration; the anomalous signs in uncertainties 9 and 10 are settled by sense.
- The formula "My own dearest … from your girl" and the groups `Nz`, `pxo`, `Efbsftu`, `Cpz`, `gspn`, `Hjsm` recur on the Abbott cards. The clear date, postmark, recipient and Wimborne origin fit the correspondence.

## Response to review 1

Verdict ACCEPT, with four minor findings. All four are addressed. No plaintext letter changed; the reproduction command still gives 54 enciphered letters and the same plaintext.

1. **Undisclosed j in `Xjmm`: fixed.** Confirmed on `review/work/r_all.png` and `z_j.png`: there is no dot, and the head is g-like. Added as uncertainty 9, and the sentence on restorations in "Why I believe this is correct" is softened.
2. **Two omitted dots: fixed.** The dots after `gspn` and `Zpvs` are visible on `work/crops/reading-2x.png`. They are added to the table and to `work/transcription.json`, and uncertainty 8 now names them.
3. **Other letter forms: fixed.** The second f of `Efbsftu`, the c and v of `bmcvn` and the dotless j of `Hjsm` are confirmed on the reviewer's crops and disclosed as uncertainty 10, with the consequence for q.
4. **`Uijt` capital: fixed.** The transcription is now `uijt` in the table and in `work/transcription.json`, and uncertainty 4 cites hcp-1358 and hcp-1362.

One more correction made while checking the review: the postmark day and the "10" are not securely legible, so Origin now gives only what the reviewer confirmed.
